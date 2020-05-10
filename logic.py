import twint
import saveToDB
import urllib.request, json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

from monkeylearn import MonkeyLearn


def covidByCountry():
    with urllib.request.urlopen("https://api.apify.com/v2/key-value-stores/tVaYRsPHLjNdNBu7S/records/LATEST?disableRedirect=true") as url:
        data = json.loads(url.read().decode())

        file = open('covid.json', 'w')
        file.writelines(str(data))
        return file



def addSentiment(tweets):
    analyzer = SentimentIntensityAnalyzer()
    newTweets=list()
    for tweet in tweets:
        t = {"tweet":tweet}
        t.update( analyzer.polarity_scores(tweet) )
        newTweets.append( t )

    return newTweets

def getTwit(user,key):
    #config a twint obj
    search = twint.Config()
    user = user.lower()
    search.Username = user
    search.Search = key
    search.Limit=5
    search.Store_object =True
    #save the output into a file
    search.Output = "search.txt"
    twint.run.Search(search)

    #open the output file
    search = open("search.txt", encoding="utf8").read().splitlines()

    #using the user name for splitting each tweet
    userForSplit='<'+user+'>'

    #making a search with Search(user and key)
    #remove the id, time and user name
    #send as a list to DB with the user name
    search = list( map( lambda tw: tw.lower().split(userForSplit)[1],search) )

    return ( search, user )
    #return saveToDB.toDB( search, user )




def main(user, search):
    tweets, user = getTwit(user, search)
    statistics = covidByCountry()
    tweets = addSentiment(tweets)
    saveToDB.toDB( tweets, user )
