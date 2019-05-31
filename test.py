import tweepy

import time

from config import keys

auth = tweepy.OAuthHandler(keys['CLIENT_ID'], keys['CLIENT_SECRET'])
auth.set_access_token(keys['CONSUMER_ID'],keys['CONSUMER_SECRET'])

api = tweepy.API(auth)

#id_last = '1057334316819275776' since_id = id_last


FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    file = open(file_name)
    last_seen_id = int(file.read().strip())
    file.close()
    return last_seen_id

def store_last_seen_id(file_name, last_seen_id):
    file = open(file_name, 'w')
    file.write(str(last_seen_id))
    file.close()
    return

def reply():
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(since_id=last_seen_id, tweet_mode = 'extended')

    for mention in reversed(mentions):
        last_seen_id = mention.id
        store_last_seen_id(FILE_NAME,last_seen_id)
        if '#replyashish' in mention.full_text.lower():
            print('found #replyashish! by @'+ mention.user.screen_name+'id : '+ str(mention.id))
            api.update_status('@'+ mention.user.screen_name+ ' `Hey, You mentioned me... at '+ str(mention.created_at), mention.id)

while True:
    reply()
    time.sleep(15)
    print('Searching...')
        