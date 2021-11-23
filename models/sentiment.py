import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()#takes a string and returns one of 4 categories: negative, positive, neutral, and compound

class SentimentAnalysis():
    def __init__(self, text):
        self.polarity = sid.polarity_scores(text)
    def getSentiment(self):
        self.sent_message = "The article was rated as " + str(self.polarity['neg']*100) + "% NEGATIVE"
        self.sent_message += "\nThe article was rated as " + str(self.polarity['neu']*100) + "% NEUTRAL"
        self.sent_message += "\nThe article was rated as " + str(self.polarity['pos']*100) + "% POSITIVE"
        self.sentiment = ''
        if self.polarity['compound'] <= -0.05:
            self.sentiment = "NEGATIVE"
        elif self.polarity['compound'] > -0.05 and self.polarity['compound'] < 0.05:
            self.sentiment = "NEUTRAL"
        else:
            self.sentiment = "POSITIVE"
        self.sent_message += "\nThe article's overall sentiment is " + self.sentiment
        
        return self.sent_message

def run(clean_text):
    pass