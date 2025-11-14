# 📝 Template: Resumo de Artigos com IA

## Objetivo
Automatizar o resumo de artigos salvos no Notion usando IA.

## Workflow

```
[Artigo Salvo] → [IA Processa] → [Resumo no Notion]
```

## Configuração

### Opção 1: Com Make.com (Visual)

**Módulos:**
```
1. Notion: Watch Database Items
   - Database: "Artigos para Ler"
   - Filter: Status = "Novo"

2. HTTP Request: Get Article Content
   - URL: {{1.properties.URL.url}}
   - Method: GET

3. HTTP Request: Groq AI
   - URL: https://api.groq.com/openai/v1/chat/completions
   - Method: POST
   - Body: {
       "model": "llama-3.1-70b-versatile",
       "messages": [{
         "role": "user",
         "content": "Resuma este artigo em 3 parágrafos:\n\n{{2.data}}"
       }]
     }

4. Notion: Update Database Item
   - Page ID: {{1.id}}
   - Properties:
     - Resumo: {{3.choices[0].message.content}}
     - Status: "Resumido"
     - Data Resumo: {{now}}
```

### Opção 2: Com Python Script

```python
from groq import Groq
from notion_client import Client
import os

groq = Groq(api_key=os.getenv("GROQ_API_KEY"))
notion = Client(auth=os.getenv("NOTION_TOKEN"))

DATABASE_ID = "SEU_DATABASE_ID"

def summarize_articles():
    """
    Processa artigos com status "Novo"
    """
    # Buscar artigos novos
    results = notion.databases.query(
        database_id=DATABASE_ID,
        filter={
            "property": "Status",
            "select": {
                "equals": "Novo"
            }
        }
    )
    
    for page in results["results"]:
        # Obter URL do artigo
        url = page["properties"]["URL"]["url"]
        title = page["properties"]["Nome"]["title"][0]["text"]["content"]
        
        # Buscar conteúdo (simplificado - usar requests + BeautifulSoup na prática)
        # article_content = fetch_article_content(url)
        
        # Resumir com IA
        prompt = f"Resuma este artigo em 3 parágrafos: {title}"
        
        response = groq.chat.completions.create(
            model="llama-3.1-70b-versatile",
            messages=[{"role": "user", "content": prompt}]
        )
        
        summary = response.choices[0].message.content
        
        # Atualizar no Notion
        notion.pages.update(
            page_id=page["id"],
            properties={
                "Resumo": {
                    "rich_text": [{"text": {"content": summary}}]
                },
                "Status": {
                    "select": {"name": "Resumido"}
                }
            }
        )
        
        print(f"✅ Resumido: {title}")

# Executar
summarize_articles()
```

## Estrutura do Database Notion

### Propriedades Necessárias:

| Nome | Tipo | Descrição |
|------|------|-----------|
| Nome | Title | Título do artigo |
| URL | URL | Link do artigo |
| Status | Select | Novo / Em Leitura / Resumido |
| Resumo | Text | Resumo gerado pela IA |
| Tags | Multi-select | Categorias |
| Data Adicionada | Created time | Auto |
| Data Resumo | Date | Quando foi resumido |

### Views Úteis:

1. **Para Resumir**
   - Filter: Status = "Novo"
   - Sort: Data Adicionada (mais recente)

2. **Resumidos**
   - Filter: Status = "Resumido"
   - Sort: Data Resumo (mais recente)

3. **Por Tag**
   - Group by: Tags

## Prompts Sugeridos

### Resumo Executivo
```
Analise este artigo e forneça:
1. Ideia principal (1 frase)
2. Resumo executivo (3 parágrafos)
3. Principais insights (5 tópicos)
4. Conclusão prática
```

### Resumo Acadêmico
```
Resuma este artigo acadêmico:
1. Objetivo do estudo
2. Metodologia utilizada
3. Principais resultados
4. Conclusões e implicações
5. Limitações mencionadas
```

### Resumo de Notícia
```
Resuma esta notícia:
1. O que aconteceu?
2. Quem está envolvido?
3. Quando e onde?
4. Por que é importante?
5. Qual o impacto esperado?
```

## Melhorias Possíveis

### 1. Extração de Conteúdo
```python
import requests
from bs4 import BeautifulSoup

def fetch_article_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Remover scripts e estilos
    for script in soup(["script", "style"]):
        script.decompose()
    
    # Extrair texto
    text = soup.get_text()
    
    # Limpar
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)
    
    return text[:5000]  # Limitar tamanho
```

### 2. Análise de Sentimento
```python
prompt = f"""
Analise este artigo e forneça:
1. Resumo
2. Sentimento: Positivo/Neutro/Negativo
3. Tom: Informativo/Opinativo/Crítico
4. Público-alvo: Técnico/Geral/Especializado

Artigo: {content}
"""
```

### 3. Geração de Tags Automática
```python
prompt = f"""
Leia este artigo e sugira 3-5 tags/categorias relevantes.
Retorne apenas as tags separadas por vírgula.

Artigo: {content}
"""

tags_text = generate_with_ai(prompt)
tags_list = [tag.strip() for tag in tags_text.split(',')]

# Atualizar no Notion
notion.pages.update(
    page_id=page_id,
    properties={
        "Tags": {
            "multi_select": [{"name": tag} for tag in tags_list]
        }
    }
)
```

### 4. Agendamento Automático
```python
import schedule
import time

def auto_summarize():
    print("🔄 Processando artigos...")
    summarize_articles()
    print("✅ Concluído!")

# Executar a cada hora
schedule.every().hour.do(auto_summarize)

# Ou uma vez por dia às 9h
schedule.every().day.at("09:00").do(auto_summarize)

while True:
    schedule.run_pending()
    time.sleep(60)
```

## Custos Estimados

### Usando Groq (Gratuito)
- ✅ **Custo: $0/mês**
- Limite: 30 requests/min
- Suficiente para: ~1000 artigos/dia

### Usando GPT-3.5-turbo
- 💰 **Custo: ~$0.50/mês**
- Para: 100 artigos/mês
- Resumos de ~500 tokens cada

### Usando Gemini (Gratuito)
- ✅ **Custo: $0/mês**
- Limite: 15 requests/min
- Suficiente para: ~600 artigos/dia

## Exemplos de Saída

### Input
```
URL: https://example.com/article-about-ai
Título: "The Future of AI in 2024"
```

### Output
```
Resumo:
O artigo explora as principais tendências de IA para 2024, focando em 
três áreas principais: IA generativa, automação empresarial e ética em IA.

O autor argumenta que veremos uma democratização maior das ferramentas de 
IA, tornando-as acessíveis para empresas de todos os tamanhos. Especial 
atenção é dada aos modelos open source e plataformas no-code.

Concluindo, o artigo sugere que 2024 será um ano de consolidação e 
aplicação prática, em vez de descobertas revolucionárias.

Tags: IA, Tendências, 2024, Tecnologia, Automação
Status: Resumido
```

## Troubleshooting

### Problema: Resumo muito longo
**Solução:** Ajustar prompt
```python
prompt = "Resuma em EXATAMENTE 3 parágrafos curtos (máximo 300 palavras total)"
```

### Problema: Conteúdo do site não carrega
**Solução:** Usar biblioteca especializada
```python
pip install newspaper3k
from newspaper import Article

def fetch_article(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.text
```

### Problema: Rate limit atingido
**Solução:** Adicionar delays
```python
import time

for page in results["results"]:
    # ... processar ...
    time.sleep(2)  # 2 segundos entre artigos
```

## Próximos Passos

1. ✅ Configure o database no Notion
2. 📝 Escolha método (Make.com ou Python)
3. 🔧 Customize os prompts
4. ⚡ Teste com alguns artigos
5. 🚀 Automatize completamente

---

**Template criado para maximizar produtividade com IA + Notion**
