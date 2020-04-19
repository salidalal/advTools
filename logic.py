import twint
import saveToDB




def getTwit(user,key):
    search = twint.Config()
    search.Username = user
    search.Search = key
    search.Limit=5
    search.Store_object =True
    search.Output = "search.txt"
    twint.run.Search(search)


    search = open("search.txt", encoding="utf8").read().splitlines()


    userForSplit='<'+user+'>'

    #making a search with Search(user and key)
    #remove the id, time and user name
    #send as a list to DB with the user name
    return saveToDB.toDB( list( map( lambda tw: tw.lower().split(userForSplit)[1],search) ), user )



def main(user, search):
    getTwit(user, search)