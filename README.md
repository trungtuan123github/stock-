# 📈 Auto-Warning Stock Price System

An automated pipeline to analyze stock prices and news sentiment, then generate buy/sell warnings based on combined signals.

---

## 🔁 Project Pipeline Overview

```mermaid
graph TD
    A[1. Fetch Stock Price Data (Yahoo Finance)] --> B[2. Analyze Price Signals]
    B --> C[3. Scrape News Articles (Yahoo Finance)]
    C --> D[4. Analyze News Sentiment]
    D --> E[5. Generate Warning (Buy / Sell / Hold)]

auto-warning-stock/
│
├── main.py                         # Entry point of the system
├── requirements.txt                # Python dependencies
│
├── price_analysis/
│   └── fetch_yahoo.py              # Fetch historical price data using yfinance
│
├── news_scraper/
│   └── yahoo_news_scraper.py      # Scrape news using Yahoo Finance
│
├── sentiment_analysis/
│   └── sentiment_predictor.py     # Predict sentiment using pretrained model
│
├── decision_engine/
│   └── warning_generator.py       # Generate trading warnings based on signals
│
└── utils/
    └── logger.py                  # Optional: Logging and helpers
