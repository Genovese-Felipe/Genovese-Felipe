# 🔓 Soluções Open Source para Notion + IA

## Visão Geral

Alternativas gratuitas e open source para integrar IA com Notion, sem depender de serviços pagos:

```
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│ LLM Open     │ -> │ Self-Hosted  │ -> │   Notion     │
│ Source       │    │ ou Free API  │    │   (API)      │
└──────────────┘    └──────────────┘    └──────────────┘
```

---

## 🌟 Opções Gratuitas de LLMs

### 1. Groq (⭐ Mais Recomendado)

**Por que Groq é incrível:**
- ✅ **Completamente gratuito** (sem cartão de crédito)
- ✅ **Extremamente rápido** (tokens/segundo)
- ✅ **Modelos de qualidade**: LLaMA 3.1, Mixtral, Gemma
- ✅ **Rate limits generosos**: 30 req/min
- ✅ **API simples** (compatível com OpenAI)

**Setup:**

```python
import os
from groq import Groq
from notion_client import Client

GROQ_API_KEY = os.getenv("GROQ_API_KEY")  # Grátis em console.groq.com
NOTION_TOKEN = os.getenv("NOTION_TOKEN")
NOTION_PAGE_ID = os.getenv("NOTION_PAGE_ID")

groq_client = Groq(api_key=GROQ_API_KEY)
notion = Client(auth=NOTION_TOKEN)

def generate_with_groq(prompt, model="llama-3.1-70b-versatile"):
    """Gera conteúdo com Groq (GRÁTIS!)"""
    
    chat_completion = groq_client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "Você cria conteúdo estruturado em Markdown para Notion."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        model=model,
        temperature=0.7,
        max_tokens=8000,
        top_p=1,
        stream=False
    )
    
    return chat_completion.choices[0].message.content

def send_to_notion(content):
    """Envia para Notion"""
    blocks = []
    
    for paragraph in content.split('\n\n'):
        if paragraph.strip():
            blocks.append({
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [{"text": {"content": paragraph}}]
                }
            })
    
    notion.blocks.children.append(
        block_id=NOTION_PAGE_ID,
        children=blocks
    )

# Uso
prompt = "Crie um guia sobre produtividade com IA"
content = generate_with_groq(prompt)
send_to_notion(content)
```

**Instalação:**
```bash
pip install groq notion-client python-dotenv
```

**Obter API Key:**
1. Vá para: https://console.groq.com/
2. Crie conta (grátis, sem cartão)
3. Vá em "API Keys"
4. Crie uma nova key

**Modelos Disponíveis (Gratuitos):**
- `llama-3.1-70b-versatile` - Melhor para tarefas gerais
- `llama-3.1-8b-instant` - Mais rápido
- `mixtral-8x7b-32768` - Grande contexto
- `gemma2-9b-it` - Google Gemma

---

### 2. Hugging Face Inference API

**Características:**
- ✅ Gratuito com rate limits
- ✅ Centenas de modelos disponíveis
- ✅ Sem necessidade de GPU própria

```python
import requests

HF_API_KEY = os.getenv("HF_API_KEY")  # Grátis em huggingface.co

def generate_with_huggingface(prompt, model="meta-llama/Meta-Llama-3-8B-Instruct"):
    """Usa Hugging Face Inference API"""
    
    API_URL = f"https://api-inference.huggingface.co/models/{model}"
    
    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 2000,
            "temperature": 0.7,
            "top_p": 0.95
        }
    }
    
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()[0]['generated_text']

# Uso
content = generate_with_huggingface("Crie um artigo sobre IA")
send_to_notion(content)
```

**Obter Token:**
1. Criar conta em: https://huggingface.co/
2. Settings → Access Tokens
3. Create new token

---

### 3. Ollama (Self-Hosted)

**Para rodar localmente:**

```bash
# Instalar Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Baixar modelo
ollama pull llama3.1

# Rodar modelo
ollama serve
```

**Python Integration:**

```python
import requests

def generate_with_ollama(prompt, model="llama3.1"):
    """Usa Ollama local"""
    
    url = "http://localhost:11434/api/generate"
    
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    
    response = requests.post(url, json=payload)
    return response.json()['response']

# Uso
content = generate_with_ollama("Crie um tutorial de Python")
send_to_notion(content)
```

**Vantagens:**
- ✅ 100% gratuito
- ✅ Privacidade total
- ✅ Sem rate limits
- ✅ Offline

**Desvantagens:**
- ⚠️ Requer hardware (RAM/GPU)
- ⚠️ Setup mais complexo

---

### 4. Together AI

**Free Tier Generoso:**

```python
import together

together.api_key = os.getenv("TOGETHER_API_KEY")

def generate_with_together(prompt):
    """Usa Together AI (plano gratuito disponível)"""
    
    response = together.Complete.create(
        prompt=prompt,
        model="meta-llama/Llama-3-70b-chat-hf",
        max_tokens=2000,
        temperature=0.7
    )
    
    return response['output']['choices'][0]['text']
```

---

## 🤖 Plataformas de Automação Open Source

### 1. n8n (⭐ Altamente Recomendado)

**O que é:**
- Ferramenta de automação visual (alternativa ao Zapier)
- 100% open source e gratuita
- Self-hosted ou cloud

**Setup:**

```bash
# Via Docker
docker run -it --rm \
  --name n8n \
  -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n \
  n8nio/n8n

# Ou via npm
npm install n8n -g
n8n start
```

**Criar Workflow n8n para Notion:**

1. **Trigger:** Webhook ou Cron
2. **HTTP Request:** Chamar Groq/HuggingFace API
3. **Function:** Processar resposta
4. **Notion Node:** Criar/atualizar página

**Exemplo de Workflow JSON:**

```json
{
  "nodes": [
    {
      "name": "Cron",
      "type": "n8n-nodes-base.cron",
      "parameters": {
        "triggerTimes": {
          "item": [
            {
              "hour": 9,
              "minute": 0
            }
          ]
        }
      }
    },
    {
      "name": "Groq API",
      "type": "n8n-nodes-base.httpRequest",
      "parameters": {
        "url": "https://api.groq.com/openai/v1/chat/completions",
        "method": "POST",
        "jsonParameters": true,
        "options": {},
        "bodyParametersJson": "{\n  \"model\": \"llama-3.1-70b-versatile\",\n  \"messages\": [\n    {\n      \"role\": \"user\",\n      \"content\": \"Crie um resumo diário de tecnologia\"\n    }\n  ]\n}"
      }
    },
    {
      "name": "Notion",
      "type": "n8n-nodes-base.notion",
      "parameters": {
        "resource": "page",
        "operation": "create",
        "pageId": "YOUR_PAGE_ID"
      }
    }
  ],
  "connections": {
    "Cron": {
      "main": [[{ "node": "Groq API" }]]
    },
    "Groq API": {
      "main": [[{ "node": "Notion" }]]
    }
  }
}
```

**Recursos:**
- 📖 Docs: https://docs.n8n.io/
- 🎓 Templates: https://n8n.io/workflows/

---

### 2. Activepieces

**Similar ao n8n, mas com foco em facilidade:**

```bash
# Via Docker
docker run -p 8080:80 activepieces/activepieces
```

**Features:**
- Interface mais simples que n8n
- Integração nativa com Notion
- Templates prontos

---

### 3. Pipedream

**Free Tier:**
- 333 credits/mês gratuitos
- Serverless (não precisa hospedar)

```javascript
// Pipedream Workflow
export default defineComponent({
  async run({ steps, $ }) {
    // 1. Gerar conteúdo com Groq
    const groqResponse = await axios.post(
      'https://api.groq.com/openai/v1/chat/completions',
      {
        model: 'llama-3.1-70b-versatile',
        messages: [{ role: 'user', content: 'Crie conteúdo' }]
      },
      {
        headers: { 'Authorization': `Bearer ${process.env.GROQ_API_KEY}` }
      }
    );
    
    // 2. Enviar para Notion
    await axios.patch(
      `https://api.notion.com/v1/blocks/${process.env.NOTION_PAGE_ID}/children`,
      {
        children: [
          {
            object: 'block',
            type: 'paragraph',
            paragraph: {
              rich_text: [{
                text: { content: groqResponse.data.choices[0].message.content }
              }]
            }
          }
        ]
      },
      {
        headers: {
          'Authorization': `Bearer ${process.env.NOTION_TOKEN}`,
          'Notion-Version': '2022-06-28'
        }
      }
    );
  }
});
```

---

## 📦 Ferramentas e Bibliotecas

### 1. LangChain (Open Source)

**Framework para LLM applications:**

```python
from langchain_groq import ChatGroq
from langchain_community.document_loaders import NotionDBLoader
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Setup
llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name="llama-3.1-70b-versatile"
)

# Template
template = """
Crie conteúdo estruturado sobre: {topic}

Formato: Markdown
Seções: 3-5
Estilo: Profissional e informativo
"""

prompt = PromptTemplate(template=template, input_variables=["topic"])
chain = LLMChain(llm=llm, prompt=prompt)

# Gerar e enviar para Notion
content = chain.run(topic="IA no trabalho")
send_to_notion(content)
```

**Instalação:**
```bash
pip install langchain langchain-groq
```

---

### 2. LlamaIndex (Open Source)

**Para RAG (Retrieval-Augmented Generation):**

```python
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.groq import Groq

# Setup LLM
llm = Groq(model="llama-3.1-70b-versatile", api_key=GROQ_API_KEY)

# Carregar documentos
documents = SimpleDirectoryReader("data").load_data()

# Criar índice
index = VectorStoreIndex.from_documents(documents, llm=llm)

# Query
query_engine = index.as_query_engine()
response = query_engine.query("Resuma estes documentos")

# Enviar para Notion
send_to_notion(str(response))
```

---

### 3. AutoGen (Microsoft - Open Source)

**Para agentes autônomos:**

```python
import autogen

config_list = [
    {
        "model": "llama-3.1-70b-versatile",
        "api_key": GROQ_API_KEY,
        "base_url": "https://api.groq.com/openai/v1"
    }
]

# Criar assistente
assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config={"config_list": config_list}
)

# Criar usuário proxy
user_proxy = autogen.UserProxyAgent(
    name="user",
    human_input_mode="NEVER",
    code_execution_config={"work_dir": "coding"}
)

# Iniciar conversa
user_proxy.initiate_chat(
    assistant,
    message="Crie um artigo sobre automação e salve em Markdown"
)
```

---

## 🔧 Projetos Completos Open Source

### 1. Notionize (GitHub)

**Ferramenta open source para Notion:**
- Clone: https://github.com/yourusername/notionize
- Recursos: Templates, automações, integrações

### 2. Notion-AI-Bridge (Exemplo)

```python
# notion_ai_bridge.py
class NotionAIBridge:
    def __init__(self, llm_provider="groq"):
        self.llm_provider = llm_provider
        self.notion = Client(auth=NOTION_TOKEN)
    
    def generate_and_send(self, prompt, page_id):
        # Gerar com LLM escolhido
        if self.llm_provider == "groq":
            content = generate_with_groq(prompt)
        elif self.llm_provider == "ollama":
            content = generate_with_ollama(prompt)
        
        # Enviar para Notion
        self.send_to_notion(content, page_id)
    
    def send_to_notion(self, content, page_id):
        # Implementação...
        pass

# Uso
bridge = NotionAIBridge(llm_provider="groq")
bridge.generate_and_send(
    "Crie um plano de estudos",
    page_id=NOTION_PAGE_ID
)
```

---

## 💰 Comparação de Custos

| Solução | Custo Mensal | Rate Limits | Qualidade |
|---------|--------------|-------------|-----------|
| **Groq** | 💚 $0 | 30 req/min | ⭐⭐⭐⭐ |
| **HuggingFace** | 💚 $0 | 1000 req/dia | ⭐⭐⭐ |
| **Ollama** | 💚 $0 | Ilimitado | ⭐⭐⭐⭐ |
| **Together AI** | 💚 $0* | 60 req/min | ⭐⭐⭐⭐ |
| **n8n** | 💚 $0 | Ilimitado | - |
| **Pipedream** | 💚 $0* | 333 credits | - |

*Free tier disponível

---

## 🎯 Stack Recomendada (100% Gratuita)

### Setup Ideal:

```
┌─────────────────────────────────────────────┐
│  1. Groq (LLM gratuito e rápido)            │
│  2. n8n (Automação open source)             │
│  3. Notion API (Workspace Plus)             │
│  4. Python Scripts (Customização)           │
└─────────────────────────────────────────────┘
```

**Por que:**
- ✅ Custo zero
- ✅ Sem vendor lock-in
- ✅ Máxima flexibilidade
- ✅ Privacidade controlada

---

## 📋 Checklist de Implementação

### Opção 1: Quick Start (1 hora)
- [ ] Criar conta no Groq
- [ ] Obter API key (grátis)
- [ ] Instalar `groq` e `notion-client`
- [ ] Rodar script exemplo
- [ ] Testar geração de conteúdo

### Opção 2: Setup Completo (1 dia)
- [ ] Setup Groq + Notion
- [ ] Instalar n8n via Docker
- [ ] Criar workflows básicos
- [ ] Configurar automações
- [ ] Documentar processos

### Opção 3: Self-Hosted (2-3 dias)
- [ ] Instalar Ollama
- [ ] Baixar modelos LLaMA
- [ ] Setup n8n self-hosted
- [ ] Criar scripts personalizados
- [ ] Configurar backups

---

## 🚀 Exemplos Práticos

### 1. Daily Digest Automático

```python
# daily_digest.py
import schedule
import time

def create_daily_digest():
    topics = [
        "Últimas notícias em tecnologia",
        "Tendências de IA",
        "Dicas de produtividade"
    ]
    
    for topic in topics:
        prompt = f"Resuma em 2 parágrafos: {topic}"
        content = generate_with_groq(prompt)
        send_to_notion(content)
        time.sleep(2)  # Rate limiting

# Agendar para 9h todos os dias
schedule.every().day.at("09:00").do(create_daily_digest)

while True:
    schedule.run_pending()
    time.sleep(60)
```

### 2. Content Generator

```python
def generate_blog_post(topic, tone="professional"):
    prompt = f"""
    Crie um artigo de blog sobre: {topic}
    Tom: {tone}
    
    Estrutura:
    - Introdução cativante
    - 3 seções principais com subtópicos
    - Conclusão com call-to-action
    - Formato: Markdown
    """
    
    content = generate_with_groq(prompt, model="llama-3.1-70b-versatile")
    send_to_notion(content)
    
    return "✅ Artigo criado e enviado ao Notion!"
```

### 3. Research Assistant

```python
def research_and_summarize(topic):
    # 1. Gerar outline
    outline_prompt = f"Crie um outline para pesquisar sobre: {topic}"
    outline = generate_with_groq(outline_prompt)
    
    # 2. Para cada seção, gerar conteúdo
    sections = outline.split('\n')
    full_content = []
    
    for section in sections:
        if section.strip():
            section_prompt = f"Desenvolva em 2 parágrafos: {section}"
            section_content = generate_with_groq(section_prompt)
            full_content.append(section_content)
            time.sleep(2)
    
    # 3. Enviar para Notion
    final_content = '\n\n'.join(full_content)
    send_to_notion(final_content)
```

---

## 🔗 Recursos Adicionais

- 🌐 **Groq**: https://console.groq.com/
- 🤗 **Hugging Face**: https://huggingface.co/
- 🦙 **Ollama**: https://ollama.com/
- 🔧 **n8n**: https://n8n.io/
- 📚 **LangChain**: https://python.langchain.com/
- 🦜 **LlamaIndex**: https://www.llamaindex.ai/

---

## Próximos Passos

- → **[Automações No-Code](06-Automacoes-Zapier-Make.md)**
- → **[Scripts de Exemplo](07-Scripts-Exemplos/)**
- → **[Templates de Workflows](08-Templates-Workflows/)**
