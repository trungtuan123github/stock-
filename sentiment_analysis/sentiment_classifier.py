import google.generativeai as genai
import os
import os
import requests

GEMINI_API_KEY = "AIzaSyBxz9OzH-TW6m0KHLMX_jtSTL3XWPzY5s0"

def classify_sentiment(title):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"

    headers = {
        "Content-Type": "application/json"
    }

    prompt = f"""Bạn là một nhà phân tích tài chính. Dự đoán cảm xúc của tiêu đề sau là 'positive', 'negative', hay 'neutral'?

Tiêu đề: "{title}"

Chỉ trả lời đúng một từ: positive, negative, hoặc neutral."""

    data = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()

        text = result['candidates'][0]['content']['parts'][0]['text'].strip().lower()

        if text in ['positive', 'negative', 'neutral']:
            return text
        else:
            return 'neutral'
    except Exception as e:
        print("Gemini API Error:", e)
        return 'neutral'
