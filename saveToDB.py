import pymongo


def toDB(tweets, user):
    print("HI")
    print(tweets[0])
    # open a mongo connection
    client = pymongo.MongoClient("mongodb://localhost:27017/")

    db = client["mydatabase"]
   # print(client.list_database_names())

    #dblist = client.list_database_names()
   # if "mydatabase" in dblist:
    #    print("The database exists.")
    #else:
     #   print("The database dose not exists.")

    col = db[user]

    for tweet in tweets:
        tweetsToDB = {"tweet": tweet}
        result = col.insert_one(tweetsToDB)
        print('One post: {0}'.format(result.inserted_id))


