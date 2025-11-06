"""
Helper functions para trabalhar com Notion API

Funções úteis para:
- Criar páginas
- Atualizar conteúdo
- Buscar informações
- Manipular databases
"""

import os
from notion_client import Client
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
notion = Client(auth=NOTION_TOKEN)


# ============================================
# FUNÇÕES DE BLOCOS (BLOCKS)
# ============================================

def create_heading(text, level=2):
    """
    Cria um header (H1, H2 ou H3)
    """
    heading_type = f"heading_{level}"
    return {
        "object": "block",
        "type": heading_type,
        heading_type: {
            "rich_text": [{"text": {"content": text}}]
        }
    }


def create_paragraph(text):
    """
    Cria um parágrafo
    """
    return {
        "object": "block",
        "type": "paragraph",
        "paragraph": {
            "rich_text": [{"text": {"content": text}}]
        }
    }


def create_bullet_list(items):
    """
    Cria uma lista de bullets
    """
    blocks = []
    for item in items:
        blocks.append({
            "object": "block",
            "type": "bulleted_list_item",
            "bulleted_list_item": {
                "rich_text": [{"text": {"content": item}}]
            }
        })
    return blocks


def create_numbered_list(items):
    """
    Cria uma lista numerada
    """
    blocks = []
    for item in items:
        blocks.append({
            "object": "block",
            "type": "numbered_list_item",
            "numbered_list_item": {
                "rich_text": [{"text": {"content": item}}]
            }
        })
    return blocks


def create_code_block(code, language="python"):
    """
    Cria um bloco de código
    """
    return {
        "object": "block",
        "type": "code",
        "code": {
            "rich_text": [{"text": {"content": code}}],
            "language": language
        }
    }


def create_quote(text):
    """
    Cria uma citação
    """
    return {
        "object": "block",
        "type": "quote",
        "quote": {
            "rich_text": [{"text": {"content": text}}]
        }
    }


def create_callout(text, icon="💡"):
    """
    Cria um callout
    """
    return {
        "object": "block",
        "type": "callout",
        "callout": {
            "rich_text": [{"text": {"content": text}}],
            "icon": {"emoji": icon}
        }
    }


def create_divider():
    """
    Cria um divisor
    """
    return {
        "object": "block",
        "type": "divider",
        "divider": {}
    }


def create_toggle(title, children_blocks):
    """
    Cria um toggle (acordeão)
    """
    return {
        "object": "block",
        "type": "toggle",
        "toggle": {
            "rich_text": [{"text": {"content": title}}],
            "children": children_blocks
        }
    }


def create_bookmark(url, caption=""):
    """
    Cria um bookmark
    """
    block = {
        "object": "block",
        "type": "bookmark",
        "bookmark": {
            "url": url
        }
    }
    
    if caption:
        block["bookmark"]["caption"] = [{"text": {"content": caption}}]
    
    return block


# ============================================
# FUNÇÕES DE PÁGINAS (PAGES)
# ============================================

def create_page(parent_id, title, children_blocks=None):
    """
    Cria uma nova página
    """
    page_data = {
        "parent": {"page_id": parent_id},
        "properties": {
            "title": {
                "title": [
                    {
                        "text": {
                            "content": title
                        }
                    }
                ]
            }
        }
    }
    
    if children_blocks:
        page_data["children"] = children_blocks
    
    response = notion.pages.create(**page_data)
    return response


def update_page_title(page_id, new_title):
    """
    Atualiza o título de uma página
    """
    response = notion.pages.update(
        page_id=page_id,
        properties={
            "title": {
                "title": [
                    {
                        "text": {
                            "content": new_title
                        }
                    }
                ]
            }
        }
    )
    return response


def append_blocks(page_id, blocks):
    """
    Adiciona blocos a uma página existente
    """
    response = notion.blocks.children.append(
        block_id=page_id,
        children=blocks
    )
    return response


def get_page_content(page_id):
    """
    Obtém o conteúdo de uma página
    """
    blocks = []
    has_more = True
    next_cursor = None
    
    while has_more:
        response = notion.blocks.children.list(
            block_id=page_id,
            start_cursor=next_cursor
        )
        
        blocks.extend(response.get("results", []))
        has_more = response.get("has_more", False)
        next_cursor = response.get("next_cursor")
    
    return blocks


# ============================================
# FUNÇÕES DE DATABASE
# ============================================

def create_database_page(database_id, properties):
    """
    Cria uma nova página em um database
    
    Exemplo de properties:
    {
        "Name": {"title": [{"text": {"content": "Meu Item"}}]},
        "Status": {"select": {"name": "Em Progresso"}},
        "Tags": {"multi_select": [{"name": "importante"}, {"name": "urgente"}]},
        "Data": {"date": {"start": "2024-01-01"}},
        "Numero": {"number": 42}
    }
    """
    response = notion.pages.create(
        parent={"database_id": database_id},
        properties=properties
    )
    return response


def query_database(database_id, filter_conditions=None, sorts=None):
    """
    Busca itens em um database
    
    Exemplo de filter:
    {
        "property": "Status",
        "select": {"equals": "Em Progresso"}
    }
    
    Exemplo de sorts:
    [
        {
            "property": "Data",
            "direction": "descending"
        }
    ]
    """
    query_params = {"database_id": database_id}
    
    if filter_conditions:
        query_params["filter"] = filter_conditions
    
    if sorts:
        query_params["sorts"] = sorts
    
    results = []
    has_more = True
    next_cursor = None
    
    while has_more:
        if next_cursor:
            query_params["start_cursor"] = next_cursor
        
        response = notion.databases.query(**query_params)
        results.extend(response.get("results", []))
        has_more = response.get("has_more", False)
        next_cursor = response.get("next_cursor")
    
    return results


def update_database_page(page_id, properties):
    """
    Atualiza propriedades de uma página em database
    """
    response = notion.pages.update(
        page_id=page_id,
        properties=properties
    )
    return response


# ============================================
# HELPERS ÚTEIS
# ============================================

def create_daily_note(parent_id, content_blocks=None):
    """
    Cria nota diária com data de hoje
    """
    today = datetime.now().strftime("%Y-%m-%d")
    title = f"Daily Note - {today}"
    
    blocks = [
        create_heading(f"📅 {today}", 1),
        create_divider()
    ]
    
    if content_blocks:
        blocks.extend(content_blocks)
    
    return create_page(parent_id, title, blocks)


def create_meeting_notes(parent_id, meeting_title, attendees, topics, action_items):
    """
    Cria template de notas de reunião
    """
    blocks = [
        create_heading(meeting_title, 1),
        create_callout(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M')}", "📅"),
        create_divider(),
        
        create_heading("Participantes", 2),
        *create_bullet_list(attendees),
        
        create_heading("Tópicos Discutidos", 2),
        *create_numbered_list(topics),
        
        create_heading("Action Items", 2),
        *create_bullet_list(action_items)
    ]
    
    return create_page(parent_id, meeting_title, blocks)


def create_article_summary(parent_id, article_title, url, summary_points, key_quotes):
    """
    Cria resumo de artigo
    """
    blocks = [
        create_heading(article_title, 1),
        create_bookmark(url, "Artigo original"),
        create_divider(),
        
        create_heading("Resumo", 2),
        *create_bullet_list(summary_points),
        
        create_heading("Citações Importantes", 2)
    ]
    
    for quote in key_quotes:
        blocks.append(create_quote(quote))
    
    return create_page(parent_id, f"Resumo: {article_title}", blocks)


def create_learning_resource(parent_id, topic, resources, key_concepts):
    """
    Cria página de recursos de aprendizado
    """
    blocks = [
        create_heading(f"📚 {topic}", 1),
        create_divider(),
        
        create_heading("Conceitos Chave", 2),
        *create_bullet_list(key_concepts),
        
        create_heading("Recursos Recomendados", 2)
    ]
    
    for resource_name, resource_url in resources.items():
        blocks.append(create_bookmark(resource_url, resource_name))
    
    return create_page(parent_id, topic, blocks)


# ============================================
# EXEMPLO DE USO
# ============================================

def example_usage():
    """
    Demonstração de uso das funções
    """
    PAGE_ID = os.getenv("NOTION_PAGE_ID")
    
    # Exemplo 1: Criar conteúdo estruturado
    blocks = [
        create_heading("Meu Guia de Python", 1),
        create_callout("Este é um guia completo para iniciantes!", "🎓"),
        create_divider(),
        
        create_heading("Introdução", 2),
        create_paragraph("Python é uma linguagem de programação poderosa e fácil de aprender."),
        
        create_heading("Conceitos Básicos", 2),
        *create_bullet_list([
            "Variáveis e tipos de dados",
            "Estruturas de controle",
            "Funções",
            "Classes e objetos"
        ]),
        
        create_heading("Exemplo de Código", 2),
        create_code_block('def hello_world():\n    print("Hello, World!")', "python"),
        
        create_heading("Recursos", 2),
        create_bookmark("https://docs.python.org/", "Documentação Oficial")
    ]
    
    append_blocks(PAGE_ID, blocks)
    print("✅ Conteúdo criado com sucesso!")


if __name__ == "__main__":
    if NOTION_TOKEN:
        example_usage()
    else:
        print("❌ Configure NOTION_TOKEN no .env")
