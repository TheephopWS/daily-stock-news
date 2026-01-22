# Daily Stock News Sentiment Analyzer

A Python tool that fetches daily business news and analyzes sentiment using FinBERT to generate bullish/bearish trading signals.

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
