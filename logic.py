import twint
import saveToDB
from monkeylearn import MonkeyLearn






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
    search = list( map( lambda tw: tw.lower().split(userForSplit)[1],search) )
    ml = MonkeyLearn('16694abd24e9e59916c65d23796392327997c0e1')
    data = ["This is a great tool!"]
    model_id = 'cl_pi3C7JiL'
    result = ml.classifiers.classify(model_id, search[1:3])
    print(result.body[0])


    return saveToDB.toDB( result.body, user )



def main(user, search):
    getTwit(user, search)