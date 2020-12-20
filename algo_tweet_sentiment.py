import sys
import tweepy
from textblob import TextBlob


# your Twitter app credentials


keyword = (sys.argv[1])

# -----------------------------------
if __name__ == "__main__":
    # twitter authentication
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    twitter_api = tweepy.API(auth)

    # get latest 100 tweets containing the phrase $SPX
    tweets = twitter_api.search(keyword, count=1000)

    # parse sentiment
    valid = 0 # counter for tweets with a determined sentiment
    positive = 0 # counter for positive tweets

    for tweet in tweets:
        text = TextBlob(tweet.text).sentiment
        if text.subjectivity != 0:
            
            valid += 1
            positive += (text.polarity > 0)

    # sentiment ratio
    sentiment = positive / valid

    # construct tweet
    tweet = "Tweet Sentiment for %s is %.2f%%" % (keyword, (sentiment * 100))

    # to actually tweet, uncomment this line:
    # twitter_api.update_status(status=tweet)

    # for now, just print out the tweet
    print(tweet)