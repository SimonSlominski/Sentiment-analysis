# Sentiment analysis of Tweets for a specific user

## Overview:
To conduct sentiment analysis, perform the following steps:
1. Collect twitter data
2. Do sentiment analysis
3. Do statistics and data visualization (optionally)

### Requirements:
- Python 3.7
- NumPy
- Pandas
- Tweepy
- Textblob

### STEP 1 - Data Collection

**1.1 Create a Twitter app**

You have to create a new Twitter App. You can do it by adding new app in your Twitter account: https://developer.twitter.com. 
After that click on the "Keys and tokens" and copy that. That's it for now!

**1.2 Twitter Configuration File**

*Files: credentials.py*

In project directory create credentials.py and put there data (keys and tokens) from your Twitter app. 

- consumer_key = "your consumer key"
- consumer_secret = "your consumer secret"
- access_token = "your access token"
- access_token_secret = "your access token secret"

**1.3 Test Twitter API connection**

*Files: test_twitter_connection.py

Before we'll get further, let's test and check our conection with Twitter App. To conduct test just run the test_twitter_connection.py script. 

If everything works you will see the text of tweet from twitter_user (default = realDonalTrump).

If you get authentication errors, check your keys and tokens in the credentials file. 

**1.4 Download Tweets**

*Files: doAnalysis.py

After creating function 'twitter_api_connection', its time to download some tweets. To do this you have to pick a username (for instance, I've chosen Donald Trump to check if the sentiment of his tweets is similar to his behavior).

Then put your username to the variable called 'twitter_user'. Default count number of downloading tweets is 150. 


### STEP 2 - Creating DataFrame with Pandas

With this line of code we could create a basic dataframe with collected Tweets:

`data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])`

In this case, we have only 'Tweet.text'. But we can add some data to created dataframe. 

If you use this code: `print(dir(tweets[0]))` you will see all the elements you can fetch. For me the most important was:
- ID: id
- Date: created at
- Source: info about source
- Likes: number of likes
- RTs: number of retweets
- len: length of a tweet


### STEP 3 - Sentiment analysis

Textblob allows us to do sentiment analysis with ease. Textblob checks every tweet and sets polarity accordingly:
- Positive >0
- Neutral =0
- Negative <0

Consequently, we'll get an extra column which contains the sentiment analysis result. 

### STEP 4 - Results

In the end, we would like to know the percentage structure of results. To verify the results, we will count the number for each group and determine the percentages.

Results:
- Positive tweets: 47.33%
- Neutral tweets: 31.33%
- Negative tweets: 21.33%

Keep in mind that your results could be different. It depends on the set of tweets. (Last updated: January 16th, 2019.)





