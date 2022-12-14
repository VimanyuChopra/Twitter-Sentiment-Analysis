import tweepy
from textblob import TextBlob
import pandas as pd

def BMP(s):
    return "".join((i if ord(i) < 10000 else '\ufffd' for i in s))

def perform_analysis(text):
    tweets = []
    sentiments = []
    polarities = []
    subjectivities = []
    try:
        tweets = get_tweets(text)
        print("Tweets retrieval successful")
    except:
        print("Tweets retrieval unsuccessful")
        if not tweets:
            return ["Tweets retrieval unsuccessful", False,0]
    for tweet in tweets:
        tb = TextBlob(str(tweet))
        polarities.append(tb.sentiment.polarity)    
        subjectivities.append(tb.sentiment.subjectivity)
        # set sentiment
        if tb.sentiment.polarity >= 0.1:
            sentiments.append('positive')
        elif tb.sentiment.polarity <= -0.05:
            sentiments.append('negative')
        else:
            sentiments.append('neutral')
    #Defining Pandas DataFrame with all the above lists
    tdf = pd.DataFrame({'Review Content' : tweets, 'Sentiment' : sentiments, 'Polarity' : polarities, 'Subjectivity' : subjectivities}, columns = ['Review Content','Sentiment','Polarity','Subjectivity'])
    analysis = "Sentiment Analysis on #" + text + " tweets : \n"
    analysis += "Total Tweets : " + str(len(tweets)) + "\n"
    analysis += "Average Polarity : " + str(sum(polarities)/len(polarities)) + "\n"
    analysis += "Average Subjectivity: " + str(sum(subjectivities)/len(subjectivities)) + "\n"
    if (sum(polarities)/len(polarities) > 0.05):
        analysis += "Overall Sentiment : Positive"
    elif (sum(polarities)/len(polarities) < -0.05):
        analysis += "Overall Sentiment : Negative"
    else:
        analysis += "Overall Sentiment : Neutral"
        
    return [analysis, True,tdf]

def generateCSV(rdf,file):
    rdf.to_csv(file, index=False)
    print ("Successfully Generated")

def get_tweets(text):
    
    consumer_key= 'wWd7rfnx0psWRYgqSqFycXvzg'
    consumer_secret= 'caMlhQsB5MqD0anXMXv7z6IZY01RwBJqwu9vTK7UxGSiv62Bqa'

    access_token='935417152236019712-MxqC6Imbs9GrEoPGPkl8iFemck9vxi8'
    access_token_secret='kwdRVq8xD5GL5IwkjcizWvE9WbSXi85Q1iIsO4ePUiE7d'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    # Retrieve Tweets
    public_tweets = api.search(text, count = 50)
    
    tweets = []

    for tweet in public_tweets:
        tweets.append(BMP(tweet.text))
        
    return tweets

