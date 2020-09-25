import tweepy


consumer_key= '{YOUR_KEY}'
consumer_secret= '{YOUR_SECRET}'
access_token= '{YOUR_TOKEN}'
access_token_secret= '{YOUR_TOKEN_SECRET}'


# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key,
    consumer_secret)
auth.set_access_token(access_token,
    access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")
