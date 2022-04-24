"""
ndas.read_csv()
This program collects Reddit posts from ten subreddits and stores the data in
JSON format in a specified file.
"""

import copy as cp
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

curated_extreme = ['amitheasshole', 'todayilearned', 'explainlikeimfive', 'news', 'askreddit', 'cornell']

# A dict where keys are strings (subreddit names) and values are a list of post titles
popular_dict = {}
curated_dict = {}
curated_extreme_dict = {}

def add_to_dict(subreddit_name, dict_data, num):
    """
    Function that adds posts of a given subreddit to a dict

    Parameters
        subreddit_name is the subreddit name
        dict_data is the dict to store data to
        limit is how many posts to scrape per subreddit
    """
    for submission in reddit.subreddit(subreddit_name).top("all", limit=num):
        dict_data[subreddit_name].append(submission.title)

def store_as_pandas(dict_data, column_names, file_name):
    """
    Function that stores dict_data as a pandas dataframe and saves to a csv file

    Parameters
        dict_data is the dict to store data to
        column_names is a list of column names
        file_name is the file name of the CSV to store to
    """
    # Make a copy of dict_data to avoid overwriting the original
    copy_dict = cp.deepcopy(dict_data)
    
    # Find the max column length
    max_length = 0
    for key in column_names:
        column_length = len(copy_dict[key])
        max_length = max(column_length, max_length)
    
    # Add 'NaN' values to each key in data_dict until every key has the same
    # number of entries
    for key in column_names:
        column_length = len(copy_dict[key])
        while column_length < max_length:
            copy_dict[key].append('NaN')
            column_length += 1

    df = pd.DataFrame(copy_dict, columns = column_names)
    df.to_csv(f'{file_name}.csv')

# Generate keys with empty lists for both dicts
for name in popular:
    popular_dict[name] = []
for name in curated:
    curated_dict[name] = []
for name in curated_extreme:
    curated_extreme_dict[name] = []

# Add data to dicts
# for i in range(len(popular)):
#     add_to_dict(popular[i], popular_dict, 100)
#     print(f'Popular: Added column {popular[i]}')
# for i in range(len(curated)):
#     add_to_dict(curated[i], curated_dict, 100)
#     print(f'Curated: Added column {curated[i]}')
for i in range(len(curated_extreme)):
    add_to_dict(curated_extreme[i], curated_extreme_dict, 1000)
    print(f'Extreme Curated: Added column {curated_extreme[i]}')

# Store data in CSV files
# store_as_pandas(popular_dict, popular, 'popular_data')
# store_as_pandas(curated_dict, curated, 'curated_data')
store_as_pandas(curated_extreme_dict, curated_extreme, 'curated_extreme_data')