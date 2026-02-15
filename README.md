# Daily Stock News Sentiment Analyzer

A Python tool that fetches daily business news and analyzes sentiment using FinBERT to generate bullish/bearish trading signals.

## Latest Daily Stock News Data

JSON file updated ~every 3 hours with the most recent business/finance news headlines, sentiment analysis (via FinBERT), and bullish/bearish trading signals.

[![Latest News JSON](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2FTheephopWS%2Fdaily-stock-news%2Fmain%2Fdata%2Fdaily_news.json&query=$.last_updated&label=Last%20Updated&color=blue&cacheSeconds=10800&logo=json)](https://raw.githubusercontent.com/TheephopWS/daily-stock-news/main/data/daily_news.json)

**Direct link (always latest committed version):**

https://raw.githubusercontent.com/TheephopWS/daily-stock-news/main/data/daily_news.json

You can fetch it directly in code:

```js
// JavaScript (fetch latest data)
fetch('https://raw.githubusercontent.com/TheephopWS/daily-stock-news/main/data/daily_news.json')
  .then(r => r.json())
  .then(data => console.log(data));
```
```python
# Python (requests)
import requests
response = requests.get('https://raw.githubusercontent.com/TheephopWS/daily-stock-news/main/data/daily_news.json')
data = response.json()
print(data)
```

## Output

Results are saved to `data/daily_news.json`:

```json
[
    {
        "title": "Stock surges after earnings beat",
        "sentiment": "POSITIVE",
        "score": 0.9234,
        "signal": "BULLISH"
    }
]
```

## Requirements

- Python 3.10+
- CUDA (optional, for GPU acceleration)
