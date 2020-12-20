import sys
import tweepy
from textblob import TextBlob


# your Twitter app credentials
consumer_key = "ZGv6D6GfBLDUCvPiqTPqrzj2w"
consumer_secret = "ietfliI2HN7wtViJGqdKqa6W1b2Rpjauf1PX0YtKstY5uCRwDj"
access_token = "1103867661845356544-GCcPrMPz9skmb4Pc2EwpT7x08VTQIh"
access_token_secret = "8qmqClPKEVfZr6eAWqOnlIy0GCmQxPNDZP5sYFaitk7C8"

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