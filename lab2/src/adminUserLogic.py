from . import client
from . import data
r = client.r
def log_events():
    end = r.llen(data.log_events)
    listOfSpamers =  r.lrange(data.log_events,0,end)
    for el in listOfSpamers:
       print(el)
    input()
def List_of_Users_these_are_online():
    print("Users online:")
    input()
def Rating_of_active_users():
    print("Active users:")
    amount = r.zcard(data.active_users)
    listOfActiveUsers = r.zrange(data.active_users, 0, amount, True, True)
    for el in listOfActiveUsers:
        print(el)
    input()

    input()
def Rating_of_active_spamers():
    print("Active spamers")
    amount = r.zcard(data.spamers)
    listOfSpamers = r.zrange(data.spamers,0,r.zcard(data.spamers),True,True)
    for el in listOfSpamers:
        print(el)
    input()
