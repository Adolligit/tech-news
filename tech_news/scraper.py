import re
import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    """Retorna a estrutura HTML da página"""
    try:
        time.sleep(1)
        response = requests.get(
            url,
            3,
            {"user-agent": "Fake user-agent"}
        )
        response.raise_for_status()
    except (requests.Timeout, requests.HTTPError):
        return None
    else:
        return response.text


# Requisito 2
def scrape_updates(html_content) -> list:
    """Busca através do HTML por links específicos e os retorna em uma vetor"""
    return Selector(html_content).css(".entry-title a::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    """Busca o botão de ir para a próxima página e retorna sua url"""
    return Selector(text=html_content).css(".next::attr(href)").get()


# Requisito 4
def scrape_news(html_content):
    """
        Através do HTML, busca elementos específicos e
        retorna seus dados estruturados
    """
    page = Selector(html_content)
    url = page.css('head').xpath('//link[@rel="canonical"]').attrib['href']
    title = page.xpath('//h1[@class="entry-title"]/text()').get().strip()
    timestamp = page.css('.meta-date::text').get()
    writer = page.css('.author a::text').get()
    comments_count = page.xpath('//div[@id="comments"]//h5/text()').get()
    comments_count = comments_count.split()[0] if comments_count else 0

    paragraph = page.css('.entry-content p').get()
    summary = re.compile(r'<.*?>').sub('', paragraph).strip()

    tags = page.xpath('//a[@rel="tag"]/text()').getall()
    category = page.xpath('//span[@class="label"]/text()').get()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": comments_count,
        "summary": summary,
        "tags": tags,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount) -> list:
    """Busca e retorna a quantidade exata de notíticas"""
    url = 'https://blog.betrybe.com'
    news = []

    while len(news) < amount:
        page = fetch(url)
        news += scrape_updates(page)
        url = scrape_next_page_link(page)

    news = [
        scrape_news(fetch(link))
        for link in news[:amount]
    ]

    create_news(news)

    return news
