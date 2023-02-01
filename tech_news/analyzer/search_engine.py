from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    """
        Busca por notícias que correspondem ao 'title' e retorna o título
        e sua url
    """
    found = search_news({"title": {"$regex": title, "$options": "i"}})

    return [
        (news["title"], news["url"])
        for news in found
    ]


# Requisito 7
def search_by_date(date):
    """
        Procura por notícias que correspondem a data. Retorna seu título e url.
    """
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
    """
        Encontra notícias que corresponde a 'tag' fornecedida como parâmetro.
        Retorna uma lista de tuplas com 'title' e 'url' de cada notícia
        encontrada.
    """
    found = search_news({"tags": {"$regex": tag, "$options": "i"}})

    return [
        (news["title"], news["url"])
        for news in found
    ]


# Requisito 9
def search_by_category(category):
    """
        Vai encontrar notícias que tem a mesma categoria fornecida como
        parâmetro. Retornará uma lista com tuplas, contendo 'title' e 'url' de
        cada notícia encontrada.
    """
    found = search_news({"category": {"$regex": category, "$options": "i"}})

    return [
        (news["title"], news["url"])
        for news in found
    ]
