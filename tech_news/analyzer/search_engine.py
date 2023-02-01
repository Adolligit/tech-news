from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    """Busca e retorna notícias pelo título fornecido como parâmetro"""
    found = search_news({"title": {"$regex": title, "$options": "i"}})

    return [
        (news["title"], news["url"])
        for news in found
    ]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        datetime.fromisoformat(date)
        formatted_date = date.split('-')
        formatted_date.reverse()
        formatted_date = '/'.join(formatted_date)

        found = search_news({"timestamp": {"$eq": formatted_date}})
    except ValueError:
        raise ValueError('Data inválida')
    else:
        return [
            (news["title"], news["url"])
            for news in found
        ]


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
