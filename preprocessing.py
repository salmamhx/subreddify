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
    
    Data structure for words are:
        all_words = [title1, title2, ..., title]
        title = [list of words, subreddit]
        list of words = [word1, word2, ..., word]
    """
    result = []
    columns = list(df)[1:]

    for subreddit in columns:
        row_length = len(df[subreddit])
        for i in range(row_length):
            post_title = str(df[subreddit][i])
            if post_title == 'nan':
                result.append([[''], ''])
            else:
                result.append([clean_text(post_title), subreddit])

    return result


# df_popular = pd.read_csv('data/test_popular_data.csv')
# df_curated = pd.read_csv('data/test_curated_data.csv')
df_extreme_curated = pd.read_csv('data/curated_extreme_data.csv')
# all_words_popular = all_words_subreddit(df_popular)
# all_words_curated = all_words_subreddit(df_curated)
all_words_extreme_curated = all_words_subreddit(df_extreme_curated)
f = open("test_list.txt", "a")
f.write(f'{all_words_extreme_curated}')
f.close()