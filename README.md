# stock
auto-warning-stock-system/

│

├── data/                        # Dữ liệu lưu trữ tạm thời

│   └── raw/                    # Dữ liệu gốc tải từ Yahoo Finance

│

├── news_scraper/

│   └── cafef_scraper.py        # Thu thập tin tức từ CafeF

│

├── llm_sentiment_labeler/

│   └── labeler.py              # Dùng LLM để gán nhãn sentiment

│

├── price_analysis/


│   ├── fetch_yahoo.py          # Lấy dữ liệu giá cổ phiếu từ Yahoo Finance

│   └── labeling.py             # Xử lý và gán nhãn tăng/giảm cho giá

│

├── models/
│   ├── trainer.py              # Huấn luyện mô hình dự đoán xu hướng
│   └── penalty_loss.py         # Hàm loss có penalize cú sốc
│
├── main.py                     # Chạy toàn bộ pipeline
├── requirements.txt
└── README.md
