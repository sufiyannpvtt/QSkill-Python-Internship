from app.nlp.sentiment_engine import analyze_sentiment

def test_positive_sentiment():
    result = analyze_sentiment("This product is amazing")
    assert result["sentiment"] == "Positive"

def test_negative_sentiment():
    result = analyze_sentiment("This is the worst experience")
    assert result["sentiment"] == "Negative"

def test_neutral_sentiment():
    result = analyze_sentiment("It is okay")
    assert result["sentiment"] == "Neutral"
