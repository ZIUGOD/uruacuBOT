import tweepy
import pygame
from time import sleep
from botFunctions import * # a separate file with the whole functions and the class used in code
from botConfig import *    # a private file with the unique bot informations that can't be shared(apiKey, secretKey, bearerToken, etc...).

pygame.init()
clear()
print("Starting...")

client = tweepy.Client(bearerToken)
auth   = tweepy.OAuthHandler(apiKey, apiSecretKey)
api    = tweepy.API(auth, wait_on_rate_limit=True)
count  = 0
query  = 'Uruacu OR Uruaçu OR uruacu OR uruaçu'

auth.set_access_token(accessToken, accessSecretToken)

try:
    api.verify_credentials()
    print(bColors.GREEN + "Authentication OK!\n" + bColors.END)
except:
    print(bColors.FAIL + "Error during the authentication.\n" + bColors.END)

client = tweepy.Client
data   = api.rate_limit_status()

while True: # infinite loop that make the bot works
    count  = count + 1
    found  = False
    search = tweepy.Cursor(api.search_tweets, q=query, result_type="recent").items(25)

    print("Starting a new search: \n" + bColors.GREEN +
         f"{count}° try...\n" + bColors.END)
    sleep(1)

    for tweet in search:
        try:
            api.retweet(tweet.id)
            api.create_favorite(tweet.id)

            pygame.mixer.music.load('notificationSound.mp3')
            pygame.mixer.music.play()

            print(f"> " + bColors.CYAN + f"@UruacuBOT " + bColors.END + "found a Tweet by " 
                + bColors.CYAN + f"@{tweet.user.screen_name}" + bColors.END + 
                  f":\n{str(tweet.text)}\n" + bColors.GREEN +
                  f"Tweet {tweet.id} retweeted and favorited!\n" + bColors.END)

            count = 0
            found = True

            if tweet.user.screen_name == "glycosta":
                print("\nMaior fã de Uruaçu " + bColors.FAIL + "♥ ♥ ♥\n" + bColors.END)
            elif tweet.user.screen_name == "ZIUGOD":
                print("\nMeu criadoooorr " + bColors.FAIL + "♥ ♥ ♥\n" + bColors.END)

            waitTime(900) # 15 minutes
            break
        except Exception as e:
            pass
    
    if found == False:
        print(bColors.CYAN + f"@UruacuBOT " + bColors.END + f"made the {count}° try and found nothing.\n")
        waitTime(30)
