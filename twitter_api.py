import tweepy
import  configparser

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']
access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

auth = tweepy.OAuthHandler(api_key,api_key_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

my_query = '#cdm OR #coupedumonde'
date_since = "202211200000"
date_to = "202212200000"
numTweets = 10

# premium search
tweets= api.search_full_archive(label='eseo', query=my_query, fromDate=date_since, toDate=date_to, maxResults=numTweets)

print(tweets)