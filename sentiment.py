"""
sentiment.py

Sentiment analysis module for the Reddit Marketing Intelligence
application.

This module uses the VADER sentiment analyzer to classify
public Reddit posts into Positive, Neutral, or Negative
sentiment.
"""

from typing import Dict

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


POSITIVE_THRESHOLD = 0.05
NEGATIVE_THRESHOLD = -0.05

analyzer = SentimentIntensityAnalyzer()


def analyze_sentiment(text: str) -> Dict:
    """
    Analyze the sentiment of input text.

    Parameters
    ----------
    text : str
        Input text.

    Returns
    -------
    dict
        Dictionary containing sentiment label and polarity scores.
    """

    if not text:
        return {
            "label": "Neutral",
            "compound": 0.0,
            "positive": 0.0,
            "neutral": 1.0,
            "negative": 0.0,
        }

    scores = analyzer.polarity_scores(text)

    compound = scores["compound"]

    if compound >= POSITIVE_THRESHOLD:
        label = "Positive"
    elif compound <= NEGATIVE_THRESHOLD:
        label = "Negative"
    else:
        label = "Neutral"

    return {
        "label": label,
        "compound": compound,
        "positive": scores["pos"],
        "neutral": scores["neu"],
        "negative": scores["neg"],
    }


if __name__ == "__main__":

    sample = (
        "Our migration to Kubernetes improved performance "
        "and reduced infrastructure costs."
    )

    result = analyze_sentiment(sample)

    print(result)