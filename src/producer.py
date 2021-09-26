#!/usr/bin/python3 

from kafka import KafkaProducer
from datetime import datetime
import secret_config as conf ## where I put my Twitter API keys
import tweepy
import sys
import re
from pprint import pprint

TWEET_TOPICS = ['pizza']

KAFKA_BROKER = 'localhost:9092'
KAFKA_TOPIC = 'tweets'

class Streamer(tweepy.Stream):
    def on_request_error(self, status_code):
        if status_code == 402:
            return False

    def on_connection_error(self):
        print("Calling disconnect!!")
        self.disconnect()

    def on_status(self, status):
        tweet = status.text

        tweet = re.sub(r'RT\s@\w*:\s', '', tweet)
        tweet = re.sub(r'https?.*', '', tweet)

        global producer
        producer.send(KAFKA_TOPIC, bytes(tweet, encoding='utf-8'))

        d = datetime.now()

        print(f'[{d.hour}:{d.minute}.{d.second}] {tweet}')

stream = Streamer(
    conf.consumer_key, 
    conf.consumer_secret_key, 
    conf.access_token, 
    conf.access_token_secret)

try:
    producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER)
except Exception as e:
    print(f'Error Connecting to Kafka --> {e}')
    sys.exit(1)

stream.filter(track=TWEET_TOPICS)
