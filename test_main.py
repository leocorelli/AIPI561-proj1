import pytest
from main import sentiment_analysis

def test_sentiment_analysis1():
    assert sentiment_analysis("I love you")[0] == pytest.approx({"label": "POSITIVE", "score": 0.9998656511306763})

def test_sentiment_analysis2():
    assert sentiment_analysis("I hate you")[0] == pytest.approx({"label": "NEGATIVE", "score": 0.9991129040718079})