import pandas as pd
import numpy as np
import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from pandas import DataFrame

nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

# display df without truncate
pd.set_option('display.max_colwidth', None)

# dataframe preprocessing
class Preprocessing:

    def start_preprocessing(self, dataframe):
        self.__get_prediction_columns(dataframe)
        stopwords = nltk.corpus.stopwords.words("english")
        stopwords.extend(self.__get_list_of_stopwords)

        # remove stopwords
        for col in df.columns:
            df[col] = df[col].apply(lambda x: ' '.join([word for word in x.split() if word not in (stopwords)]))

        # lemmatization
        lemmatizer = WordNetLemmatizer()
        for col in df.columns:
            df[col] = df[col].apply(lambda x: ' '.join([lemmatizer.lemmatize(word) for word in x.split()]))

        # aggregate columns for heavy text clean
        df = df.astype(str).agg(' '.join, axis=1)

        # remove all non-alphanumeric characters
        df.replace(r'[^a-zA-Z]', ' ', regex=True, inplace=True)

        # remove single characters labels entries
        df = df.astype(str).apply(lambda x: ' '.join([w for w in x.split() if len(w)>1]))

        # remove uneccessary spaces
        df = df.astype(str).apply(lambda x: ' '.join(x.split()))

        # lower case
        df = df.astype(str).apply(lambda x: x.lower())

        # remove duplicates per row
        df = df.apply(lambda x: ' '.join(set(x.split())))



    def __get_prediction_columns(self, df):
        df[['Name', 'AT_MaraMatkl', 'AT_MaraMaktx', 'AT_MaraBrgew', 'AT_MaraMtart', 'AT_MaraLabor']]

    def __get_list_of_stopwords(self):
        return self.__get_list_of_nonpredicting_data

    def __get_list_of_nonpredicting_data(df: DataFrame):
        return []

