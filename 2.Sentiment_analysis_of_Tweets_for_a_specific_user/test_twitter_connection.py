# Import data (keys and tokens) from Twitter API to authorization
from credentials import *

import tweepy as tp


def twitter_api_connection():

    # Twitter API authorization process, using the keys and tokens
    auth = tp.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Return API with authentication:
    api = tp.API(auth)
    return api


test = twitter_api_connection()

# Download tweets from specific user:
twitter_user = "realDonaldTrump"
tweets = test.user_timeline(screen_name=twitter_user, count=1)

print("------- START -------")
for tweet in tweets:
    print(f"Collected {len(tweets)} Tweets from the {twitter_user}. \n")
    print(tweet.text)
print("------- THE END -------")




