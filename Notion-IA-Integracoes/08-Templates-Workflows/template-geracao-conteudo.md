# ✍️ Template: Geração de Conteúdo para Notion

## Objetivo
Automatizar a criação de conteúdo estruturado usando IA.

## Use Cases

### 1. Blog Posts
### 2. Documentação Técnica
### 3. Planos de Projeto
### 4. Guias de Estudo
### 5. Templates de Reunião

---

## 📝 Template 1: Blog Post Completo

### Prompt Otimizado

```python
def generate_blog_post(topic, tone="professional", length="medium"):
    prompt = f"""
    Crie um artigo de blog completo sobre: {topic}
    
    Especificações:
    - Tom: {tone}
    - Tamanho: {length} (~800 palavras)
    - Público: Profissionais da área
    
    Estrutura OBRIGATÓRIA:
    # [Título Cativante]
    
    ## Introdução
    [Hook inicial + contexto + o que o leitor vai aprender]
    
    ## [Subtópico 1]
    [Desenvolvimento com exemplos práticos]
    
    ## [Subtópico 2]
    [Desenvolvimento com exemplos práticos]
    
    ## [Subtópico 3]
    [Desenvolvimento com exemplos práticos]
    
    ## Conclusão
    [Resumo + call to action]
    
    ## Recursos Adicionais
    [Links úteis, leituras recomendadas]
    
    IMPORTANTE:
    - Use Markdown
    - Inclua listas e exemplos
    - Seja prático e acionável
    - Adicione estatísticas quando relevante
    """
    
    return generate_content_with_groq(prompt)
```

### Script Completo

```python
from groq import Groq
from notion_client import Client
import os
from datetime import datetime

groq = Groq(api_key=os.getenv("GROQ_API_KEY"))
notion = Client(auth=os.getenv("NOTION_TOKEN"))

def create_blog_post_in_notion(topic, parent_page_id):
    """
    Gera e publica blog post no Notion
    """
    # 1. Gerar conteúdo
    prompt = f"""
    Crie um artigo de blog sobre: {topic}
    
    Estrutura:
    # Título
    ## Introdução
    ## 3-4 Seções Principais
    ## Conclusão
    
    Formato: Markdown, tom profissional, ~800 palavras
    """
    
    response = groq.chat.completions.create(
        model="llama-3.1-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    
    content = response.choices[0].message.content
    
    # 2. Extrair título
    title = content.split('\n')[0].replace('# ', '')
    
    # 3. Criar página no Notion
    new_page = notion.pages.create(
        parent={"page_id": parent_page_id},
        properties={
            "title": {
                "title": [{"text": {"content": title}}]
            }
        }
    )
    
    # 4. Adicionar conteúdo
    blocks = parse_markdown_to_blocks(content)
    notion.blocks.children.append(
        block_id=new_page["id"],
        children=blocks
    )
    
    print(f"✅ Blog post criado: {title}")
    return new_page["url"]

# Exemplo de uso
url = create_blog_post_in_notion(
    "Como usar IA para aumentar produtividade",
    parent_page_id="YOUR_PAGE_ID"
)
print(f"📄 Link: {url}")
```

---

## 📚 Template 2: Documentação Técnica

### Prompt

```python
def generate_technical_doc(feature_name, api_details):
    prompt = f"""
    Crie documentação técnica para: {feature_name}
    
    Detalhes da API: {api_details}
    
    Estrutura:
    # {feature_name} - Documentação
    
    ## Visão Geral
    [Descrição breve, propósito, quando usar]
    
    ## Instalação
    [Comandos, dependências, pré-requisitos]
    
    ## Quick Start
    [Exemplo mínimo funcionando]
    
    ## API Reference
    [Métodos, parâmetros, retornos]
    
    ## Exemplos Avançados
    [3-4 casos de uso reais]
    
    ## Troubleshooting
    [Problemas comuns e soluções]
    
    ## Changelog
    [Versão atual e mudanças recentes]
    
    Use code blocks, tabelas quando apropriado.
    Seja preciso e completo.
    """
    
    return generate_content_with_gemini(prompt)
```

### Exemplo de Uso

```python
doc = generate_technical_doc(
    feature_name="User Authentication API",
    api_details="""
    POST /api/auth/login
    POST /api/auth/register
    GET /api/auth/verify
    POST /api/auth/logout
    """
)

send_to_notion(doc, database_id=DOCS_DATABASE)
```

---

## 🎯 Template 3: Plano de Projeto

### Script Automatizado

```python
def create_project_plan(project_name, goals, duration_weeks):
    """
    Gera plano de projeto estruturado
    """
    prompt = f"""
    Crie um plano de projeto para: {project_name}
    
    Objetivos: {goals}
    Duração: {duration_weeks} semanas
    
    Estrutura:
    # Plano de Projeto: {project_name}
    
    ## Executive Summary
    [Resumo do projeto em 2 parágrafos]
    
    ## Objetivos
    - Objetivo 1
    - Objetivo 2
    - Objetivo 3
    
    ## Escopo
    ### Incluído
    - [Item 1]
    - [Item 2]
    
    ### Não Incluído
    - [Item 1]
    - [Item 2]
    
    ## Timeline
    ### Semana 1-2: [Fase]
    - Task 1
    - Task 2
    
    ### Semana 3-4: [Fase]
    - Task 1
    - Task 2
    
    [Continue para {duration_weeks} semanas]
    
    ## Recursos Necessários
    - Humanos
    - Tecnológicos
    - Financeiros
    
    ## Riscos e Mitigação
    | Risco | Probabilidade | Impacto | Mitigação |
    |-------|---------------|---------|-----------|
    | ... | ... | ... | ... |
    
    ## Critérios de Sucesso
    - KPI 1
    - KPI 2
    - KPI 3
    
    ## Próximos Passos
    1. [Ação imediata]
    2. [Ação seguinte]
    """
    
    content = generate_content_with_groq(prompt)
    
    # Criar no Notion com metadata
    page = notion.pages.create(
        parent={"database_id": PROJECTS_DATABASE},
        properties={
            "Nome": {"title": [{"text": {"content": project_name}}]},
            "Status": {"select": {"name": "Planning"}},
            "Duração": {"number": duration_weeks},
            "Data Início": {"date": {"start": datetime.now().isoformat()}},
        }
    )
    
    # Adicionar conteúdo
    blocks = parse_markdown_to_blocks(content)
    notion.blocks.children.append(block_id=page["id"], children=blocks)
    
    return page["url"]

# Uso
url = create_project_plan(
    project_name="Nova Feature de Dashboard",
    goals="Criar dashboard interativo com métricas em tempo real",
    duration_weeks=8
)
```

---

## 🎓 Template 4: Guia de Estudos

### Gerador de Currículo de Aprendizado

```python
def create_learning_path(topic, skill_level, time_available):
    """
    Cria guia de estudos personalizado
    """
    prompt = f"""
    Crie um guia de estudos completo para aprender: {topic}
    
    Nível atual: {skill_level}
    Tempo disponível: {time_available}
    
    # Guia de Estudos: {topic}
    
    ## Introdução
    [Por que aprender? Aplicações práticas. Oportunidades.]
    
    ## Pré-requisitos
    - [Conhecimento 1]
    - [Conhecimento 2]
    
    ## Conceitos Fundamentais
    ### Conceito 1: [Nome]
    - O que é
    - Por que importante
    - Como aprender
    
    [Repetir para 5-7 conceitos]
    
    ## Plano de Estudos ({time_available})
    
    ### Semana 1: [Tema]
    - [ ] Tarefa 1
    - [ ] Tarefa 2
    - [ ] Projeto prático
    
    [Continue conforme tempo disponível]
    
    ## Recursos Recomendados
    ### Cursos
    - [Curso 1] - Motivo
    - [Curso 2] - Motivo
    
    ### Livros
    - [Livro 1] - Para quem
    - [Livro 2] - Para quem
    
    ### Comunidades
    - [Comunidade 1]
    - [Comunidade 2]
    
    ## Projetos Práticos
    1. [Projeto Iniciante] - Objetivos de aprendizado
    2. [Projeto Intermediário] - Objetivos
    3. [Projeto Avançado] - Objetivos
    
    ## Checklist de Progresso
    - [ ] Domino conceito A
    - [ ] Completei projeto B
    - [ ] Posso explicar C
    
    ## Próximos Passos
    [O que estudar depois de dominar este tópico]
    """
    
    content = generate_content_with_gemini(prompt, "gemini-1.5-flash")
    
    # Criar página de estudo
    page = notion.pages.create(
        parent={"database_id": LEARNING_DATABASE},
        properties={
            "Tópico": {"title": [{"text": {"content": topic}}]},
            "Nível": {"select": {"name": skill_level}},
            "Status": {"select": {"name": "Em Progresso"}},
            "Data Início": {"date": {"start": datetime.now().isoformat()}}
        }
    )
    
    blocks = parse_markdown_to_blocks(content)
    notion.blocks.children.append(block_id=page["id"], children=blocks)
    
    return page["url"]

# Exemplo
url = create_learning_path(
    topic="Python para Data Science",
    skill_level="Iniciante",
    time_available="3 meses"
)
```

---

## 📋 Template 5: Notas de Reunião

### Auto-gerador de Atas

```python
def create_meeting_template(meeting_type, attendees, main_topics):
    """
    Gera template de reunião preenchido
    """
    prompt = f"""
    Crie notas de reunião estruturadas para:
    
    Tipo: {meeting_type}
    Participantes: {', '.join(attendees)}
    Tópicos: {', '.join(main_topics)}
    
    # {meeting_type} - {datetime.now().strftime('%d/%m/%Y')}
    
    ## Informações
    - **Data**: {datetime.now().strftime('%d/%m/%Y às %H:%M')}
    - **Participantes**: {', '.join(attendees)}
    - **Duração**: [A preencher]
    
    ## Agenda
    {chr(10).join([f'{i}. {topic}' for i, topic in enumerate(main_topics, 1)])}
    
    ## Discussões
    ### {main_topics[0]}
    - **Discussão**: [Resumo dos pontos discutidos]
    - **Decisões**: [O que foi decidido]
    - **Preocupações**: [Pontos levantados]
    
    [Repetir para cada tópico]
    
    ## Action Items
    | Ação | Responsável | Prazo | Status |
    |------|-------------|-------|--------|
    | [Ação 1] | [Nome] | [Data] | ⏳ Pendente |
    | [Ação 2] | [Nome] | [Data] | ⏳ Pendente |
    
    ## Decisões Importantes
    - ✅ [Decisão 1]
    - ✅ [Decisão 2]
    
    ## Próxima Reunião
    - **Data Proposta**: [Data]
    - **Tópicos**: [Lista]
    
    ## Notas Adicionais
    [Observações, links compartilhados, etc]
    """
    
    content = generate_content_with_groq(prompt)
    
    # Criar no database de reuniões
    page = notion.pages.create(
        parent={"database_id": MEETINGS_DATABASE},
        properties={
            "Título": {"title": [{"text": {"content": f"{meeting_type} - {datetime.now().strftime('%d/%m/%Y')}"}}]},
            "Tipo": {"select": {"name": meeting_type}},
            "Data": {"date": {"start": datetime.now().isoformat()}},
            "Participantes": {"multi_select": [{"name": name} for name in attendees]}
        }
    )
    
    blocks = parse_markdown_to_blocks(content)
    notion.blocks.children.append(block_id=page["id"], children=blocks)
    
    return page["url"]
```

---

## 🔄 Automação Completa

### Script Master para Múltiplos Tipos

```python
def auto_content_generator():
    """
    Sistema completo de geração de conteúdo
    """
    content_types = {
        "blog": create_blog_post_in_notion,
        "docs": generate_technical_doc,
        "project": create_project_plan,
        "learning": create_learning_path,
        "meeting": create_meeting_template
    }
    
    # Menu interativo
    print("🤖 Gerador de Conteúdo IA + Notion")
    print("\nEscolha o tipo de conteúdo:")
    for i, (key, _) in enumerate(content_types.items(), 1):
        print(f"{i}. {key.title()}")
    
    choice = input("\nOpção: ")
    # ... implementar lógica de seleção
```

---

## 📊 Métricas e Acompanhamento

### Dashboard de Conteúdo Gerado

Criar no Notion:

**Database: Content Generated**

| Campo | Tipo | Descrição |
|-------|------|-----------|
| Título | Title | Nome do conteúdo |
| Tipo | Select | Blog/Docs/Project/etc |
| Palavras | Number | Contagem |
| Modelo IA | Select | Groq/Gemini/GPT |
| Data Criação | Created time | Auto |
| Custo Estimado | Formula | Baseado em tokens |
| Qualidade | Select | Alta/Média/Baixa |
| Status | Select | Rascunho/Revisão/Publicado |

---

## Próximos Passos

1. ✅ Escolher templates relevantes
2. 🔧 Customizar prompts
3. 🚀 Automatizar geração
4. 📊 Acompanhar métricas
5. 🔄 Iterar e melhorar

**Template para maximizar criação de conteúdo com IA**
