from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import torch

from .config import SENTIMENT_POSITIVE_THRESHOLD, SENTIMENT_NEGATIVE_THRESHOLD

class SentimentAnalyzer:
    """
    Initialize a SentimentAnalyzer object.

    Args:
        model_name (str): The name of the pre-trained model to use for sentiment analysis.
            Defaults to "ProsusAI/finbert".

    Attributes:
        device (int): The device to use for sentiment analysis. 0 if CUDA is available, -1 otherwise.
        tokenizer (AutoTokenizer): The tokenizer to use for sentiment analysis.
        model (AutoModelForSequenceClassification): The pre-trained model to use for sentiment analysis.
        pipe (Pipeline): The pipeline to use for sentiment analysis.
        positive_threshold (float): The threshold above which a sentiment is considered positive.
        negative_threshold (float): The threshold below which a sentiment is considered negative.
    """
    def __init__(self, model_name: str = "ProsusAI/finbert"):
        self.device = 0 if torch.cuda.is_available() else -1
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)
        
        self.pipe = pipeline("text-classification", 
                             model=self.model,
                             tokenizer=self.tokenizer,
                             device=self.device)
        
        self.positive_threshold = SENTIMENT_POSITIVE_THRESHOLD
        self.negative_threshold = SENTIMENT_NEGATIVE_THRESHOLD
    
    def analyze(self, text: str) -> dict:
        result = self.pipe(text)[0]
        return {
            "label": result["label"].lower(),  # positive, negative, neutral
            "score": result["score"],
            "signal": self._get_signal(result)
        }
    
    def analyze_batch(self, texts: list[str]) -> list[dict]:
        results = self.pipe(texts, batch_size=16)
        return [
            {
                "label": r["label"].lower(),
                "score": r["score"],
                "signal": self._get_signal(r)
            }
            for r in results
        ]
    
    def _get_signal(self, result: dict) -> str:
        label = result["label"].lower()
        score = result["score"]
        
        if label == "positive" and score >= self.positive_threshold:
            return "BULLISH"
        elif label == "negative" and score >= self.negative_threshold:
            return "BEARISH"
        return "NEUTRAL"
    

if __name__ == "__main__":
    """
    Sample use case
    """
    analyzer = SentimentAnalyzer()
    sample_texts = [
        "The company's stock price soared after the successful product launch.",
        "Market uncertainty is causing investors to be cautious.",
        "Oracle Corp. has pushed back the completion dates for some of the data centers it’s developing for the artificial intelligence model developer OpenAI to 2028 from 2027, according to people familiar with the work. The delays are largely due to labor and material shortages, said the people, asking not to be identified discussing private schedules."
    ]

    for text in sample_texts:
        print(f"Text: {text}\nAnalysis: {analyzer.analyze(text)}\n")

    