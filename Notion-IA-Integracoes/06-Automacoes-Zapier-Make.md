# 🔄 Automações No-Code: Zapier, Make.com e Alternativas

## Visão Geral

Soluções de automação visual (sem programação) para conectar IA com Notion:

```
┌─────────────┐    ┌──────────────┐    ┌─────────────┐
│  Trigger    │ -> │  No-Code     │ -> │   Notion    │
│  (IA/Tempo) │    │  Platform    │    │   (API)     │
└─────────────┘    └──────────────┘    └─────────────┘
```

---

## 🟦 Make.com (Recomendado)

### Por que Make.com?

✅ **Plano Gratuito**: 1.000 operações/mês  
✅ **Interface Visual**: Drag & drop  
✅ **Integração Notion Nativa**: Fácil de configurar  
✅ **HTTP Modules**: Para qualquer API  
✅ **Agendamento**: Cron jobs visuais

### Setup Inicial

1. **Criar Conta:**
   - Vá para: https://www.make.com/
   - Cadastre-se (plano gratuito)

2. **Conectar Notion:**
   - Em "Connections" → "Add"
   - Escolha "Notion"
   - Autorize seu workspace

3. **Obter API Keys das IAs:**
   - Groq: https://console.groq.com/
   - OpenAI: https://platform.openai.com/
   - Gemini: https://aistudio.google.com/

---

## 📋 Cenários Práticos com Make.com

### 1. Daily AI Summary para Notion

**Componentes:**
```
[Schedule] → [HTTP: Groq API] → [Text Parser] → [Notion: Create Page]
```

**Configuração Passo a Passo:**

**Módulo 1 - Schedule (Trigger):**
```
Type: Every Day
Time: 09:00
Time Zone: America/Sao_Paulo
```

**Módulo 2 - HTTP Request (Groq):**
```
URL: https://api.groq.com/openai/v1/chat/completions
Method: POST
Headers:
  - Authorization: Bearer YOUR_GROQ_API_KEY
  - Content-Type: application/json
Body Type: Raw
Body:
{
  "model": "llama-3.1-70b-versatile",
  "messages": [
    {
      "role": "user",
      "content": "Crie um resumo diário sobre tendências de tecnologia em 2024. Formato Markdown."
    }
  ],
  "temperature": 0.7,
  "max_tokens": 2000
}
```

**Módulo 3 - Text Parser:**
```
Pattern: {{2.choices[0].message.content}}
```

**Módulo 4 - Notion: Create Page:**
```
Database: Seu Database
Title: Daily Tech Summary - {{formatDate(now; "DD/MM/YYYY")}}
Content: {{3.text}}
```

---

### 2. Resumir Artigos Salvos no Notion

**Componentes:**
```
[Notion: Watch Items] → [HTTP: Get Article] → [Groq: Summarize] → [Notion: Update Item]
```

**Módulo 1 - Notion: Watch Database Items:**
```
Database ID: SEU_DATABASE_ID
Filter: Status = "To Summarize"
```

**Módulo 2 - HTTP Request (Fetch Article):**
```
URL: {{1.properties.URL.url}}
Method: GET
```

**Módulo 3 - HTTP Request (Groq - Summarize):**
```
Body:
{
  "model": "llama-3.1-70b-versatile",
  "messages": [
    {
      "role": "user",
      "content": "Resuma este artigo em 3 parágrafos:\n\n{{2.data}}"
    }
  ]
}
```

**Módulo 4 - Notion: Update Page:**
```
Page ID: {{1.id}}
Property: Summary
Value: {{3.choices[0].message.content}}
Status: Summarized
```

---

### 3. Gerador de Conteúdo Semanal

**Trigger: Webhook**

```bash
# Chamar via curl ou script
curl -X POST https://hook.make.com/YOUR_WEBHOOK_ID \
  -H "Content-Type: application/json" \
  -d '{
    "topic": "IA no marketing",
    "format": "guia completo",
    "sections": 5
  }'
```

**Processamento:**
```
[Webhook] → [Router] → [Multiple AI Requests] → [Aggregator] → [Notion: Create]
```

---

### 4. Análise de Feedback do Notion

**Cenário:**
Você tem um database de feedback. Make.com analisa diariamente com IA.

```
[Schedule] → [Notion: Search] → [Iterator] → [Groq: Analyze] → [Notion: Update]
```

**Groq Prompt:**
```
Analise este feedback e classifique:
- Sentimento: Positivo/Neutro/Negativo
- Categoria: Bug/Feature/Elogio/Outro
- Prioridade: Alta/Média/Baixa
- Resumo: (1 frase)

Feedback: {{item.properties.Feedback.text}}

Retorne JSON:
{
  "sentiment": "",
  "category": "",
  "priority": "",
  "summary": ""
}
```

---

## 🟧 Zapier

### Limitações do Plano Gratuito

- ⚠️ Apenas 100 tasks/mês
- ⚠️ 5 Zaps ativos
- ⚠️ 15 minutos de intervalo (não real-time)

### Quando Usar Zapier

- Templates prontos para começar rápido
- Integrações com apps não disponíveis no Make
- Simplicidade sobre complexidade

### Exemplo de Zap

**Zap: Email → GPT → Notion**

```
Trigger: Gmail (New Email)
Filter: Subject contains "Summary Request"
Action 1: OpenAI (Completion)
  Prompt: Resuma este email: {{body}}
Action 2: Notion (Create Page)
  Title: Email Summary - {{subject}}
  Content: {{openai.output}}
```

---

## 🟩 Pipedream (Serverless)

### Vantagens

✅ **Código + No-Code**: Híbrido  
✅ **Free Tier**: 333 credits/mês  
✅ **Serverless**: Não precisa hospedar  
✅ **Instant Triggers**: Webhooks em tempo real

### Workflow Example

```javascript
// Pipedream Workflow: Groq → Notion
export default defineComponent({
  async run({ steps, $ }) {
    // 1. Chamar Groq
    const groqResponse = await require("@pipedreamhq/platform").axios($, {
      url: 'https://api.groq.com/openai/v1/chat/completions',
      method: 'POST',
      headers: {
        Authorization: `Bearer ${this.groq.$auth.api_key}`,
        'Content-Type': 'application/json'
      },
      data: {
        model: 'llama-3.1-70b-versatile',
        messages: [
          {
            role: 'user',
            content: 'Crie um plano de estudos de Python'
          }
        ]
      }
    });
    
    const content = groqResponse.choices[0].message.content;
    
    // 2. Enviar para Notion
    await require("@pipedreamhq/platform").axios($, {
      url: `https://api.notion.com/v1/blocks/${process.env.NOTION_PAGE_ID}/children`,
      method: 'PATCH',
      headers: {
        Authorization: `Bearer ${this.notion.$auth.oauth_access_token}`,
        'Notion-Version': '2022-06-28',
        'Content-Type': 'application/json'
      },
      data: {
        children: [
          {
            object: 'block',
            type: 'paragraph',
            paragraph: {
              rich_text: [{ text: { content } }]
            }
          }
        ]
      }
    });
    
    return { success: true, content };
  }
});
```

---

## 🆓 Alternativas Gratuitas

### 1. IFTTT

**Limitações:**
- Muito básico para IA + Notion
- Sem integração Notion nativa
- Apenas applets simples

**Uso possível:**
```
Webhook → Email → (Manual para Notion)
```

### 2. Automate.io

**Free Tier:**
- 300 actions/mês
- Integrações limitadas

---

## 📊 Comparação de Plataformas

| Plataforma | Custo (Free) | Ops/Mês | Notion | IA APIs | Complexidade |
|------------|--------------|---------|--------|---------|--------------|
| **Make.com** | ✅ Grátis | 1.000 | ✅ Nativo | ✅ HTTP | ⭐⭐ Média |
| **Zapier** | ⚠️ Limitado | 100 | ✅ Nativo | ⚠️ Limitado | ⭐ Fácil |
| **Pipedream** | ✅ Grátis | 333 | ✅ API | ✅ Código | ⭐⭐⭐ Alta |
| **n8n** | ✅ Grátis | Ilimitado | ✅ Nativo | ✅ HTTP | ⭐⭐⭐ Alta |
| **IFTTT** | ⚠️ Muito limitado | 100 | ❌ Não | ❌ Não | ⭐ Muito Fácil |

---

## 🎯 Stack Recomendada por Perfil

### Para Iniciantes
```
Make.com (visual) + Groq (grátis) + Notion
```

### Para Desenvolvedores
```
Pipedream (híbrido) + Qualquer LLM + Notion
```

### Para Máxima Flexibilidade
```
n8n (self-hosted) + Ollama (local) + Notion
```

### Para Simplicidade Extrema
```
Zapier + OpenAI + Notion
(Custos: Zapier pago + OpenAI API)
```

---

## 🔧 Templates Prontos

### Template 1: Daily Digest

**Make.com Scenario JSON:**
```json
{
  "name": "Daily AI Digest to Notion",
  "flow": [
    {
      "id": 1,
      "module": "gateway:Schedule",
      "version": 1,
      "parameters": {
        "schedule": {
          "time": "09:00",
          "timezone": "America/Sao_Paulo"
        }
      }
    },
    {
      "id": 2,
      "module": "http:ActionMakeRequest",
      "parameters": {
        "url": "https://api.groq.com/openai/v1/chat/completions",
        "method": "POST",
        "headers": [
          {
            "name": "Authorization",
            "value": "Bearer {{secrets.GROQ_API_KEY}}"
          }
        ],
        "qs": [],
        "bodyType": "raw",
        "rawBody": "{\"model\":\"llama-3.1-70b-versatile\",\"messages\":[{\"role\":\"user\",\"content\":\"Resumo diário de tech\"}]}"
      }
    },
    {
      "id": 3,
      "module": "notion:createPage",
      "parameters": {
        "parent": "{{database.dailyDigest}}",
        "properties": {
          "title": "Daily Summary - {{formatDate(now)}}",
          "content": "{{2.choices[0].message.content}}"
        }
      }
    }
  ]
}
```

### Template 2: Article Summarizer

**Zapier Template:**
```
Name: Auto-Summarize Articles in Notion
Trigger: Notion - New Database Item
  Filter: Status = "To Read"
Action 1: Webhooks - GET
  URL: {{trigger.properties.URL}}
Action 2: OpenAI - Completion
  Prompt: Summarize: {{webhooks.content}}
Action 3: Notion - Update Database Item
  ID: {{trigger.id}}
  Summary: {{openai.text}}
  Status: "Summarized"
```

---

## 💡 Use Cases Avançados

### 1. Multi-Language Content Generator

**Make.com:**
```
[Trigger] → [Groq: Generate EN] → [Router]
  ├─→ [Groq: Translate PT] → [Notion: Create PT]
  └─→ [Groq: Translate ES] → [Notion: Create ES]
```

### 2. Smart Meeting Notes

**Pipedream:**
```javascript
// 1. Webhook recebe transcrição de reunião
// 2. GPT extrai action items
// 3. Cria tarefas no Notion para cada pessoa
```

### 3. Content Calendar Automation

**Make.com:**
```
[Groq: Generate Ideas] → [Iterator] → [Notion: Create in Calendar]
```

---

## 🚨 Troubleshooting

### Erro: "Rate limit exceeded"

**Solução em Make.com:**
```
Adicionar módulo "Sleep" entre requests:
[HTTP Request] → [Sleep: 2s] → [Next Request]
```

### Erro: "Notion API validation error"

**Verificar:**
- Format dos blocos está correto?
- Propriedades do database existem?
- Integração está conectada à página?

### Workflow não executa

**Make.com:**
- Verificar se scenario está "ON"
- Checar histórico de execuções
- Validar credenciais das conexões

---

## 📚 Recursos de Aprendizado

### Make.com
- 📖 Docs: https://www.make.com/en/help
- 🎓 Academy: https://www.make.com/en/academy
- 📺 YouTube: Canal oficial Make

### Zapier
- 📖 Docs: https://zapier.com/help
- 🎓 Learn: https://learn.zapier.com/
- 🗂️ Templates: https://zapier.com/apps/notion/integrations

### Pipedream
- 📖 Docs: https://pipedream.com/docs
- 💻 GitHub: https://github.com/PipedreamHQ
- 🌐 Community: https://pipedream.com/community

---

## ⏱️ Estimativa de Setup

| Plataforma | Tempo Setup | Dificuldade | Resultado |
|------------|-------------|-------------|-----------|
| Make.com | 30 min | ⭐⭐ | Workflow visual funcionando |
| Zapier | 15 min | ⭐ | Zap básico ativo |
| Pipedream | 45 min | ⭐⭐⭐ | Workflow híbrido |
| n8n | 2 horas | ⭐⭐⭐⭐ | Self-hosted completo |

---

## 🎁 Bônus: Webhooks para Integrar

### Criar Webhook no Make.com

1. Adicionar módulo "Webhooks: Custom webhook"
2. Copiar URL gerada
3. Chamar de qualquer lugar:

```bash
curl -X POST https://hook.make.com/YOUR_ID \
  -H "Content-Type: application/json" \
  -d '{
    "action": "create_summary",
    "topic": "IA em 2024",
    "format": "markdown"
  }'
```

### Processar no Workflow

```
[Webhook] → [Parse JSON] → [Groq AI] → [Notion]
```

---

## Próximos Passos

- → **[Scripts de Exemplo](07-Scripts-Exemplos/)**
- → **[Templates de Workflows](08-Templates-Workflows/)**
- → **[Voltar ao Início](README.md)**
