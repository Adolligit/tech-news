from tech_news.database import find_news


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
    """Seu código deve vir aqui"""
