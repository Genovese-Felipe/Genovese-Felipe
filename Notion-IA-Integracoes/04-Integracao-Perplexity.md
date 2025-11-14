# 🔍 Integração Perplexity Pro + Notion

## Visão Geral

Com sua assinatura **Perplexity Pro**, você pode integrar pesquisa avançada com IA ao seu workflow do Notion:

```
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│  Perplexity  │ -> │ Perplexity   │ -> │   Notion     │
│  (Interface) │    │ API/Sharing  │    │   (API)      │
└──────────────┘    └──────────────┘    └──────────────┘
```

---

## Características da Perplexity Pro

✅ **Pesquisa com fontes verificadas**  
✅ **Acesso a GPT-4, Claude 3.5, etc.**  
✅ **Unlimited Pro searches**  
✅ **File uploads e análise**  
✅ **Compartilhamento de threads**  
✅ **API em beta (pAPI)**

---

## Método 1: Perplexity pAPI (Beta)

### 1.1 Obter Acesso à pAPI

**Status atual:**
- ⚠️ A API ainda está em **Beta Privado**
- 🔜 Acesso será expandido gradualmente
- 📧 Inscreva-se na waitlist: https://www.perplexity.ai/hub/developers

**Quando tiver acesso:**

```python
import os
import requests
from notion_client import Client

PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY")
NOTION_TOKEN = os.getenv("NOTION_TOKEN")
NOTION_PAGE_ID = os.getenv("NOTION_PAGE_ID")

def search_with_perplexity(query, model="sonar-pro"):
    """Busca usando Perplexity API"""
    
    url = "https://api.perplexity.ai/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {PERPLEXITY_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": model,  # sonar-pro, sonar-medium, etc.
        "messages": [
            {
                "role": "system",
                "content": "Você é um assistente de pesquisa que fornece respostas precisas com fontes."
            },
            {
                "role": "user",
                "content": query
            }
        ],
        "max_tokens": 2000,
        "temperature": 0.2,
        "top_p": 0.9,
        "return_citations": True,
        "search_domain_filter": ["perplexity.ai"],
        "return_images": False,
        "search_recency_filter": "month"
    }
    
    response = requests.post(url, json=payload, headers=headers)
    result = response.json()
    
    # Extrair resposta e citações
    answer = result['choices'][0]['message']['content']
    citations = result.get('citations', [])
    
    return answer, citations

def format_perplexity_response(answer, citations):
    """Formata resposta com citações para Notion"""
    
    blocks = []
    
    # Adicionar resposta
    for paragraph in answer.split('\n\n'):
        if paragraph.strip():
            blocks.append({
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [{"text": {"content": paragraph}}]
                }
            })
    
    # Adicionar citações
    if citations:
        blocks.append({
            "object": "block",
            "type": "heading_3",
            "heading_3": {
                "rich_text": [{"text": {"content": "Fontes:"}}]
            }
        })
        
        for i, citation in enumerate(citations, 1):
            blocks.append({
                "object": "block",
                "type": "bulleted_list_item",
                "bulleted_list_item": {
                    "rich_text": [
                        {
                            "text": {
                                "content": f"[{i}] ",
                            }
                        },
                        {
                            "text": {
                                "content": citation.get('title', 'Source'),
                                "link": {"url": citation.get('url', '#')}
                            }
                        }
                    ]
                }
            })
    
    return blocks

def send_research_to_notion(query):
    """Pesquisa com Perplexity e envia para Notion"""
    
    print(f"🔍 Pesquisando: {query}")
    answer, citations = search_with_perplexity(query)
    
    notion = Client(auth=NOTION_TOKEN)
    blocks = format_perplexity_response(answer, citations)
    
    # Adicionar título da pesquisa
    blocks.insert(0, {
        "object": "block",
        "type": "heading_2",
        "heading_2": {
            "rich_text": [{"text": {"content": f"Pesquisa: {query}"}}]
        }
    })
    
    notion.blocks.children.append(
        block_id=NOTION_PAGE_ID,
        children=blocks
    )
    
    return "✅ Pesquisa adicionada ao Notion!"

# Exemplo de uso
if __name__ == "__main__":
    query = "Quais são as últimas tendências em IA generativa para 2024?"
    result = send_research_to_notion(query)
    print(result)
```

---

## Método 2: Usando Interface Web + Compartilhamento

### 2.1 Workflow Manual Otimizado

**Passo a Passo:**

1. **Pesquisar no Perplexity:**
   - Faça sua pergunta em https://www.perplexity.ai/
   - Use Pro mode para melhores resultados
   - Ajuste configurações (focus, modelo, etc.)

2. **Compartilhar Thread:**
   - Clique em "Share" na thread
   - Copie o link público
   - Ou copie o conteúdo diretamente

3. **Enviar para Notion:**
   
   **Opção A - Via Web Clipper:**
   - Use Notion Web Clipper extension
   - Clique no ícone e salve no Notion
   
   **Opção B - Via Copy/Paste:**
   - Selecione todo o conteúdo
   - Cole no Notion (mantém formatação)
   
   **Opção C - Via API com link:**
   ```python
   def add_perplexity_thread_to_notion(thread_url, title):
       notion = Client(auth=NOTION_TOKEN)
       
       blocks = [
           {
               "object": "block",
               "type": "bookmark",
               "bookmark": {
                   "url": thread_url,
                   "caption": [{"text": {"content": title}}]
               }
           }
       ]
       
       notion.blocks.children.append(
           block_id=NOTION_PAGE_ID,
           children=blocks
       )
   ```

### 2.2 Extensão de Browser Customizada

**Criar Bookmarklet para automação:**

```javascript
javascript:(function(){
  var content = document.querySelector('.thread-content').innerText;
  var sources = Array.from(document.querySelectorAll('.citation')).map(c => c.href);
  
  // Enviar para servidor intermediário que comunica com Notion
  fetch('YOUR_SERVER/perplexity-to-notion', {
    method: 'POST',
    body: JSON.stringify({content, sources}),
    headers: {'Content-Type': 'application/json'}
  });
})();
```

---

## Método 3: Via OpenRouter + Perplexity Models

### 3.1 Usar OpenRouter como Proxy

**OpenRouter** (https://openrouter.ai/) oferece acesso a modelos Perplexity:

```python
import os
import requests
from notion_client import Client

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def search_with_openrouter(query):
    """Usa Perplexity via OpenRouter"""
    
    url = "https://openrouter.ai/api/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://your-site.com",
        "X-Title": "Notion Integration"
    }
    
    payload = {
        "model": "perplexity/llama-3.1-sonar-large-128k-online",
        "messages": [
            {
                "role": "user",
                "content": query
            }
        ]
    }
    
    response = requests.post(url, json=payload, headers=headers)
    result = response.json()
    
    return result['choices'][0]['message']['content']

# Uso similar aos outros métodos
```

**Modelos Disponíveis via OpenRouter:**
- `perplexity/llama-3.1-sonar-small-128k-online`
- `perplexity/llama-3.1-sonar-large-128k-online`
- `perplexity/llama-3.1-sonar-huge-128k-online`

---

## Método 4: Automação com Make.com/Zapier

### 4.1 Via Make.com

**Cenário:**
```
Webhook → HTTP Request (Perplexity API) → Notion
```

**Configuração:**

1. **Trigger:** Webhook (você envia query via POST)
2. **Action 1:** HTTP Request para Perplexity API
3. **Action 2:** Parse response
4. **Action 3:** Create page in Notion

### 4.2 Via Zapier

**Não há integração nativa Perplexity no Zapier ainda**, mas você pode:

1. Usar "Webhooks by Zapier"
2. Configurar custom API call
3. Conectar com Notion

---

## Método 5: Python Script com Selenium

### 5.1 Automatizar Interface Web

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from notion_client import Client
import time

def automate_perplexity_search(query):
    """Automatiza busca no Perplexity Web"""
    
    # Configurar WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    
    try:
        # Abrir Perplexity
        driver.get('https://www.perplexity.ai/')
        time.sleep(2)
        
        # Encontrar input e digitar query
        search_box = driver.find_element(By.CSS_SELECTOR, 'textarea')
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)
        
        # Aguardar resposta
        time.sleep(10)  # Ajustar conforme necessário
        
        # Extrair conteúdo
        answer = driver.find_element(By.CLASS_NAME, 'answer-text').text
        
        # Extrair fontes
        sources = []
        source_elements = driver.find_elements(By.CLASS_NAME, 'citation')
        for source in source_elements:
            sources.append({
                'title': source.text,
                'url': source.get_attribute('href')
            })
        
        return answer, sources
        
    finally:
        driver.quit()

def automated_research_to_notion(query):
    """Automação completa: Perplexity -> Notion"""
    
    # Buscar no Perplexity
    answer, sources = automate_perplexity_search(query)
    
    # Preparar blocos para Notion
    notion = Client(auth=NOTION_TOKEN)
    blocks = []
    
    # Título
    blocks.append({
        "object": "block",
        "type": "heading_2",
        "heading_2": {
            "rich_text": [{"text": {"content": f"📊 Pesquisa: {query}"}}]
        }
    })
    
    # Resposta
    blocks.append({
        "object": "block",
        "type": "paragraph",
        "paragraph": {
            "rich_text": [{"text": {"content": answer}}]
        }
    })
    
    # Fontes
    if sources:
        blocks.append({
            "object": "block",
            "type": "heading_3",
            "heading_3": {
                "rich_text": [{"text": {"content": "🔗 Fontes:"}}]
            }
        })
        
        for source in sources:
            blocks.append({
                "object": "block",
                "type": "bulleted_list_item",
                "bulleted_list_item": {
                    "rich_text": [
                        {
                            "text": {
                                "content": source['title'],
                                "link": {"url": source['url']}
                            }
                        }
                    ]
                }
            })
    
    # Enviar para Notion
    notion.blocks.children.append(
        block_id=NOTION_PAGE_ID,
        children=blocks
    )
    
    return "✅ Pesquisa automatizada enviada ao Notion!"

# Instalação: pip install selenium
```

---

## Use Cases Práticos

### 1. Daily Research Digest

```python
def create_daily_digest():
    """Cria digest diário de pesquisas"""
    
    topics = [
        "Últimas notícias em IA",
        "Tendências de tecnologia",
        "Atualizações de mercado"
    ]
    
    for topic in topics:
        send_research_to_notion(topic)
        time.sleep(5)  # Rate limiting
    
    return "✅ Digest diário criado!"
```

### 2. Competitive Analysis

```python
def competitive_research(competitors):
    """Pesquisa sobre competidores"""
    
    for competitor in competitors:
        query = f"Últimas notícias e atualizações sobre {competitor}"
        send_research_to_notion(query)
        time.sleep(5)
```

### 3. Market Research

```python
def market_research(market, aspects):
    """Pesquisa de mercado estruturada"""
    
    for aspect in aspects:
        query = f"{market}: {aspect}"
        send_research_to_notion(query)
```

### 4. Learning Assistant

```python
def create_study_guide(topic):
    """Cria guia de estudos com Perplexity"""
    
    queries = [
        f"Explique {topic} para iniciantes",
        f"Conceitos avançados de {topic}",
        f"Exemplos práticos de {topic}",
        f"Recursos para aprender {topic}"
    ]
    
    for query in queries:
        send_research_to_notion(query)
        time.sleep(5)
```

---

## Comparação de Métodos

| Método | Dificuldade | Custo | Automação | Fontes |
|--------|-------------|-------|-----------|--------|
| **pAPI (quando disponível)** | ⭐⭐ | 💰 | ⚡⚡⚡ | ✅ |
| **Web + Manual** | ⭐ | ✅ Grátis | ❌ | ✅ |
| **OpenRouter** | ⭐⭐ | 💰 | ⚡⚡⚡ | ⚠️ |
| **Selenium** | ⭐⭐⭐ | ✅ Grátis | ⚡⚡ | ✅ |
| **Make.com** | ⭐⭐ | ✅/💰 | ⚡⚡⚡ | ✅ |

---

## Alternativas Enquanto pAPI não está disponível

### 1. You.com API

```python
# You.com oferece API similar ao Perplexity
import requests

def search_with_you(query):
    url = "https://api.you.com/search"
    headers = {"X-API-Key": YOU_API_KEY}
    params = {"query": query}
    
    response = requests.get(url, headers=headers, params=params)
    return response.json()
```

### 2. Brave Search API

```python
# Brave Search também oferece API
def search_with_brave(query):
    url = "https://api.search.brave.com/res/v1/web/search"
    headers = {
        "Accept": "application/json",
        "X-Subscription-Token": BRAVE_API_KEY
    }
    params = {"q": query}
    
    response = requests.get(url, headers=headers, params=params)
    return response.json()
```

### 3. SerpAPI (Google Search)

```python
# SerpAPI para buscar no Google
from serpapi import GoogleSearch

def search_with_serpapi(query):
    params = {
        "q": query,
        "api_key": SERPAPI_KEY
    }
    
    search = GoogleSearch(params)
    results = search.get_dict()
    return results
```

---

## Workflow Recomendado (Atual)

### Para Uso Diário:

1. **Faça pesquisas no Perplexity Pro**
2. **Use compartilhamento de threads**
3. **Adicione ao Notion via:**
   - Web Clipper (mais rápido)
   - Copy/Paste (manual mas simples)
   - Bookmark do thread (mantém atualizado)

### Para Automação:

1. **Enquanto pAPI não disponível:**
   - Use OpenRouter + modelos Perplexity
   - Ou use Selenium para automação web
   
2. **Quando pAPI disponível:**
   - Migre para pAPI oficial
   - Melhor performance e confiabilidade

---

## Recursos e Referências

- 🌐 **Perplexity**: https://www.perplexity.ai/
- 📧 **API Waitlist**: https://www.perplexity.ai/hub/developers
- 🔧 **OpenRouter**: https://openrouter.ai/
- 📖 **Notion API**: https://developers.notion.com/

---

## Próximos Passos

- → **[Soluções Open Source](05-Solucoes-Open-Source.md)**
- → **[Automações No-Code](06-Automacoes-Zapier-Make.md)**
- → **[Scripts de Exemplo](07-Scripts-Exemplos/)**

---

## Nota Final

💡 **Perplexity Pro** é excelente para pesquisa com fontes verificadas. Enquanto a API oficial não está disponível, use:
- Interface web + compartilhamento (mais simples)
- OpenRouter (para automação)
- Selenium (para casos específicos)
