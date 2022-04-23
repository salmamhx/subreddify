import pandas as pd
import csv
import sklearn.feature_extraction

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS

subreddits = ["askreddit","worldnews", "funny", "gaming", "news", "movies", "tifu", "mildlyinteresting", "explainlikeimfive", "pics", "todayilearned", "jokes", "aww", "videos", "lifeprotips", "twoxchromosomes", "oldschoolcool", "art", "dataisbeautiful", "amitheasshole"]
df = pd.read_csv('popular_data.csv', usecols=subreddits)

print(df["worldnews"]) #example print

sentences = {
    "My sample sentence."
}

vectorizor = CountVectorizer(stop_words=ENGLISH_STOP_WORDS)

# vectorizor.fit(sentences)
# vectorizor.get_feature_names()

##

vector = vectorizor.transform(sentences)
vector_spaces = vector.toarray()

vector_spaces

##

for i, v in zip(sentences, vector_spaces):
    print(i)
    print(v)