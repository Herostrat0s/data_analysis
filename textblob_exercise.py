import tweepy
from textblob import TextBlob

consumer_key = "KCHMmVuZaSOXDOnw2d6vJBRFv"
consumer_secret = "1d4AeZgkHhoyzQoK1VvNYziAIs5ed5aLwprFMUaTAqJ8djcMsz"

access_token = "1452717079296200707-dSGr5dFdz5D9mioXtBrYhEbh6yatSw"
access_token_secret = "qcY5lzxvitjoGNmLDxt92eztkxs0c4cRCyzNTWITUcpMW"

auth = tweepy.OAuth1UserHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search_tweets("Kudüs")

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)