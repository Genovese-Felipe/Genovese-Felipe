# 🔧 Setup da Notion API

## Passo 1: Criar Integração no Notion

### 1.1 Acessar o Portal de Desenvolvedores

1. Vá para: https://www.notion.so/my-integrations
2. Clique em **"+ New integration"**
3. Escolha o workspace onde quer usar a integração

### 1.2 Configurar a Integração

```
Nome: "Minha IA External"
Logo: (opcional)
Associated workspace: [Seu workspace]

Capabilities (Capacidades):
✅ Read content
✅ Update content  
✅ Insert content
✅ Read comments (opcional)
✅ Insert comments (opcional)

User Information:
□ No user information (recomendado para começar)
```

### 1.3 Obter o Token de Integração

Após criar, você receberá um **Integration Token** que começa com `secret_`

```
Exemplo: secret_AbCd123456789XyZ...
```

⚠️ **IMPORTANTE**: 
- Guarde este token em local seguro
- Nunca compartilhe ou comite em repositórios públicos
- Trate como uma senha

---

## Passo 2: Conectar a Integração às Páginas

### 2.1 Adicionar Integração a uma Página

1. Abra a página do Notion que deseja automatizar
2. Clique nos três pontos (`...`) no canto superior direito
3. Vá em **"Connections"** ou **"Add connections"**
4. Selecione sua integração "Minha IA External"

⚠️ A integração só pode acessar páginas que você explicitamente compartilhar com ela.

### 2.2 Obter o ID da Página

**Método 1 - Pela URL:**
```
URL: https://www.notion.so/Minha-Pagina-123abc456def789
Page ID: 123abc456def789
```

**Método 2 - Copiar Link:**
1. Clique em "Share" na página
2. Copie o link
3. O ID é a última parte da URL (32 caracteres hexadecimais)

**Formato do Page ID:**
```
Original: 123abc456def789012345678901234567
Formatado: 123abc45-6def-7890-1234-567890123456
```

---

## Passo 3: Testar a Conexão

### 3.1 Teste Rápido com cURL

```bash
curl -X GET https://api.notion.com/v1/pages/YOUR_PAGE_ID \
  -H "Authorization: Bearer YOUR_INTEGRATION_TOKEN" \
  -H "Notion-Version: 2022-06-28"
```

**Resposta esperada:**
```json
{
  "object": "page",
  "id": "123abc45-6def-7890-1234-567890123456",
  "created_time": "2024-01-01T00:00:00.000Z",
  "properties": { ... }
}
```

### 3.2 Teste com Python

```python
import requests

NOTION_TOKEN = "secret_YOUR_TOKEN_HERE"
PAGE_ID = "YOUR_PAGE_ID_HERE"

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json"
}

response = requests.get(
    f"https://api.notion.com/v1/pages/{PAGE_ID}",
    headers=headers
)

print(response.status_code)  # Deve retornar 200
print(response.json())
```

---

## Passo 4: Configurar Databases (Opcional)

### 4.1 Criar Database no Notion

1. Crie uma nova página
2. Digite `/database` e escolha "Table - Inline"
3. Configure as colunas desejadas

### 4.2 Obter Database ID

Similar ao Page ID:
```
URL: https://www.notion.so/123abc456def?v=789...
Database ID: 123abc456def (parte antes do ?)
```

### 4.3 Compartilhar Database com Integração

Mesmo processo da página:
1. Abra o database
2. Três pontos > "Add connections"
3. Selecione sua integração

---

## Passo 5: Boas Práticas de Segurança

### 5.1 Armazenar Credenciais com Segurança

**Opção 1 - Variáveis de Ambiente:**
```bash
# Linux/Mac - adicione ao ~/.bashrc ou ~/.zshrc
export NOTION_TOKEN="secret_YOUR_TOKEN"
export NOTION_PAGE_ID="YOUR_PAGE_ID"
```

```bash
# Windows - PowerShell
$env:NOTION_TOKEN = "secret_YOUR_TOKEN"
$env:NOTION_PAGE_ID = "YOUR_PAGE_ID"
```

**Opção 2 - Arquivo .env (Recomendado):**
```bash
# .env
NOTION_TOKEN=secret_YOUR_TOKEN
NOTION_PAGE_ID=YOUR_PAGE_ID
```

```python
# Python com python-dotenv
from dotenv import load_dotenv
import os

load_dotenv()
NOTION_TOKEN = os.getenv("NOTION_TOKEN")
```

**Opção 3 - Gerenciador de Senhas:**
Use 1Password, Bitwarden, ou similar para armazenar tokens

### 5.2 Gitignore

Se usar repositório Git, adicione ao `.gitignore`:
```
.env
*.env
secrets/
config/secrets.json
```

---

## Passo 6: Instalar Bibliotecas

### Python

```bash
# Biblioteca oficial do Notion
pip install notion-client

# Para requisições HTTP diretas
pip install requests python-dotenv
```

### Node.js

```bash
# SDK oficial do Notion
npm install @notionhq/client

# Para variáveis de ambiente
npm install dotenv
```

---

## Estrutura de Projeto Recomendada

```
meu-projeto-notion/
├── .env                    # Credenciais (NÃO commitar)
├── .gitignore             # Ignorar .env
├── config.py              # Configurações
├── notion_client.py       # Cliente Notion
├── ai_integrations/       # Integrações com IAs
│   ├── gpt_integration.py
│   ├── gemini_integration.py
│   └── perplexity_integration.py
└── workflows/             # Automações específicas
    ├── summarize_article.py
    └── generate_content.py
```

---

## Exemplo Completo - Hello World

```python
from notion_client import Client

# Inicializar cliente
notion = Client(auth="secret_YOUR_TOKEN")

# Criar uma página simples
new_page = notion.pages.create(
    parent={"page_id": "YOUR_PARENT_PAGE_ID"},
    properties={
        "title": {
            "title": [
                {
                    "text": {
                        "content": "Minha Primeira Página via API"
                    }
                }
            ]
        }
    },
    children=[
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [
                    {
                        "text": {
                            "content": "Esta página foi criada pela API do Notion! 🎉"
                        }
                    }
                ]
            }
        }
    ]
)

print(f"Página criada: {new_page['url']}")
```

---

## Troubleshooting

### Erro: "unauthorized"
- ✓ Verifique se o token está correto
- ✓ Confirme que a integração está conectada à página/database

### Erro: "object_not_found"
- ✓ Verifique se o page_id está correto
- ✓ Confirme que a página foi compartilhada com a integração

### Erro: "validation_error"
- ✓ Verifique a estrutura do JSON enviado
- ✓ Consulte a documentação para o formato correto

### Erro: "rate_limited"
- ✓ Você excedeu o rate limit (3 requests/segundo)
- ✓ Adicione delays entre requisições

---

## Rate Limits

```
Rate Limit: 3 requests por segundo
```

**Implementar rate limiting:**

```python
import time

def call_notion_api_safely(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        time.sleep(0.34)  # ~3 requests/segundo
        return result
    return wrapper
```

---

## Recursos Adicionais

- 📖 **Documentação Oficial**: https://developers.notion.com/
- 🔧 **API Reference**: https://developers.notion.com/reference/intro
- 💬 **Community**: https://developers.notion.com/community
- 🎓 **Tutoriais**: https://developers.notion.com/docs/getting-started

---

## Próximo Passo

Agora que você configurou a Notion API, escolha como integrar sua IA preferida:
- → **[ChatGPT/GPT Plus](02-Integracao-ChatGPT.md)**
- → **[Gemini Pro](03-Integracao-Gemini.md)**
- → **[Perplexity Pro](04-Integracao-Perplexity.md)**
