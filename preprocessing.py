# import libraries
# import pandas as pd
# import csv
# from sklearn.feature_extraction.text import CountVectorizer
# import subreddit_apis

# list of each subreddit, either popular or curated
# popular = ['askreddit', 'worldnews', 'funny', 'gaming', 'news', 'movies', 'tifu', 'mildlyinteresting', 'explainlikeimfive', 'pics', 'todayilearned', 'jokes', 'aww', 'videos', 'lifeprotips', 'twoxchromosomes', 'oldschoolcool', 'art', 'dataisbeautiful', 'amitheasshole', ]
# curated = ['askreddit', 'news', 'gaming', 'movies', 'tifu', 'amitheasshole', 'todayilearned', 'lifeprotips', 'oldschoolcool', 'dataisbeautiful', 'explainlikeimfive', 'mildlyinteresting', 'aww', 'twoxchromosomes', 'wallstreetbets', 'politics', 'cornell', 'technews']

# list of post titles for each subreddit
# titles = {
#     'title1',
#     'title2'
# }

import pandas as pd
import string

PUNCTUATIONS = [string.punctuation[i] for i in range(len(string.punctuation))]
df = pandas.read_csv('data/test_popular_data.csv')
print(df)

def preprocess(title):
    """
    Converts a string into a list of strings corresponding to each word. For
    example: "Hello world!" becomes ['Hello', 'world', '!']
    """
    result = title.split()
    
    for word in result:
        for punctuation in PUNCTUATIONS:
            if punctuation in word:
                i = result.index(word)
                before_result = result[:i]
                after_result = result[i+1:]

                # tmp_result is a list of just this word: eg. the 'as!sss' becomes
                # ['a', 's', '!'];
                i = word.index(punctuation)
                before_word = word[:i]
                after_word = word[i+1:]
                word_list = filter(None, [before_word] + [punctuation] + [after_word])
                
                result = before_result + word_list + after_result
        
        # result = ['Hello', 'world!']
        # result = ['world', '!']
    
    return result

# Iterate through all post titles in data
all_words_popular = []
all_words_curated = []

for subreddit in popular:
    for title in subreddit:
        all_words_popular.append(preprocess(title))

for subreddit in curated:
    for title in subreddit:
        all_words_curated.append(preprocess(title))
            
print(all_words_popular)
            
# df = pd.read_csv('popular_data.csv', usecols=subreddits)

# # create vectorizer, extracting stop words
# vectorizer = CountVectorizer(stop_words='english')

# vectorizer.fit_transform(subreddit_apis.curated_dict).toArray()
# vectorizer.fit_transform(subreddit_apis.popular_dict).toArray()

# # gets each word in the titles
# vectorizer.fit(titles)

# # gets dictionary of above words
# vectorizer.get_feature_names()

# # each title is transformed to a vector space
# vector = vectorizer.transform(titles)
# vector_spaces = vector.toarray()
# # vector_spaces

# # sentences with their respective vector space representations
# for t, v in zip(titles, vector_spaces):
#     print(t)
#     print(v)