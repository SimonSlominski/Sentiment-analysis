from textblob import TextBlob
from credentials import *
import tweepy as tp
import pandas as pd
import numpy as np
import re


def twitter_api_connection():

    # Twitter API authorization process, using the keys and tokens
    auth = tp.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Return API with authentication:
    api = tp.API(auth)
    return api


collect = twitter_api_connection()

# Download tweets from specific user:
twitter_user = "realDonaldTrump"
tweets = collect.user_timeline(screen_name=twitter_user, count=150)
print(f"Collected {len(tweets)} Tweets from the user {twitter_user}. \n")


# Create dataframe:
data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])


# Add additional info to dataframe
data['ID']      = np.array([tweet.id for tweet in tweets])
data['Date']    = np.array([tweet.created_at for tweet in tweets])
data['Source']  = np.array([tweet.source for tweet in tweets])
data['Likes']   = np.array([tweet.favorite_count for tweet in tweets])
data['RTs']     = np.array([tweet.retweet_count for tweet in tweets])
data['len']     = np.array([len(tweet.text) for tweet in tweets])


def clean_tweet(tweet):
    # Remove URLS from tweet.text
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())


def do_sentiment(tweet):
    # Specify polarity for every tweet

    analysis = TextBlob(clean_tweet(tweet))
    if analysis.sentiment.polarity > 0:
        return 1
    elif analysis.sentiment.polarity == 0:
        return 0
    else:
        return -1


# Add column with results to dataframe
data['SA'] = np.array([ do_sentiment(tweet) for tweet in data['Tweets'] ])

# We construct lists with classified tweets:
positive_tweets = [tweet for index, tweet in enumerate(data['Tweets']) if data['SA'][index] > 0]
neutral_tweets = [tweet for index, tweet in enumerate(data['Tweets']) if data['SA'][index] == 0]
negative_tweets = [tweet for index, tweet in enumerate(data['Tweets']) if data['SA'][index] < 0]

# Show the results of the analysis
print(f"Positive tweets: {round(len(positive_tweets)*100/len(data['Tweets']),2)}%")
print(f"Neutral tweets: {round(len(neutral_tweets)*100/len(data['Tweets']),2)}%")
print(f"Negative tweets: {round(len(negative_tweets)*100/len(data['Tweets']),2)}%")

