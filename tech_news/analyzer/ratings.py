from tech_news.database import find_news
from collections import Counter


def criterion(e):
    return e["comments_count"]


# Requisito 10
def top_5_news():
    """
        Retornará 5 notícias rankeadas pelo critério de quantidade
        de comentários.
    """
    news = find_news()
    news.sort(key=criterion, reverse=True)

    return [
        (top['title'], top['url'])
        for top in news[:5]
    ]


# Requisito 11
def top_5_categories():
    """
        Retorna um ranking com as 5 categorias mais populares entres as
        notícias armazenadas no banco de dados.
    """
    categories = [news["category"] for news in find_news()]
    count = Counter(sorted(categories))
    return [top_categories[0] for top_categories in count.most_common(5)]
