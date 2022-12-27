import itertools
import snscrape.modules.twitter as sntwitter
import pandas as pd
from datetime import datetime

start_time = datetime.now()

num_tweets = 5
# Creating dataFrame storing tweets along the duration of the World Cup searching for "#coupedumonde"
data_tweets = pd.DataFrame(itertools.islice(sntwitter.TwitterSearchScraper('"#coupedumonde since:2022-11-20 until:2022-12-19"').get_items(),num_tweets))

end_time = datetime.now()

df_tweets = data_tweets[['date', 'id', 'content', 'retweetCount','likeCount','place','inReplyToTweetId',
                         'retweetedTweet','coordinates','lang']]
df_tweets.to_csv('tweets_coupedumonde.csv')

print('Duration: {}'.format(end_time - start_time))