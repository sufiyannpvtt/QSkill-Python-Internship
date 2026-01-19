from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text: str) -> dict:
    if not text or not text.strip():
        return {
            "sentiment": "Neutral",
            "polarity": 0.0,
            "confidence": 0,
            "emoji": "😐"
        }

    scores = analyzer.polarity_scores(text)
    compound = scores["compound"]

    if compound >= 0.05:
        sentiment = "Positive"
        emoji = "😊"
    elif compound <= -0.05:
        sentiment = "Negative"
        emoji = "😞"
    else:
        sentiment = "Neutral"
        emoji = "😐"

    confidence = int(abs(compound) * 100)
    confidence = max(40, min(confidence, 95))

    return {
        "sentiment": sentiment,
        "polarity": round(compound, 3),
        "confidence": confidence,
        "emoji": emoji
    }
