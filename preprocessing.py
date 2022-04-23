import pandas as pd
import re
import string

def clean_text(row):
    # Lower case
    row = row.lower()

    # Remove URLs
    row = re.sub('http\S+|www.\S+', '', row)

    # Remove @mentions
    row = re.sub('@[A-Za-z0-9]+', '', row)

    # Remove non-standard characters
    row = row.encode("ascii", "ignore").decode()

    # Remove punctuation
    row = row.translate(str.maketrans('', '', string.punctuation))

    # Remove extraneous whitespace
    row = row.strip()

    # Split titles by words
    row = row.split()

    return row


def all_words_subreddit(df):
    """
    Iterates through the given data frame and returns tokenized versions of all
    post titles within a subreddit.
    """
    result = []
    columns = list(df)[1:]

    for subreddit in columns:
        row_length = len(df[subreddit])
        for i in range(row_length):
            post_title = df[subreddit][i]
            # print(post_title)
            result.append(clean_text(post_title))

    return result


df_popular = pd.read_csv('data/test_popular_data.csv')
df_curated = pd.read_csv('data/test_curated_data.csv')
all_words_popular = all_words_subreddit(df_popular)
all_words_curated = all_words_subreddit(df_curated)
