import itertools
import snscrape.modules.twitter as sntwitter
import pandas as pd
from datetime import datetime

start_time = datetime.now()

num_tweets = 10
# Creating dataFrame storing tweets along the duration of the World Cup searching for "cdm"
data_tweets = pd.DataFrame(itertools.islice(sntwitter.TwitterSearchScraper('cdm since:2022-11-20 until:2022-11-21').get_items(),num_tweets))

end_time = datetime.now()

df_tweets = data_tweets[['date', 'id', 'content', 'retweetCount','likeCount','place','inReplyToTweetId',
                         'retweetedTweet','coordinates','hashtags','lang']]
print((df_tweets[["inReplyToTweetId"]])

df_tweets.to_csv('tweets_cdm.csv')
print('Duration: {}'.format(end_time - start_time))