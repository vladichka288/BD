from datetime import datetime
from . import client
from . import data
r =client.r
def createUser(login, isAdmin,password="-1",):
    p = r.pipeline()
    p.hset(login, 'online', "True")
    p.hset(login, 'dataOfRegistration', str(datetime.now()))
    p.hset(login, 'dataOfRegistration', str(datetime.now()))
    p.hset(login, 'isAdmin', str(isAdmin))
    p.sadd(data.users,login)
    if isAdmin == True:
        p.hset(login, 'password', password)
    p.execute()


def getUser(login):
    return r.hgetall(login)