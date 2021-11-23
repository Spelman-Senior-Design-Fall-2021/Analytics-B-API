from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')

# takes a string and returns one of 4 categories: negative, positive, neutral, and compound
sid = SentimentIntensityAnalyzer()

# class SentimentAnalysis():
#     def __init__(self, text):
#         self.polarity = sid.polarity_scores(text)

#     def getSentiment(self):
#         self.sent_message = "The article was rated as " + \
#             str(self.polarity['neg']*100) + "% NEGATIVE"
#         self.sent_message += "\nThe article was rated as " + \
#             str(self.polarity['neu']*100) + "% NEUTRAL"
#         self.sent_message += "\nThe article was rated as " + \
#             str(self.polarity['pos']*100) + "% POSITIVE"
#         self.sentiment = ''
#         if self.polarity['compound'] <= -0.05:
#             self.sentiment = "NEGATIVE"
#         elif self.polarity['compound'] > -0.05 and self.polarity['compound'] < 0.05:
#             self.sentiment = "NEUTRAL"
#         else:
#             self.sentiment = "POSITIVE"
#         self.sent_message += "\nThe article's overall sentiment is " + self.sentiment

#         return self.sent_message


def run(text):
    polarity = sid.polarity_scores(text)
    neg = polarity['neg']*100
    neu = polarity['neu']*100
    pos = polarity['pos']*100
    overall_sentiment = ''

    if polarity['compound'] <= -0.05:
        overall_sentiment = "negative"
    elif polarity['compound'] > -0.05 and polarity['compound'] < 0.05:
        overall_sentiment = "neutral"
    else:
        overall_sentiment = "positive"

    return {
        "neg": neg,
        "neu": neu,
        "pos": pos,
        "overall": overall_sentiment
    }
