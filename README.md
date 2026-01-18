# Daily Stock News Sentiment Analyzer

A Python tool that fetches daily business news and analyzes sentiment using FinBERT to generate bullish/bearish trading signals.

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure API Key

Create a `.env` file in the project root:

```env
NEWSAPI_KEY=your_newsapi_key_here
```

Get your free API key at [newsapi.org](https://newsapi.org/register)

## Usage

### Run via Python

```bash
python main.py
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
