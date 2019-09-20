# TWITTER HANDSHAKE FILE. Keys/Tokens/Secrets come from .env file

import basilica
import tweepy
from decouple import config
from .models import DB, Tweet, User

# OAuthHandler is an open authentication handler; "CONSUMER" might refer to logging into twitter with 
#  your own twitter account
TWITTER_AUTH = tweepy.OAuthHandler(config('TWITTER_CONSUMER_KEY'), config('TWITTER_CONSUMER_SECRET'))

TWITTER_AUTH.set_access_token(config('TWITTER_ACCESS_TOKEN'), config('TWITTER_ACCESS_TOKEN_SECRET'))

TWITTER = tweepy.API(TWITTER_AUTH)

BASILICA = basilica.Connection(config('BASILICA_KEY'))