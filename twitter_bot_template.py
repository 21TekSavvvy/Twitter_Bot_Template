import tweepy


consumer_key = #Enter your twitter consumer_key
consumer_secret = #Enter your twitter consumer_secret key
access_token = #Enter your twitter access_token
access_token_secret = #Enter your twitter access_token_secret


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token( access_token,access_token_secret)


api = tweepy.API(auth, wait_on_rate_limit=True)
# verify if your api works
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")



def timelineDisplay():
    timeline = api.home_timeline()
    for tweet in timeline:
        print(f"{tweet.user.name} said {tweet.text}")

def followBack():
    for follower in api.get_followers():
        follower.follow()
    print("Followed everyone that is following " )

def updateStatus():
    inputstr = input("Enter whatever you feel like tweeting: ")
    api.update_status(inputstr)
    print("Posted")

def updateProfile():
    print("Profile Menu")
    print("1. Update Name")
    print("2. Update Website links")
    print("3. Update Description")
    print("4. Location")

    pInput = int(input("Enter 1-4: "))
    while (pInput>0 and pInput <5 ):

        if pInput == 1:
            nInput = input("Enter your full name: ")
            api.update_profile(name = nInput)
        elif pInput == 2:
            urlInput = input("Enter your Website url starting with https:// :  ")
            api.update_profile(url = urlInput)
        elif pInput == 3:
            desInput = input("Enter your profile description: ")
            api.update_profile(description = desInput)
        elif pInput == 4:
            locInput = input("Enter your Location: ")
            api.update_profile(location = locInput)
        pInput = int(input("Enter 1-4: "))
    menu()

def retweetWithSearchByKeywords():
    search = input("Enter a keyword to search: ")
    numTweets = int(input("Enter the amount of tweets you want to retweet (0-10times): "))

    for tweet in  tweepy.Cursor(api.search_tweets, q = search).items(numTweets):
        try:

            tweetID = tweet.id

            #verify if the tweet has been retweeted already
            status = api.get_status(tweetID)
            retweeted = status.retweeted
            #retweet if tweets hasn't been retweeted yet, or skip tweet
            if retweeted == False:
                api.retweet(tweetID)
            else:
                continue
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break



        print("Retweeted!")

def retweetWithSearchByUser():
    username = input("Enter a username to search (add @ before the name): ")
    numTweets = int(input("Enter the amount of tweets per page you want to retweet(0-10 times): "))

    userFound = api.get_user(screen_name = username)

    for tweet in api.user_timeline(screen_name = userFound.screen_name,count = numTweets, exclude_replies = True):
        try:
            tweetID = tweet.id


            #verify if the tweet has been retweeted already
            status = api.get_status(tweetID)
            retweeted = status.retweeted
            #retweet if tweets hasn't been retweeted yet, or skip tweet
            if retweeted == False:
                api.retweet(tweetID)
            else:
                continue

        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break


        print("Retweeted!")

def likeWithSearchByUser():
    username = input("Enter a username to search (no @ sign): ")
    numTweets = int(input("Enter the amount of tweets per page you want to like on their timeline(0-10): "))

    userFound = api.get_user(screen_name = username)
    user_tweets = api.user_timeline(screen_name = userFound.screen_name,count = numTweets, exclude_replies = True)
    for tweet in user_tweets:
        try:
            tweetID = tweet.id
            #verify if the tweet has been Liked already
            status = api.get_status(tweetID)
            favorited = status.favorited
            #retweet if tweets hasn't been Liked yet, or skip tweet
            if favorited == False:
                api.create_favorite(tweetID)
            else:
                continue


        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break


        print("Liked!")

def likeWithSearchByKeywords():
    keyword = input("Enter a keyword to search: ")
    numTweets = int(input("Enter the amount of tweets you want to like on their timeline(0-10 times): "))

    for tweet in tweepy.Cursor(api.search_tweets, q = keyword).items(numTweets):
        try:
            tweetID = tweet.id
            #verify if the tweet has been Liked already
            status = api.get_status(tweetID)
            favorited = status.favorited
            #retweet if tweets hasn't been Liked yet, or skip tweet
            if favorited == False:
                api.create_favorite(tweetID)
            else:
                continue

        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break


        print("Liked!")

def followByUsername():


    username = input("Enter a username to search (no @ sign): ")
    userFound = api.get_user(screen_name = username)
    try:
        api.create_friendship(screen_name = userFound.screen_name)

    except tweepy.TweepError as e:
        print(e.reason)

    print ("Followed!")


def unfollowByUsername():

    username = input("Enter a username to search (no @ sign): ")
    userFound = api.get_user(screen_name = username)
    try:
        api.destroy_friendship(screen_name = userFound.screen_name)

    except tweepy.TweepError as e:
        print(e.reason)

    print ("Unfollowed!")

def menu():
    print('Menu')
    print("0.Exit")
    print("1. Tweet")
    print("2. Retweet feed by searching with keyword")
    print("3. Retweet User's feed by searching with username")
    print("4. Like feed by searching with keyword")
    print("5. Like User's feed by searching with username")
    print("6. Update Profile Settings")
    print("7. Follow users by searching their username")
    print("8. Unfollow users by searching their username")
    print("9. Follow Back everyone who is currently following you")
    print("10. Print Home Timeline")

    mInput = int(input("Enter your Choice: "))
    while (mInput>0 and mInput <11 ):
        if mInput == 1:
            updateStatus()
        elif mInput == 2:
            retweetWithSearchByKeywords()
        elif mInput == 3:
            retweetWithSearchByUser()
        elif mInput == 4:
            likeWithSearchByKeywords()
        elif mInput == 5:
            likeWithSearchByUser()
        elif mInput == 6:
            updateProfile()
        elif mInput == 7:
            followByUsername()
        elif mInput == 8:
            unfollowByUsername()
        elif mInput == 9:
            followBack()
        elif mInput == 10:
            timelineDisplay()
        else:
            break
        mInput = int(input("Enter your Choice: "))






if __name__ == '__main__':
    menu()
