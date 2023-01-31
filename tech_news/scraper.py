import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
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
    return Selector(html_content).css(".entry-title a::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    return Selector(text=html_content).css(".next::attr(href)").get()


# Requisito 4
def scrape_news(html_content):
    page = Selector(html_content)


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
