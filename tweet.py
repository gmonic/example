import tweepy
from flask import Flask, render_template, request

app = Flask("Twitter")

with open("credentials.txt", "r") as file:
    consumer_key = file.readline().split()[2]
    consumer_secret = file.readline().split()[2]
    access_token = file.readline().split()[2]
    access_token_secret = file.readline().split()[2]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

@app.route("/")

def main():
    return render_template("main.html")

@app.route("/timeline", method=["GET"])
def timeline():
    tweets_from_timeline = api.home_timeline()
    return render_template("main.html, tweets_from_timeline")
 print("hello")




tweets_from_timeline = api.home_timeline()
for tweet in tweets_from_timeline:
        print (tweet.text)

post_tweet = api.update_status(text=input("What would you like to tweet?"))

post_tweet = api.update_status(text)

app.run(debug=True)
