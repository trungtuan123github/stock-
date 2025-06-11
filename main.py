from price_analysis.fetch_yahoo import fetch_stock_data
from news_scraper.yahoo_news_scraper import get_yahoo_news_via_api
from sentiment_analysis.sentiment_classifier import classify_sentiment

def main():
    ticker = "AAPL"  # Or VNM, etc.
    
    print("Fetching stock data...")
    df = fetch_stock_data(ticker)
    print("Fetching latest news...")
    news = get_yahoo_news_via_api(ticker)
    for item in news:
        print(f"- {item['title']} ({item['time']})")
        print(f"  {item['url']}")
    for article in news:
        article['sentiment'] = classify_sentiment(article['title'])

    print("\nNews Sentiment Analysis:")
    for item in news:
        print(f"[{item['sentiment'].upper()}] {item['title']}")

if __name__ == "__main__":
    main()
    