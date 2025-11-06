"""
Script de exemplo: Google Gemini + Notion
Gera conteúdo usando Gemini (gratuito) e envia para o Notion

Requisitos:
    pip install google-generativeai notion-client python-dotenv

Variáveis de Ambiente (.env):
    GOOGLE_API_KEY=AIza...
    NOTION_TOKEN=secret_...
    NOTION_PAGE_ID=...
"""

import os
import google.generativeai as genai
from notion_client import Client
from dotenv import load_dotenv
import time

# Carregar variáveis de ambiente
load_dotenv()

# Configuração
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
NOTION_TOKEN = os.getenv("NOTION_TOKEN")
NOTION_PAGE_ID = os.getenv("NOTION_PAGE_ID")

# Inicializar clientes
genai.configure(api_key=GOOGLE_API_KEY)
notion = Client(auth=NOTION_TOKEN)


def generate_content_with_gemini(prompt, model_name="gemini-1.5-flash"):
    """
    Gera conteúdo usando Google Gemini (GRATUITO!)
    
    Modelos disponíveis:
    - gemini-1.5-flash (recomendado - rápido e gratuito)
    - gemini-1.5-pro (mais poderoso, contexto até 2M tokens)
    - gemini-1.0-pro (versão anterior)
    """
    try:
        model = genai.GenerativeModel(model_name)
        
        response = model.generate_content(
            prompt,
            generation_config={
                "temperature": 0.7,
                "top_p": 0.95,
                "top_k": 40,
                "max_output_tokens": 8192,
            },
            safety_settings=[
                {
                    "category": "HARM_CATEGORY_HARASSMENT",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
                },
                {
                    "category": "HARM_CATEGORY_HATE_SPEECH",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
                },
            ]
        )
        
        return response.text
    
    except Exception as e:
        print(f"❌ Erro ao gerar conteúdo: {e}")
        return None


def parse_markdown_to_notion_blocks(content):
    """
    Converte Markdown para blocos do Notion
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
        
        # Headers
        if line.startswith('# ') and not line.startswith('## '):
            blocks.append({
                "object": "block",
                "type": "heading_1",
                "heading_1": {
                    "rich_text": [{"text": {"content": line[2:]}}]
                }
            })
        elif line.startswith('## ') and not line.startswith('### '):
            blocks.append({
                "object": "block",
                "type": "heading_2",
                "heading_2": {
                    "rich_text": [{"text": {"content": line[3:]}}]
                }
            })
        elif line.startswith('### '):
            blocks.append({
                "object": "block",
                "type": "heading_3",
                "heading_3": {
                    "rich_text": [{"text": {"content": line[4:]}}]
                }
            })
        # Lists
        elif line.startswith('- ') or line.startswith('* '):
            blocks.append({
                "object": "block",
                "type": "bulleted_list_item",
                "bulleted_list_item": {
                    "rich_text": [{"text": {"content": line[2:]}}]
                }
            })
        elif len(line) > 2 and line[0].isdigit() and line[1:3] in ['. ', ') ']:
            content = line.split('. ', 1)[1] if '. ' in line else line.split(') ', 1)[1]
            blocks.append({
                "object": "block",
                "type": "numbered_list_item",
                "numbered_list_item": {
                    "rich_text": [{"text": {"content": content}}]
                }
            })
        # Paragraphs
        else:
            if len(line) > 1900:
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
        
        # Dividir em chunks de 100 blocos
        chunk_size = 100
        for i in range(0, len(blocks), chunk_size):
            chunk = blocks[i:i+chunk_size]
            
            notion.blocks.children.append(
                block_id=page_id,
                children=chunk
            )
            
            if i + chunk_size < len(blocks):
                time.sleep(0.35)
        
        return True, f"✅ {len(blocks)} blocos adicionados ao Notion!"
    
    except Exception as e:
        return False, f"❌ Erro ao enviar para Notion: {e}"


def create_study_guide(topic):
    """
    Cria um guia de estudos usando Gemini
    """
    prompt = f"""
    Crie um guia de estudos completo sobre: {topic}
    
    Estrutura:
    1. Introdução (por que aprender isso?)
    2. Pré-requisitos necessários
    3. Conceitos fundamentais (5-7 tópicos principais)
    4. Plano de estudos de 30 dias
    5. Recursos recomendados (livros, cursos, sites)
    6. Projetos práticos para consolidar conhecimento
    7. Próximos passos após dominar o básico
    
    Formate em Markdown bem estruturado.
    Use listas, headers e seções claras.
    """
    
    print(f"📚 Gerando guia de estudos: {topic}...")
    content = generate_content_with_gemini(prompt, model_name="gemini-1.5-flash")
    
    if content:
        print(f"✅ Conteúdo gerado ({len(content)} caracteres)")
        return content
    return None


def analyze_long_document(document_text):
    """
    Analisa documento longo usando Gemini 1.5 Pro (contexto de 2M tokens)
    """
    prompt = f"""
    Analise o seguinte documento e forneça:
    
    1. Resumo Executivo (3 parágrafos)
    2. Principais Insights (5-7 pontos)
    3. Temas Recorrentes
    4. Recomendações Práticas
    5. Conclusões
    
    Documento:
    {document_text}
    """
    
    print("🔍 Analisando documento...")
    # Usar gemini-1.5-pro para documentos grandes
    content = generate_content_with_gemini(prompt, model_name="gemini-1.5-pro")
    
    if content:
        print(f"✅ Análise completa ({len(content)} caracteres)")
        return content
    return None


def main():
    """
    Exemplo de uso
    """
    print("🚀 Script Gemini + Notion\n")
    
    # Exemplo 1: Criar guia de estudos
    topic = "Machine Learning para iniciantes"
    content = create_study_guide(topic)
    
    if content:
        print("\n📝 Preview do conteúdo:")
        print("─" * 60)
        print(content[:600] + "..." if len(content) > 600 else content)
        print("─" * 60)
        
        print("\n📤 Enviando para o Notion...")
        success, message = send_to_notion(content)
        print(message)
    
    # Exemplo 2: Gerar conteúdo customizado
    custom_prompt = """
    Crie um artigo sobre as 10 melhores práticas de produtividade com IA.
    
    Para cada prática, inclua:
    - Descrição
    - Ferramenta recomendada
    - Exemplo de uso
    - Benefício esperado
    
    Formato: Markdown com headers e listas.
    """
    
    print("\n\n💡 Gerando artigo customizado...")
    custom_content = generate_content_with_gemini(custom_prompt)
    
    if custom_content:
        print(f"✅ Artigo gerado ({len(custom_content)} caracteres)")
        
        # Adicionar um divisor no Notion antes do segundo conteúdo
        notion.blocks.children.append(
            block_id=NOTION_PAGE_ID,
            children=[
                {
                    "object": "block",
                    "type": "divider",
                    "divider": {}
                }
            ]
        )
        
        success, message = send_to_notion(custom_content)
        print(message)
    
    print("\n🎉 Processo concluído!")


if __name__ == "__main__":
    if not all([GOOGLE_API_KEY, NOTION_TOKEN, NOTION_PAGE_ID]):
        print("❌ Erro: Configure as variáveis de ambiente no arquivo .env")
        print("\nCrie um arquivo .env com:")
        print("GOOGLE_API_KEY=AIza...")
        print("NOTION_TOKEN=secret_...")
        print("NOTION_PAGE_ID=...")
    else:
        main()
