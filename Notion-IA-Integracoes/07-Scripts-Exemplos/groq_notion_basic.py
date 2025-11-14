"""
Script de exemplo: Groq AI + Notion
Gera conteúdo usando Groq (gratuito) e envia para o Notion

Requisitos:
    pip install groq notion-client python-dotenv

Variáveis de Ambiente (.env):
    GROQ_API_KEY=gsk_...
    NOTION_TOKEN=secret_...
    NOTION_PAGE_ID=...
"""

import os
from groq import Groq
from notion_client import Client
from dotenv import load_dotenv
import time

# Carregar variáveis de ambiente
load_dotenv()

# Configuração
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
NOTION_TOKEN = os.getenv("NOTION_TOKEN")
NOTION_PAGE_ID = os.getenv("NOTION_PAGE_ID")

# Inicializar clientes
groq_client = Groq(api_key=GROQ_API_KEY)
notion = Client(auth=NOTION_TOKEN)


def generate_content_with_groq(prompt, model="llama-3.1-70b-versatile"):
    """
    Gera conteúdo usando Groq AI (GRATUITO!)
    
    Modelos disponíveis:
    - llama-3.1-70b-versatile (recomendado)
    - llama-3.1-8b-instant (mais rápido)
    - mixtral-8x7b-32768 (grande contexto)
    - gemma2-9b-it (Google Gemma)
    """
    try:
        chat_completion = groq_client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "Você é um assistente especializado em criar conteúdo estruturado em Markdown para Notion. Seja claro, objetivo e bem formatado."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model=model,
            temperature=0.7,
            max_tokens=4000,
            top_p=1,
            stream=False
        )
        
        return chat_completion.choices[0].message.content
    
    except Exception as e:
        print(f"❌ Erro ao gerar conteúdo: {e}")
        return None


def parse_markdown_to_notion_blocks(content):
    """
    Converte Markdown para blocos do Notion
    
    Suporta:
    - Headers (# ## ###)
    - Listas (- *)
    - Listas numeradas (1. 2. 3.)
    - Parágrafos
    - Code blocks (```)
    """
    blocks = []
    lines = content.split('\n')
    
    in_code_block = False
    code_content = []
    code_language = ""
    
    for line in lines:
        # Code blocks
        if line.strip().startswith('```'):
            if not in_code_block:
                in_code_block = True
                code_language = line.strip()[3:].strip() or "plain text"
                code_content = []
            else:
                # Finalizar code block
                blocks.append({
                    "object": "block",
                    "type": "code",
                    "code": {
                        "rich_text": [{
                            "text": {"content": '\n'.join(code_content)}
                        }],
                        "language": code_language
                    }
                })
                in_code_block = False
                code_content = []
            continue
        
        if in_code_block:
            code_content.append(line)
            continue
        
        line = line.strip()
        if not line:
            continue
        
        # Heading 1
        if line.startswith('# ') and not line.startswith('## '):
            blocks.append({
                "object": "block",
                "type": "heading_1",
                "heading_1": {
                    "rich_text": [{"text": {"content": line[2:]}}]
                }
            })
        # Heading 2
        elif line.startswith('## ') and not line.startswith('### '):
            blocks.append({
                "object": "block",
                "type": "heading_2",
                "heading_2": {
                    "rich_text": [{"text": {"content": line[3:]}}]
                }
            })
        # Heading 3
        elif line.startswith('### '):
            blocks.append({
                "object": "block",
                "type": "heading_3",
                "heading_3": {
                    "rich_text": [{"text": {"content": line[4:]}}]
                }
            })
        # Bullet list
        elif line.startswith('- ') or line.startswith('* '):
            blocks.append({
                "object": "block",
                "type": "bulleted_list_item",
                "bulleted_list_item": {
                    "rich_text": [{"text": {"content": line[2:]}}]
                }
            })
        # Numbered list
        elif len(line) > 2 and line[0].isdigit() and line[1:3] in ['. ', ') ']:
            content = line.split('. ', 1)[1] if '. ' in line else line.split(') ', 1)[1]
            blocks.append({
                "object": "block",
                "type": "numbered_list_item",
                "numbered_list_item": {
                    "rich_text": [{"text": {"content": content}}]
                }
            })
        # Paragraph
        else:
            # Limitar tamanho do texto (Notion tem limite de 2000 chars)
            if len(line) > 1900:
                # Dividir em múltiplos parágrafos
                chunks = [line[i:i+1900] for i in range(0, len(line), 1900)]
                for chunk in chunks:
                    blocks.append({
                        "object": "block",
                        "type": "paragraph",
                        "paragraph": {
                            "rich_text": [{"text": {"content": chunk}}]
                        }
                    })
            else:
                blocks.append({
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {
                        "rich_text": [{"text": {"content": line}}]
                    }
                })
    
    return blocks


def send_to_notion(content, page_id=None):
    """
    Envia conteúdo para o Notion
    """
    if page_id is None:
        page_id = NOTION_PAGE_ID
    
    try:
        blocks = parse_markdown_to_notion_blocks(content)
        
        # Notion API tem limite de 100 blocos por request
        # Dividir em chunks se necessário
        chunk_size = 100
        for i in range(0, len(blocks), chunk_size):
            chunk = blocks[i:i+chunk_size]
            
            notion.blocks.children.append(
                block_id=page_id,
                children=chunk
            )
            
            # Rate limiting (3 requests/segundo)
            if i + chunk_size < len(blocks):
                time.sleep(0.35)
        
        return True, f"✅ {len(blocks)} blocos adicionados ao Notion!"
    
    except Exception as e:
        return False, f"❌ Erro ao enviar para Notion: {e}"


def main():
    """
    Exemplo de uso
    """
    print("🚀 Iniciando geração de conteúdo...\n")
    
    # Prompt de exemplo
    prompt = """
    Crie um guia completo sobre como usar IA no dia a dia profissional.
    
    Inclua:
    - Introdução sobre o impacto da IA
    - 5 ferramentas de IA úteis com descrições
    - Dicas práticas de implementação
    - Conclusão com próximos passos
    
    Formate em Markdown com headers, listas e seções bem organizadas.
    """
    
    print("💭 Prompt enviado para Groq AI...")
    content = generate_content_with_groq(prompt)
    
    if content:
        print(f"\n📝 Conteúdo gerado ({len(content)} caracteres)")
        print("─" * 60)
        print(content[:500] + "..." if len(content) > 500 else content)
        print("─" * 60)
        
        print("\n📤 Enviando para o Notion...")
        success, message = send_to_notion(content)
        print(message)
        
        if success:
            print("\n🎉 Processo concluído com sucesso!")
        else:
            print("\n⚠️ Houve um problema ao enviar para o Notion")
    else:
        print("\n❌ Falha ao gerar conteúdo")


if __name__ == "__main__":
    # Verificar se as variáveis de ambiente estão configuradas
    if not all([GROQ_API_KEY, NOTION_TOKEN, NOTION_PAGE_ID]):
        print("❌ Erro: Configure as variáveis de ambiente no arquivo .env")
        print("\nCrie um arquivo .env com:")
        print("GROQ_API_KEY=gsk_...")
        print("NOTION_TOKEN=secret_...")
        print("NOTION_PAGE_ID=...")
    else:
        main()
