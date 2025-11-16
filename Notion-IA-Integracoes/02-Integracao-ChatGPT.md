# 🤖 Integração ChatGPT + Notion

## Visão Geral

Com sua assinatura do **ChatGPT Plus**, você pode integrar o GPT-4 com o Notion de várias formas:

```
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│  ChatGPT     │ -> │ OpenAI API   │ -> │   Notion     │
│  (Interface) │    │ (Programático)│   │   (API)      │
└──────────────┘    └──────────────┘    └──────────────┘
```

---

## Método 1: ChatGPT Web + Copy/Paste + Automação

### 1.1 Manualmente (Mais Simples)

**Fluxo:**
1. Use ChatGPT para gerar conteúdo
2. Copie a resposta
3. Cole no Notion

**Dica:** Use prompts otimizados para gerar formato Markdown que o Notion aceita bem.

### 1.2 Com Extensão de Browser

**Opção A - Notion Web Clipper + ChatGPT:**
1. Instale: [Notion Web Clipper](https://www.notion.so/web-clipper)
2. No ChatGPT, gere o conteúdo
3. Clique no Web Clipper para enviar ao Notion

**Opção B - Shortcuts Custom:**
Use ferramentas como:
- **Text Blaze** (Chrome): Criar snippets automáticos
- **Alfred** (Mac): Workflows customizados
- **AutoHotkey** (Windows): Scripts de automação

---

## Método 2: OpenAI API + Notion API (Programático)

### 2.1 Obter Acesso à API da OpenAI

⚠️ **IMPORTANTE**: 
- ChatGPT Plus ≠ API Access
- A API é separada e tem custo por uso
- MAS: Você pode usar modelos mais baratos (GPT-3.5-turbo)

**Setup:**
1. Vá para: https://platform.openai.com/
2. Crie uma conta (pode ser a mesma do ChatGPT)
3. Adicione método de pagamento
4. Gere uma API Key em: https://platform.openai.com/api-keys

**Custos da API (referência):**
```
GPT-3.5-turbo:  $0.0005 / 1K tokens (~$0.50 para 1 milhão de tokens)
GPT-4-turbo:    $0.01 / 1K tokens de entrada
GPT-4o:         $0.005 / 1K tokens de entrada
GPT-4o-mini:    $0.000150 / 1K tokens (mais barato)
```

### 2.2 Script Python - ChatGPT para Notion

```python
import os
from openai import OpenAI
from notion_client import Client

# Configuração
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
NOTION_TOKEN = os.getenv("NOTION_TOKEN")
NOTION_PAGE_ID = os.getenv("NOTION_PAGE_ID")

# Inicializar clientes
openai_client = OpenAI(api_key=OPENAI_API_KEY)
notion = Client(auth=NOTION_TOKEN)

def generate_content_with_gpt(prompt, model="gpt-4o-mini"):
    """Gera conteúdo usando GPT"""
    response = openai_client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "Você é um assistente que cria conteúdo estruturado em Markdown para Notion."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=2000
    )
    return response.choices[0].message.content

def send_to_notion(title, content):
    """Envia conteúdo para o Notion"""
    # Dividir conteúdo em blocos
    blocks = []
    
    # Adicionar título
    blocks.append({
        "object": "block",
        "type": "heading_2",
        "heading_2": {
            "rich_text": [{"text": {"content": title}}]
        }
    })
    
    # Adicionar conteúdo (dividido em parágrafos)
    for paragraph in content.split('\n\n'):
        if paragraph.strip():
            blocks.append({
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [{"text": {"content": paragraph}}]
                }
            })
    
    # Criar página no Notion
    notion.blocks.children.append(
        block_id=NOTION_PAGE_ID,
        children=blocks
    )
    
    return "✅ Conteúdo adicionado ao Notion!"

# Exemplo de uso
if __name__ == "__main__":
    prompt = """
    Crie um resumo executivo sobre as tendências de IA em 2024.
    Inclua 3 pontos principais com exemplos práticos.
    Formate em Markdown.
    """
    
    print("🤖 Gerando conteúdo com GPT...")
    content = generate_content_with_gpt(prompt)
    
    print("📝 Enviando para o Notion...")
    result = send_to_notion("Tendências de IA 2024", content)
    
    print(result)
```

### 2.3 Instalação

```bash
pip install openai notion-client python-dotenv
```

**Arquivo .env:**
```bash
OPENAI_API_KEY=sk-proj-...
NOTION_TOKEN=secret_...
NOTION_PAGE_ID=123abc456def...
```

---

## Método 3: GPTs Customizados com Actions

### 3.1 Criar um GPT com Notion Integration

**Requisitos:**
- ChatGPT Plus ou Team
- Acesso ao GPT Builder

**Passo a Passo:**

1. **Criar o GPT:**
   - Vá em: https://chat.openai.com/gpts/editor
   - Clique em "Create a GPT"

2. **Configurar:**
   ```
   Nome: "Notion Content Creator"
   Descrição: "Cria e envia conteúdo diretamente para o Notion"
   Instruções: "Você é um assistente que ajuda a criar conteúdo 
                estruturado e envia para o Notion do usuário."
   ```

3. **Adicionar Action (Chamada de API):**

   **OpenAPI Schema:**
   ```yaml
   openapi: 3.1.0
   info:
     title: Notion API Integration
     version: 1.0.0
   servers:
     - url: https://api.notion.com/v1
   paths:
     /blocks/{block_id}/children:
       patch:
         operationId: appendBlocks
         summary: Adiciona blocos a uma página
         parameters:
           - name: block_id
             in: path
             required: true
             schema:
               type: string
         requestBody:
           required: true
           content:
             application/json:
               schema:
                 type: object
                 properties:
                   children:
                     type: array
         responses:
           '200':
             description: Sucesso
   ```

4. **Configurar Autenticação:**
   - Tipo: API Key
   - Header: Authorization
   - Valor: `Bearer secret_YOUR_NOTION_TOKEN`
   - Header adicional: `Notion-Version: 2022-06-28`

5. **Usar o GPT:**
   ```
   Você: "Crie um plano de estudos de Python para iniciantes 
          e envie para o Notion"
   
   GPT: [Gera o conteúdo e usa a Action para enviar ao Notion]
   ```

### 3.2 Limitações

- ⚠️ Requer configuração manual da Action
- ⚠️ Precisa expor o token do Notion (use com cuidado)
- ⚠️ Apenas para uso pessoal (não compartilhe o GPT com o token)

---

## Método 4: Via Zapier/Make.com

### 4.1 Zapier (Plano Gratuito Disponível)

**Trigger:** Webhook
**Action:** Notion - Create Page

**Configuração:**
1. Crie um Zap: Webhooks → Notion
2. Use ChatGPT para gerar conteúdo
3. Envie via webhook (usando script ou ferramenta)

### 4.2 Make.com (Plano Gratuito: 1000 ops/mês)

**Cenário:**
```
OpenAI (GPT-4) → Text Parser → Notion (Create Page)
```

**Benefícios:**
- Interface visual
- Sem programação necessária
- Agendamento automático

---

## Método 5: GitHub Copilot + Notion

Se você tem **GitHub Copilot**:

### 5.1 VS Code Extension

1. Use Copilot para gerar conteúdo
2. Copilot pode sugerir código que interage com Notion API
3. Execute scripts diretamente do VS Code

**Exemplo de prompt para Copilot:**
```python
# Gerar um artigo sobre clean code e enviar para Notion
# usando a API do Notion com autenticação
```

### 5.2 Copilot Chat

```
Você: "Escreva um script Python que:
1. Gera conteúdo sobre Design Patterns
2. Formata em blocos do Notion
3. Envia via API para meu workspace"

Copilot: [Gera o script completo]
```

---

## Use Cases Práticos

### 1. Resumir Artigos

```python
def summarize_article_to_notion(article_url):
    # 1. Extrair conteúdo do artigo (com BeautifulSoup ou similar)
    article_text = extract_content(article_url)
    
    # 2. Resumir com GPT
    summary = generate_content_with_gpt(
        f"Resuma este artigo em 3 parágrafos: {article_text}",
        model="gpt-4o-mini"
    )
    
    # 3. Enviar para Notion
    send_to_notion(f"Resumo: {article_url}", summary)
```

### 2. Gerar Conteúdo Estruturado

```python
def create_meeting_notes(meeting_topic):
    prompt = f"""
    Crie notas de reunião para o tópico: {meeting_topic}
    
    Inclua:
    - Agenda (3 itens)
    - Discussão (formato de tópicos)
    - Action Items (3 itens com responsáveis)
    - Próximos Passos
    
    Formate em Markdown.
    """
    
    content = generate_content_with_gpt(prompt)
    send_to_notion(f"Reunião: {meeting_topic}", content)
```

### 3. Análise de Dados

```python
def analyze_data_and_report(data_description):
    prompt = f"""
    Analise os seguintes dados e crie um relatório executivo:
    {data_description}
    
    Inclua:
    - Insights principais
    - Tendências identificadas
    - Recomendações
    """
    
    analysis = generate_content_with_gpt(prompt, model="gpt-4o")
    send_to_notion("Análise de Dados", analysis)
```

---

## Workflow Recomendado

### Setup Inicial (Uma Vez):
1. Configure Notion API (10 min)
2. Configure OpenAI API (5 min)
3. Instale dependências Python (2 min)
4. Teste o script básico (5 min)

### Uso Diário:
1. Identifique tarefa que quer automatizar
2. Ajuste o prompt do GPT
3. Execute o script
4. Confira no Notion

---

## Custos Estimados

### Cenário: 100 gerações por mês

**Usando GPT-4o-mini (recomendado):**
```
Input:  1000 tokens/geração = 100K tokens = $0.015
Output: 500 tokens/geração  = 50K tokens  = $0.060
Total: ~$0.08/mês
```

**Usando GPT-3.5-turbo:**
```
Total: ~$0.05/mês
```

💡 **Muito mais barato que Notion AI ($10/mês)!**

---

## Alternativas Gratuitas

Se não quiser usar a API da OpenAI:

### 1. OpenRouter
- Acesso a vários modelos via uma API
- Alguns modelos gratuitos
- https://openrouter.ai/

### 2. Groq (Grátis!)
- LLaMA 3, Mixtral, etc.
- API gratuita com rate limits generosos
- https://console.groq.com/

### 3. Google AI Studio (Gemini)
- Gemini Pro gratuitamente
- Veja: `03-Integracao-Gemini.md`

---

## Troubleshooting

### Erro: "invalid_request_error"
- Verifique se a API key está correta
- Confirme que tem créditos na conta OpenAI

### Erro: Rate limit atingido
- API OpenAI: 3 requests/min (tier gratuito)
- Adicione delays entre chamadas

### Conteúdo não aparece formatado no Notion
- Use a estrutura de blocos correta
- Consulte: https://developers.notion.com/reference/block

---

## Próximos Passos

- → **[Integração com Gemini](03-Integracao-Gemini.md)** - Alternativa gratuita
- → **[Scripts de Exemplo](07-Scripts-Exemplos/)** - Código pronto para usar
- → **[Automações](06-Automacoes-Zapier-Make.md)** - No-code solutions
