# 💎 Integração Gemini Pro + Notion

## Visão Geral

Com sua assinatura **Gemini Advanced** (ou Gemini Pro gratuito), você pode integrar com o Notion de várias formas:

```
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│  Gemini      │ -> │ Google AI    │ -> │   Notion     │
│  (Interface) │    │ Studio/API   │    │   (API)      │
└──────────────┘    └──────────────┘    └──────────────┘
```

---

## Vantagens do Gemini

✅ **API Gratuita** com Google AI Studio  
✅ **Modelos potentes**: Gemini 1.5 Pro/Flash  
✅ **Grande contexto**: Até 2M tokens (Gemini 1.5 Pro)  
✅ **Multimodal**: Texto, imagens, vídeo, áudio  
✅ **Boa integração com Google Workspace**

---

## Método 1: Google AI Studio + Notion API

### 1.1 Obter API Key do Google AI Studio

**Passo a Passo:**
1. Vá para: https://aistudio.google.com/
2. Faça login com sua conta Google
3. Clique em "Get API Key"
4. Crie um novo projeto (ou use existente)
5. Gere a API key

**Gratuito:**
- ✅ Gemini 1.5 Flash: 15 RPM, 1M TPM
- ✅ Gemini 1.5 Pro: 2 RPM, 32K TPM
- ✅ Gemini 1.0 Pro: 15 RPM

### 1.2 Script Python - Gemini para Notion

```python
import os
import google.generativeai as genai
from notion_client import Client

# Configuração
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
NOTION_TOKEN = os.getenv("NOTION_TOKEN")
NOTION_PAGE_ID = os.getenv("NOTION_PAGE_ID")

# Inicializar clientes
genai.configure(api_key=GOOGLE_API_KEY)
notion = Client(auth=NOTION_TOKEN)

def generate_content_with_gemini(prompt, model_name="gemini-1.5-flash"):
    """Gera conteúdo usando Gemini"""
    model = genai.GenerativeModel(model_name)
    
    response = model.generate_content(
        prompt,
        generation_config={
            "temperature": 0.7,
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 8192,
        }
    )
    
    return response.text

def parse_markdown_to_notion_blocks(content):
    """Converte Markdown para blocos do Notion"""
    blocks = []
    lines = content.split('\n')
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Heading 1
        if line.startswith('# '):
            blocks.append({
                "object": "block",
                "type": "heading_1",
                "heading_1": {
                    "rich_text": [{"text": {"content": line[2:]}}]
                }
            })
        # Heading 2
        elif line.startswith('## '):
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
        elif line[0].isdigit() and line[1:].startswith('. '):
            blocks.append({
                "object": "block",
                "type": "numbered_list_item",
                "numbered_list_item": {
                    "rich_text": [{"text": {"content": line.split('. ', 1)[1]}}]
                }
            })
        # Code block (simplified)
        elif line.startswith('```'):
            continue  # Ignorar por simplicidade neste exemplo
        # Paragraph
        else:
            blocks.append({
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [{"text": {"content": line}}]
                }
            })
    
    return blocks

def send_to_notion(content):
    """Envia conteúdo para o Notion"""
    blocks = parse_markdown_to_notion_blocks(content)
    
    # Adicionar blocos à página
    notion.blocks.children.append(
        block_id=NOTION_PAGE_ID,
        children=blocks
    )
    
    return "✅ Conteúdo adicionado ao Notion!"

# Exemplo de uso
if __name__ == "__main__":
    prompt = """
    Crie um guia completo sobre como usar IA no dia a dia.
    
    Inclua:
    - Título principal
    - 3 seções principais
    - Exemplos práticos
    - Dicas e boas práticas
    
    Formate em Markdown com headers, listas e parágrafos.
    """
    
    print("💎 Gerando conteúdo com Gemini...")
    content = generate_content_with_gemini(prompt)
    
    print("📝 Enviando para o Notion...")
    result = send_to_notion(content)
    
    print(result)
    print(f"\n📄 Preview:\n{content[:500]}...")
```

### 1.3 Instalação

```bash
pip install google-generativeai notion-client python-dotenv
```

**Arquivo .env:**
```bash
GOOGLE_API_KEY=AIza...
NOTION_TOKEN=secret_...
NOTION_PAGE_ID=123abc456def...
```

---

## Método 2: Gemini Web + Extensions

### 2.1 Google Workspace Integration

Se você usa **Google Workspace** com Gemini:

1. **Gmail + Notion:**
   - Use Gemini para gerar resposta de email
   - Copie para Notion via Web Clipper

2. **Google Docs + Notion:**
   - Use "Help me write" do Gemini no Docs
   - Exporte para Notion via integração nativa

3. **Google Sheets + Notion:**
   - Gemini pode analisar dados em Sheets
   - Exporte resultados para Notion database

### 2.2 Browser Extensions

**Opção A - Notion Web Clipper:**
1. Use Gemini em gemini.google.com
2. Clipe conteúdo para Notion

**Opção B - Integração via Shortcuts:**
- Use Google Apps Script para automação
- Conecte Gemini API + Notion API

---

## Método 3: Análise Multimodal

### 3.1 Analisar Imagens e Enviar para Notion

```python
import PIL.Image

def analyze_image_and_send_to_notion(image_path, query):
    """Analisa imagem com Gemini Vision e envia para Notion"""
    
    # Carregar imagem
    img = PIL.Image.open(image_path)
    
    # Modelo multimodal
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # Gerar análise
    prompt = f"{query}\n\nBaseado na imagem, forneça uma análise detalhada."
    response = model.generate_content([prompt, img])
    
    # Enviar para Notion
    blocks = parse_markdown_to_notion_blocks(response.text)
    
    # Adicionar imagem também
    blocks.insert(0, {
        "object": "block",
        "type": "image",
        "image": {
            "type": "external",
            "external": {"url": "URL_DA_IMAGEM"}  # Upload para CDN antes
        }
    })
    
    notion.blocks.children.append(
        block_id=NOTION_PAGE_ID,
        children=blocks
    )
    
    return "✅ Análise enviada ao Notion!"

# Exemplo de uso
analyze_image_and_send_to_notion(
    "screenshot.png",
    "Analise este dashboard e forneça insights"
)
```

### 3.2 Processar PDFs

```python
def process_pdf_with_gemini(pdf_path):
    """Processa PDF com Gemini e envia resumo para Notion"""
    
    # Upload do PDF
    file = genai.upload_file(pdf_path)
    
    # Modelo
    model = genai.GenerativeModel('gemini-1.5-pro')
    
    # Gerar resumo
    response = model.generate_content([
        "Resuma este documento em tópicos principais. "
        "Inclua conclusões e pontos de ação.",
        file
    ])
    
    # Enviar para Notion
    send_to_notion(response.text)
    
    return "✅ Resumo do PDF enviado ao Notion!"
```

---

## Método 4: Integração com Google Apps Script

### 4.1 Automatizar de Google Sheets para Notion

```javascript
// Google Apps Script
function generateWithGeminiAndSendToNotion() {
  // 1. Obter dados do Google Sheet
  var sheet = SpreadsheetApp.getActiveSheet();
  var data = sheet.getDataRange().getValues();
  
  // 2. Chamar Gemini API
  var apiKey = 'YOUR_GOOGLE_API_KEY';
  var url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=' + apiKey;
  
  var payload = {
    "contents": [{
      "parts": [{
        "text": "Analise estes dados e crie um relatório: " + JSON.stringify(data)
      }]
    }]
  };
  
  var options = {
    'method': 'post',
    'contentType': 'application/json',
    'payload': JSON.stringify(payload)
  };
  
  var response = UrlFetchApp.fetch(url, options);
  var geminiResult = JSON.parse(response.getContentText());
  var content = geminiResult.candidates[0].content.parts[0].text;
  
  // 3. Enviar para Notion
  var notionToken = 'YOUR_NOTION_TOKEN';
  var pageId = 'YOUR_PAGE_ID';
  
  var notionUrl = 'https://api.notion.com/v1/blocks/' + pageId + '/children';
  
  var notionPayload = {
    "children": [{
      "object": "block",
      "type": "paragraph",
      "paragraph": {
        "rich_text": [{
          "text": {"content": content}
        }]
      }
    }]
  };
  
  var notionOptions = {
    'method': 'patch',
    'contentType': 'application/json',
    'headers': {
      'Authorization': 'Bearer ' + notionToken,
      'Notion-Version': '2022-06-28'
    },
    'payload': JSON.stringify(notionPayload)
  };
  
  UrlFetchApp.fetch(notionUrl, notionOptions);
  
  Logger.log('✅ Conteúdo enviado ao Notion!');
}
```

---

## Método 5: Via Make.com (Gratuito)

### 5.1 Cenário no Make.com

```
Google AI (Gemini) → Text Parser → Notion (Create Page)
```

**Configuração:**
1. Crie conta em: https://www.make.com
2. Adicione módulo "HTTP Request" para Gemini API
3. Adicione módulo "Notion"
4. Conecte e teste

**Benefícios:**
- Visual, sem código
- 1000 operações/mês grátis
- Agendamento automático

---

## Use Cases Práticos

### 1. Resumir Longos Documentos

```python
def summarize_long_document(text):
    """Usa contexto longo do Gemini (até 2M tokens)"""
    
    prompt = f"""
    Analise este documento e crie:
    1. Resumo executivo (3 parágrafos)
    2. Principais insights (5 tópicos)
    3. Recomendações (3 ações)
    
    Documento:
    {text}
    """
    
    # Gemini 1.5 Pro suporta até 2M tokens!
    content = generate_content_with_gemini(prompt, "gemini-1.5-pro")
    send_to_notion(content)
```

### 2. Análise de Sentimento de Feedback

```python
def analyze_customer_feedback(feedbacks):
    """Analisa múltiplos feedbacks e cria relatório"""
    
    prompt = f"""
    Analise estes feedbacks de clientes:
    
    {feedbacks}
    
    Forneça:
    - Sentimento geral (positivo/neutro/negativo)
    - Temas recorrentes
    - Sugestões de melhorias
    
    Formate como relatório executivo.
    """
    
    analysis = generate_content_with_gemini(prompt)
    send_to_notion(analysis)
```

### 3. Geração de Conteúdo Estruturado

```python
def create_weekly_plan(topics):
    """Cria plano semanal estruturado"""
    
    prompt = f"""
    Crie um plano semanal para estes tópicos: {topics}
    
    Para cada dia (Segunda a Sexta):
    - Tarefa principal
    - Objetivo
    - Tempo estimado
    - Recursos necessários
    
    Formate em Markdown com tabelas.
    """
    
    plan = generate_content_with_gemini(prompt, "gemini-1.5-flash")
    send_to_notion(plan)
```

### 4. Tradução e Localização

```python
def translate_and_send_to_notion(text, target_language="pt-BR"):
    """Traduz conteúdo e envia para Notion"""
    
    prompt = f"""
    Traduza o seguinte texto para {target_language}.
    Mantenha a formatação Markdown.
    
    Texto:
    {text}
    """
    
    translated = generate_content_with_gemini(prompt)
    send_to_notion(translated)
```

---

## Comparação: Gemini vs GPT para Notion

| Característica | Gemini | GPT-4 |
|----------------|--------|-------|
| **API Gratuita** | ✅ Sim | ❌ Paga |
| **Contexto** | 2M tokens | 128K tokens |
| **Multimodal** | ✅ Nativo | ✅ Limitado |
| **Velocidade** | ⚡ Rápido (Flash) | ⭐ Médio |
| **Qualidade** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Custo (se pago)** | Mais barato | Mais caro |

**Recomendação:**
- Use **Gemini 1.5 Flash** para geração rápida e gratuita
- Use **Gemini 1.5 Pro** para documentos longos
- Use **GPT-4** se precisar de máxima qualidade (e tiver budget)

---

## Rate Limits (Gratuito)

```
Gemini 1.5 Flash:
- 15 requests por minuto
- 1 milhão de tokens por minuto

Gemini 1.5 Pro:
- 2 requests por minuto  
- 32K tokens por minuto

Gemini 1.0 Pro:
- 15 requests por minuto
```

**Implementar rate limiting:**

```python
import time
from functools import wraps

def rate_limit(calls_per_minute):
    interval = 60.0 / calls_per_minute
    def decorator(func):
        last_called = [0.0]
        @wraps(func)
        def wrapper(*args, **kwargs):
            elapsed = time.time() - last_called[0]
            wait_time = interval - elapsed
            if wait_time > 0:
                time.sleep(wait_time)
            result = func(*args, **kwargs)
            last_called[0] = time.time()
            return result
        return wrapper
    return decorator

@rate_limit(15)  # 15 RPM
def safe_generate_content(prompt):
    return generate_content_with_gemini(prompt)
```

---

## Troubleshooting

### Erro: "API key not valid"
- Verifique se copiou a key completa
- Confirme que a API está habilitada no Google Cloud Console

### Erro: "Resource exhausted"
- Você excedeu o rate limit
- Adicione delays entre requisições
- Considere usar Gemini Flash (limite maior)

### Erro: "Invalid argument"
- Verifique o formato do prompt
- Confirme que o modelo suporta sua requisição

### Conteúdo cortado
- Use Gemini 1.5 Pro para contextos maiores
- Divida em múltiplas requisições se necessário

---

## Recursos Adicionais

- 📖 **Google AI Studio**: https://aistudio.google.com/
- 🔧 **Documentação**: https://ai.google.dev/docs
- 💬 **Gemini API Cookbook**: https://github.com/google-gemini/cookbook
- 🎓 **Tutoriais**: https://ai.google.dev/tutorials

---

## Custos (Se ultrapassar plano gratuito)

**Gemini API Pricing:**
```
Gemini 1.5 Flash:
- Input:  $0.075 / 1M tokens
- Output: $0.30 / 1M tokens

Gemini 1.5 Pro:
- Input:  $1.25 / 1M tokens (≤128K context)
- Output: $5.00 / 1M tokens

💡 Ainda mais barato que GPT-4!
```

---

## Próximos Passos

- → **[Integração com Perplexity](04-Integracao-Perplexity.md)**
- → **[Soluções Open Source](05-Solucoes-Open-Source.md)**
- → **[Scripts de Exemplo](07-Scripts-Exemplos/)**
