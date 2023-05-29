# استيراد المكتبات اللازمة
import pandas as pd
from tqdm.notebook import tqdm
import snscrape.modules.twitter as sntwitter
scraper = sntwitter.TwitterSearchScraper("ضع الهاشتاق هنا")
tweets = []
number_of_tweets = 1000
for i, tweet in tqdm(enumerate(scraper.get_items()), total=number_of_tweets):
    data = [tweet.id,
            tweet.date,
            tweet.content,
            tweet.user.username,
            tweet.retweetCount,
            tweet.likeCount
            ]
    tweets.append(data)
    if i > number_of_tweets:
        break
tweet_df = pd.DataFrame(tweets, columns=["id","التاريخ", "محتوى التغريدة", "اسم المستخدم","عدد اعادة التغريدات", "عدد الاعجابات"])

# Prints data frame to the console طباعة البيانات الخاصة بالتغريدات الى الشاشة
print(tweet_df)