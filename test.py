import os
import tweepy
import datetime as dt

CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_SECRET = os.environ['ACCESS_SECRET']

weekdays = ['月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日', '日曜日']

now = dt.date.today()
nowText = now.strftime(f'%Y年%m月%d日 {weekdays[now.weekday()]}')
postText = f"（自動投稿）\n本日は{nowText}です。\n自動投稿に成功しました。 by Python"
print(postText)

client = tweepy.Client(
	consumer_key = CONSUMER_KEY,
	consumer_secret = CONSUMER_SECRET,
	access_token = ACCESS_TOKEN,
	access_token_secret = ACCESS_SECRET
)

client.create_tweet(text=postText)