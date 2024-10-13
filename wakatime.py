import os
import tweepy
import datetime as dt
from dateutil.relativedelta import relativedelta
import wakapi as w

secret = os.environ['WAKATIME_SECRET']

CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_SECRET = os.environ['ACCESS_SECRET']

weekdays = ['月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日', '日曜日']

totalWork = w.total(secret, True)
totalWorkText = f"{totalWork["days"]} 日 {totalWork["hours"]} 時間 {totalWork["min"]} 分 {totalWork["sec"]} 秒"

now = dt.date.today()
yesterday = now + relativedelta(days=-1)
yesterdayText = yesterday.strftime('%Y-%m-%d')
yesterdayWork = w.date(secret,yesterdayText , True)
yesterdayWorkText = f"{yesterdayWork["hours"]} 時間 {yesterdayWork["min"]} 分 {yesterdayWork["sec"]} 秒"

todayText = now.strftime(f'%Y年%m月%d日 {weekdays[now.weekday()]}')

postText = f"（毎朝自動配信）おはようございます。本日は{todayText}です。\n\n昨日の作業時間は {yesterdayWorkText} でした。\n\n昨日までの累計は合計 {totalWorkText} です。"
print(postText)

client = tweepy.Client(
	consumer_key = CONSUMER_KEY,
	consumer_secret = CONSUMER_SECRET,
	access_token = ACCESS_TOKEN,
	access_token_secret = ACCESS_SECRET
)

client.create_tweet(text=postText)