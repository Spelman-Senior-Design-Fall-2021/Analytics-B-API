import tensorflow.keras  # needs to be imported
from tensorflow.keras import models  # using a keras model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras import preprocessing
from tensorflow.keras import metrics
#from tensorflow.keras.metrics import Accuracy
import numpy as np
import os  # fixes tensorflow error
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # fixes tensorflow error

# infile = open("test_text/liberal.txt")  # open text file
# infile = infile.read()  # put text file into a string
# string_output = infile
# print(string_output)#print string

political_model = models.load_model(
    'PoliticalSentiment.h5')  # load keras model

# create class that takes clean text as a parameter


class PoliticalBias():
    def __init__(self, text):
        self.text = text  # clean text
        self.data = np.asarray(self.preprocessData(text)).astype(
            'float32')  # call preprocess method

    def preprocessData(self, string):
        string = [string]  # put string into list
        max_features = 50000
        max_length = 500  # length into data
        tokenizer = Tokenizer(num_words=50000)  # splitting up text
        # creating vocabulary from word frequency
        tokenizer.fit_on_texts(string)
        # replaces next with corresponding word index
        tokens = tokenizer.texts_to_sequences(string)
        # making sure the sequences have equal lengths
        return preprocessing.sequence.pad_sequences(tokens, max_length)

    def pred(self):
        self.prediction = political_model.predict(self.data)[0][0]
        self.prediction_str = ''
        if self.prediction >= 0 and self.prediction <= .2:
            # highest conservative score if from 0-.2
            self.prediction_str = 'Super Conservative'
        elif self.prediction > .2 and self.prediction < .4:
            # lowest conservative score if from .2-.4
            self.prediction_str = 'Moderately Conservative'
        elif self.prediction >= .4 and self.prediction <= .6:
            self.prediction_str = 'Moderate'  # neutral score if from .4-.6
        elif self.prediction > .6 and self.prediction < .8:
            self.prediction_str = 'Moderately Liberal'  # less liberal if from .6-.8
        else:
            self.prediction_str = 'Super Liberal'  # highest liberal if .8+
        # return the string to UI
        return {"percentage": self.prediction * 100,
                "label": self.prediction_str}

# prediction = PoliticalBias(string_output) #create object
# print(prediction.pred())#prints out 81.30% Super Liberal


def run(data):
    results = []

    for clean_text in data:
        prediction = PoliticalBias(clean_text)
        results.append(prediction.pred())

    return results
