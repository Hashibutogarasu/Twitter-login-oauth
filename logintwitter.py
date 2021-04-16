import sys
import os
import tweepy
import pathlib
import json


consumer_key = "" #api_key
consumer_secret = "" #api_key_ssecret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

try:
    json_open = open('settings.json', 'r')
    json_load = json.load(json_open)

    access_token = json_load['authtoken']['access_token']
    access_token_secret = json_load['authtoken']['access_token_secret']
  
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    me = api.me()
    print(f'ログインが完了しました。:{me.name}')

except:
    # get access token from the user and redirect to auth URL
    auth_url = auth.get_authorization_url()
    print('Authorization URL: ' + auth_url)

    # ask user to verify the PIN generated in broswer
    verifier = input('PIN: ').strip()
    auth.get_access_token(verifier)

    path = './settings.json'
    f = open(path, 'w') #Jsonファイルを生成。
    f.write('{\n')
    f.write('  "authtoken":{\n')
    f.write(f'    "access_token":"{auth.access_token}",\n')
    f.write(f'    "access_token_secret":"{auth.access_token_secret}"\n')
    f.write('  }\n')
    f.write('}')

    try:
        json_open = open('settings.json', 'r')
        json_load = json.load(json_open)

        access_token = json_load['authtoken']['access_token']
        access_token_secret = json_load['authtoken']['access_token_secret']
  
        print(f"{access_token}\n{access_token_secret}")
    except Exception:
        pass

    # authenticate and retrieve user name
    auth.set_access_token(auth.access_token, auth.access_token_secret)
    api = tweepy.API(auth)
    me = api.me()
    print(f'ログインが完了しました。:{me.name}')
