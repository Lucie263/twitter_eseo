# import the module
import tweepy

# assign the values accordingly
consumer_key = "IrtXzq2QhmcXT2J9AlfMEMoN2"
consumer_secret = "8HQPL5xNN6cmqH7668vrBegOZA97tnl5CYSGm1RxcVvWJS0V2L"
access_token = "1605165130660159490-qcX01YaB3DbLfhlcwPDvJGbABCHu60"
access_token_secret = "SR9ng3Bmcvx4dw5mOaoD7rGNvbzTjLpjQ44E79kvJPBeB"

# authorization of consumer key and consumer secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# set access to user's access key and access secret
auth.set_access_token(access_token, access_token_secret)

# calling the api
api = tweepy.API(auth)

my_query = '#cdm OR #coupedumonde'
date_since = "202211200000"
date_to = "202212200000"
numTweets = 10

# premium search
tweets= api.search_tweets(q=my_query, fromDate=date_since, toDate=date_to, maxResults=numTweets)

print(tweets)