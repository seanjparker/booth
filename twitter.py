import tweepy
import os
import keys

def postPhoto(image, status, n):
    # OAuth process, using the keys and tokens
    auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
    auth.set_access_token(keys.access_token, keys.access_token_secret)

    # Creation of the actual interface, using authentication
    api = tweepy.API(auth)

    user = api.me()

    # Sample method, used to update a status
    # api.update_status('#GreatUniHack')

    # Send the tweet.
    print("Sending tweet " + n)
    api.update_with_media(image, status)
    print("Done uploading " + n)
