from collections import Counter
from pandas import DataFrame
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from app.fetcher import DataLoader


class TextProcessing:

    def __init__(self, df: DataFrame):
        nltk.download('vader_lexicon')
        self.df = df.copy()

    @staticmethod
    def _rarest_word_in_text(text):
        words = text.split()
        counts = Counter(words)
        min_shows = min(counts.values())
        for w in words:
            if counts[w] == min_shows:
                return w

    @staticmethod
    def _sentiment_of_text(text):
        score = SentimentIntensityAnalyzer().polarity_scores(text)
        if score['compound'] >= 0.5:
            return 'positive'
        elif score['compound'] >= -0.49:
            return "neutral"
        else:
            return "negative"

    def rarest_word(self):
        self.df['rarest_word'] = self.df['Text'].apply(TextProcessing._rarest_word_in_text)
        return self

    def sentiment(self):
        self.df['sentiment'] = self.df['Text'].apply(TextProcessing._sentiment_of_text)
        return self

if __name__ == '__main__':
    d = DataLoader()
    c = d.get_data()
    t = TextProcessing(DataFrame(c))
    print(t.sentiment().df)




