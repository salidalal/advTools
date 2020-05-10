import pymongo


def toDB(tweets, user):

    # open a mongo connection
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["mydatabase"]
    col = db[user]

    for tweet in tweets:
        col.insert_one(tweet)

    return tweets


