import os
import tweepy
import time
import datetime as dt
from dateutil.relativedelta import relativedelta
import wakapi as w

os.environ['TZ'] = 'Asia/Tokyo'
time.tzset()

secret = os.environ['WAKATIME_SECRET']

CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_SECRET = os.environ['ACCESS_SECRET']

weekdays = ['月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日', '日曜日']

tWork = w.total(secret, True)
tDays = tWork["days"]
tHours = tWork["hours"]
tMin = tWork["min"]
tSec = tWork["sec"]
tWorkText = f"{tDays} 日 {tHours} 時間 {tMin} 分 {tSec} 秒"

now = dt.date.today()
yesterday = now + relativedelta(days=-1)
yText = yesterday.strftime('%Y-%m-%d')
yWork = w.date(secret,yText , True)
yHours = yWork["hours"]
yMin = yWork["min"]
ySec = yWork["sec"]
yWorkText = f"{yHours} 時間 {yMin} 分 {ySec} 秒"

todayText = now.strftime(f'%Y年%m月%d日 {weekdays[now.weekday()]}')

postText = f"（毎朝自動配信）おはようございます。本日は{todayText}です。\n\n昨日の作業時間は {yWorkText} でした。\n\n昨日までの累計は合計 {tWorkText} です。"
print(postText)

client = tweepy.Client(
	consumer_key = CONSUMER_KEY,
	consumer_secret = CONSUMER_SECRET,
	access_token = ACCESS_TOKEN,
	access_token_secret = ACCESS_SECRET
)

client.create_tweet(text=postText)