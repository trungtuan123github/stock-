import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

def get_yahoo_news(ticker, limit=10):
    url = f'https://finance.yahoo.com/quote/{ticker}/news'

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(url)
        time.sleep(5)  # Chờ tải đầy đủ nội dung trang

        # Cuộn xuống để load thêm nội dung nếu cần
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        soup = BeautifulSoup(driver.page_source, 'html.parser')

        news_list = []
        articles = soup.select('li.js-stream-content a[href*="/news/"]')

        for a_tag in articles[:limit]:
            title = a_tag.text.strip()
            link = 'https://finance.yahoo.com' + a_tag['href']
            news_list.append({
                'title': title,
                'url': link,
                'time': 'Unknown'  # Bạn có thể mở rộng để crawl thời gian cụ thể
            })

        return news_list

    finally:
        driver.quit()
import requests

def get_yahoo_news_via_api(ticker, limit=10):
    query = ticker
    url = f"https://query2.finance.yahoo.com/v1/finance/search?q={query}&newsCount={limit}"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception("Không thể truy cập Yahoo Finance API")

    data = response.json()

    news_items = []
    for item in data.get("news", [])[:limit]:
        news_items.append({
            "title": item["title"],
            "url": item["link"],
            "time": item.get("providerPublishTime", "Unknown")
        })

    return news_items
