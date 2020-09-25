from secret import api
from player import *


if __name__ == "__main__":
    print('Welcome to the tweet guessing game!')
    user1 = input('Please enter the twitter handle of the first user: @')
    user2 = input('Please enter the twitter handle of the second user: @')
    print('Loading your game...')
    object = twoTwitter(user1, user2)
    #object.getSizes()
    while True:
        print('Reshuffling tweets...')
        # getting a random tweet
        currTweet = object.getRandomTweet()
        # asking for user input now
        print(f"The current tweet is: \n{currTweet}\nWho do you think tweeted this?")
        guess = input('Please enter your guess: @')
        object.checkGuess(guess, currTweet)
        if (input('Would you like to check your current score? Type Y/N: ') == 'Y'):
            object.getStatistics()
        else :
            print('Understandable, have a nice day')
