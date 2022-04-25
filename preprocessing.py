import pandas as pd
import copy as cp
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

def remove_duplicates(data_dict, columns):
    """
    Remove duplicate entries in the values of keys for data_dict, then writes
    the new dataframe to a new CSV file

    dict_data is the dict to store data to
    """
    # Initialize dicts
    result_dict = {}
    for name in columns:
        result_dict[name] = []
    
    for key in data_dict:
        lst = data_dict[key]
        result_lst = []
        more_count_lst = []
        for element in lst:
            if element not in result_lst:
                result_lst.append(element)
        
        result_dict[key] = result_lst

    store_as_pandas(result_dict, columns, 'deduplicated_curated_extreme_data3')


df_extreme_curated2 = pd.read_csv('curated_extreme_data3.csv')
columns = list(df_extreme_curated2)[1:]
print(columns)
remove_duplicates(df_extreme_curated2, columns)


# # df preprocessing, not useful anymore
# df_extreme_curated = pd.read_csv('data/curated_extreme_data.csv')
# all_words_extreme_curated = all_words_subreddit(df_extreme_curated)

# df_popular = pd.read_csv('data/test_popular_data.csv')
# df_curated = pd.read_csv('data/test_curated_data.csv')
# all_words_popular = all_words_subreddit(df_popular)
# all_words_curated = all_words_subreddit(df_curated)
# f = open("test_list.txt", "a")
# f.write(f'{all_words_extreme_curated}')
# f.close()