from secret import api
import tweepy
import random

'''
    twoTwitter -
    Class that takes in the handles of two different twitter users and contains
    the first 3200 tweets on each of the timelines
'''
class twoTwitter:
    def __init__(self, user1, user2):
        self.user1 = user1
        self.user2 = user2
        self.tweets1 = self.getTweets(user1)
        self.tweets2 = self.getTweets(user2)
        self.counter = 0
        self.total = 0

    def getTweets(self, user):
        tweets = []
        for tweet in tweepy.Cursor(api.user_timeline,
            id=user,).items(3200):
            # ensure that our tweet is not a reply or retweet, and that there is
            # no mentions or links in the tweet
            if (('https' in tweet.text) or ('@' in tweet.text) or (tweet.retweeted) or (tweet.in_reply_to_user_id != None)):
                continue
            tweets.append(tweet.text)
        return tweets

    '''
        Generates a random tweet selected from either one of our twitter handles
    '''
    def getRandomTweet(self):
        # since we are not including all 3200 tweets (as there are bound to
        # be retweets, replies, etc. to remove) we need to take the min size from either
        # twitter handle.
        index1 = random.randint(0, len(self.tweets1))
        index2 = random.randint(0, len(self.tweets2))
        flip = random.randint(0, 1)
        return self.tweets2[index2-2] if flip == 1 else self.tweets1[index1-2]

    '''
        Checks if the user guessed the right handle. If yes, we increment a counter.
        Else, we print that it's incorrect and increase the total count
    '''
    def checkGuess(self, name, tweet):
        if tweet in self.tweets1:
            if name == self.user1:
                print('Guessed correctly!')
                self.counter += 1
            else :
                print('Incorrect guess :(')
        if tweet in self.tweets2:
            if name == self.user2:
                print('Guessed correctly!')
                self.counter += 1
            else :
                print('Incorrect guess :(')
        self.total += 1

    '''
        Prints out the player's statistics for the game
    '''
    def getStatistics(self):
        print(f"You guessed {self.counter} out of {self.total} tweets.")

    # for testing purposes only:
    # def getSizes(self) :
    #     print("size of 1st handle")
    #     print(f"{len(self.tweets1)}")
    #     print("size of 2nd handle")
    #     print(f"{len(self.tweets2)}")
