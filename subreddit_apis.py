"""
This program collects Reddit posts from ten subreddits and stores the data in
JSON format in a specified file.
"""

import pandas as pd
import praw
import os
from dotenv import load_dotenv

load_dotenv()

reddit = praw.Reddit(
    client_id = os.getenv('CLIENT_ID'),
    client_secret = os.getenv('CLIENT_SECRET'),
    user_agent = 'script',
)

# List of popular subreddits to scrape
popular = ['askreddit', 'worldnews', 'funny', 'gaming', 'news', 'movies', 'tifu', 'mildlyinteresting', 'explainlikeimfive', 'pics',
           'todayilearned', 'jokes', 'aww', 'videos', 'lifeprotips', 'twoxchromosomes', 'oldschoolcool', 'art', 'dataisbeautiful', 'amitheasshole', ]
# List of curated subreddits to scrape
curated = ['askreddit', 'news', 'gaming', 'movies', 'tifu', 'amitheasshole', 'todayilearned', 'lifeprotips', 'oldschoolcool', 'dataisbeautiful',
           'explainlikeimfive', 'mildlyinteresting', 'aww', 'twoxchromosomes', 'wallstreetbets', 'politics', 'cornell', 'technews']

# A dict where keys are strings (subreddit names) and values are a list of post titles
popular_dict = {}
curated_dict = {}

def add_to_dict(subreddit_name, dict_data):
    """
    Function that adds posts of a given subreddit to a dict

    Parameters
        subreddit_name is the subreddit name
        dict_data is the dict to store data to
    """
    for submission in reddit.subreddit(subreddit_name).top("month", limit=100):
        dict_data[subreddit_name].append(submission.title)

def store_as_pandas(dict_data, column_names, file_name):
    """
    Function that stores dict_data as a pandas dataframe and saves to a csv file

    Parameters
        dict_data is the dict to store data to
        column_names is a list of column names
        file_name is the file name of the CSV to store to
    """
    df = pd.DataFrame(dict_data, columns = column_names)
    df.to_csv(f'{file_name}.csv')

# Generate keys with empty lists for both dicts
for name in popular:
    popular_dict[name] = []
for name in curated:
    curated_dict[name] = []

# Add data to dicts
for i in range(len(popular)):
    add_to_dict(popular[i], popular_dict)
    print(f'Popular: Added column {popular[i]}')
for i in range(len(curated)):
    add_to_dict(curated[i], curated_dict)
    print(f'Curated: Added column {popular[i]}')

# Store data in CSV files
store_as_pandas(popular_dict, popular, 'popular_data')
store_as_pandas(curated_dict, curated, 'curated_data')