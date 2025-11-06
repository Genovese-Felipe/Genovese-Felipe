# 📦 Scripts de Exemplo

Scripts prontos para usar com Notion + IA.

## 📋 Conteúdo

### Scripts Principais

1. **`groq_notion_basic.py`** - Groq AI + Notion (RECOMENDADO)
   - ✅ 100% Gratuito
   - ⚡ Muito rápido
   - 🎯 Fácil de usar

2. **`gemini_notion.py`** - Google Gemini + Notion
   - ✅ API gratuita
   - 🧠 Contexto de até 2M tokens
   - 🎨 Multimodal (texto, imagem, vídeo)

3. **`notion_helpers.py`** - Funções auxiliares
   - 🔧 Helpers para criar blocos
   - 📄 Templates prontos
   - 🗂️ Funções de database

## 🚀 Quick Start

### 1. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 2. Configurar Variáveis de Ambiente

Crie um arquivo `.env` na raiz:

```bash
# Groq (Gratuito)
GROQ_API_KEY=gsk_...

# Gemini (Gratuito)
GOOGLE_API_KEY=AIza...

# Notion
NOTION_TOKEN=secret_...
NOTION_PAGE_ID=...
```

### 3. Executar

**Groq + Notion:**
```bash
python groq_notion_basic.py
```

**Gemini + Notion:**
```bash
python gemini_notion.py
```

## 📖 Como Obter API Keys

### Groq (Grátis)
1. Vá para: https://console.groq.com/
2. Crie conta (sem cartão de crédito)
3. "API Keys" → "Create API Key"
4. Copie a key que começa com `gsk_`

### Google Gemini (Grátis)
1. Vá para: https://aistudio.google.com/
2. Faça login com Google
3. "Get API Key"
4. Copie a key que começa com `AIza`

### Notion
1. Vá para: https://www.notion.so/my-integrations
2. "New integration"
3. Copie o "Integration Token"
4. Compartilhe a página com sua integração

## 💡 Exemplos de Uso

### Gerar Conteúdo Simples

```python
from groq_notion_basic import generate_content_with_groq, send_to_notion

# Gerar
content = generate_content_with_groq("Crie um artigo sobre Python")

# Enviar para Notion
send_to_notion(content)
```

### Criar Estrutura Complexa

```python
from notion_helpers import *

blocks = [
    create_heading("Meu Projeto", 1),
    create_callout("Projeto iniciado!", "🚀"),
    *create_bullet_list(["Item 1", "Item 2", "Item 3"]),
    create_code_block("print('Hello')", "python")
]

append_blocks(PAGE_ID, blocks)
```

### Automatizar Geração Diária

```python
import schedule
import time
from groq_notion_basic import generate_content_with_groq, send_to_notion

def daily_summary():
    prompt = "Resuma as tendências de tech de hoje"
    content = generate_content_with_groq(prompt)
    send_to_notion(content)

schedule.every().day.at("09:00").do(daily_summary)

while True:
    schedule.run_pending()
    time.sleep(60)
```

## 🔧 Personalização

### Trocar Modelo LLM

```python
# Groq
content = generate_content_with_groq(
    prompt,
    model="llama-3.1-8b-instant"  # Mais rápido
)

# Gemini
content = generate_content_with_gemini(
    prompt,
    model_name="gemini-1.5-pro"  # Mais poderoso
)
```

### Ajustar Temperatura

Edite nos scripts:

```python
# Mais criativo (0.7-1.0)
temperature=0.9

# Mais determinístico (0.1-0.5)
temperature=0.2
```

### Customizar Formatação

Modifique a função `parse_markdown_to_notion_blocks()` para:
- Adicionar mais tipos de blocos
- Customizar estilos
- Processar formatos específicos

## 📚 Funções Úteis (notion_helpers.py)

### Criação de Blocos

```python
create_heading(text, level=2)
create_paragraph(text)
create_bullet_list(items)
create_numbered_list(items)
create_code_block(code, language="python")
create_quote(text)
create_callout(text, icon="💡")
create_divider()
create_toggle(title, children_blocks)
create_bookmark(url, caption="")
```

### Templates Prontos

```python
create_daily_note(parent_id, content_blocks=None)
create_meeting_notes(parent_id, title, attendees, topics, actions)
create_article_summary(parent_id, title, url, points, quotes)
create_learning_resource(parent_id, topic, resources, concepts)
```

### Database Operations

```python
create_database_page(database_id, properties)
query_database(database_id, filter=None, sorts=None)
update_database_page(page_id, properties)
```

## 🐛 Troubleshooting

### Erro: "Module not found"
```bash
pip install -r requirements.txt
```

### Erro: "Invalid API key"
- Verifique se a key está correta no `.env`
- Confirme que não há espaços antes/depois

### Erro: "Notion object_not_found"
- Confirme que o page_id está correto
- Verifique se a integração está conectada à página

### Erro: "Rate limit exceeded"
- Adicione `time.sleep(0.5)` entre requests
- Use menos tokens por requisição

### Conteúdo aparece sem formatação
- Verifique se está usando Markdown correto
- Teste a função `parse_markdown_to_notion_blocks()`

## 📊 Rate Limits

### Groq (Gratuito)
- 30 requests/minuto
- 6,000 tokens/minuto

### Gemini (Gratuito)
- Flash: 15 requests/minuto
- Pro: 2 requests/minuto

### Notion
- 3 requests/segundo
- Scripts já implementam rate limiting

## 🎯 Próximos Passos

1. ✅ Teste os scripts básicos
2. 📝 Customize os prompts para seu uso
3. 🔄 Configure automações com cron/schedule
4. 🎨 Crie seus próprios templates
5. 🚀 Compartilhe suas melhorias!

## 📞 Suporte

Problemas? Verifique:
- ✅ Variáveis de ambiente configuradas?
- ✅ Dependências instaladas?
- ✅ API keys válidas?
- ✅ Integração conectada no Notion?

---

**Happy Coding! 🚀**
