from collections import Counter
from pandas import DataFrame



class TextProcessing:

    def __init__(self, df: DataFrame):

        self.df = df.copy()

    @staticmethod
    def rarest_word_in_row(text):
        words = text.split()
        counts = Counter(words)
        min_freq = min(counts.values())
        for w in words:
            if counts[w] == min_freq:
                return w

    def word_rarest(self):
        self.df['rarest_word'] = self.df['Text'].apply(TextProcessing.rarest_word_in_row)
        return self




