import json
import random
from snscrape.modules import twitter
import pandas as pd
from datetime import datetime
"""
This script collects specific infos from tweets related a search word and a date. The data is stored in a json file
It takes approximatively 43s to collect data about 100 tweets
Author: Lucie 
Created on: 2024-01-04
Updated on:
"""

# Get the time from which the code is launch
start_time = datetime.now()


tweets = []
# Enter the word or sentence you want to search for
search ='coupe du monde'
# Add the periode of time you want to search for
query = search + ' since:2022-11-14 until:2022-11-15'
# Enter the number of tweets you want to collect
max_results = 500000

# Scraping function for Twitter
def scrape_search(query):
    scraper = twitter.TwitterSearchScraper(query)
    return scraper

# Collecting valuable data about the tweets
scraper = scrape_search(query)
for i, tweet in enumerate(scraper.get_items()):
    if i > max_results:
        break;
    print(f'PROGRESSION : {i * 100 / max_results}%')
    tweet_json = json.loads(tweet.json())

    tweets.append([tweet_json['date'], tweet.content, tweet.id, tweet.user.username, tweet.user.id, tweet.user.verified,tweet.user.followersCount, tweet.user.friendsCount, tweet.user.favouritesCount,
                   tweet.user.location, tweet.replyCount, tweet.retweetCount, tweet.quoteCount, tweet.lang, tweet.retweetedTweet, str(tweet.inReplyToTweetId),tweet.hashtags])
    if tweet.inReplyToUser is not None:
        tweets[-1].append(tweet.inReplyToUser.username)
    else:
        tweets[-1].append('no data')

    if tweet.place is not None:
        tweets[-1].append(tweet.place.fullName)
    else:
        tweets[-1].append('no data')

# Storing data in a dataFrame
tweets_df1 = pd.DataFrame(tweets, columns=['Datetime','Text','TweetId','Username','UserId','IfVerified','FollowerCount','FriendsCount','FavouritesCount','UserLocation',
                                         'replyCount', 'retweetCount', 'quoteCount', 'lang', 'IfretweetedTweet','inReplyToTweetId','hashtags','InReplyToUserUsername','place'])

# Create a file name in order not to overwrite
file = search + str(random.randint(1,500))
# Convert the dataFrame into a json file
tweets_df1.to_json(f'{file}.json')

# Get end of the code time
end_time = datetime.now()
# Print duration execution
print(end_time-start_time)