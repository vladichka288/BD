from datetime import datetime, date, time

from . import client
from . import data
from . import globalValue

r = client.r

def create_message(login_from,login_to,body):
    p = r.pipeline()
    login_of_messages = "_from_"+login_from+"_to_"+login_to+"_"+str(datetime.today())
    p.hset(login_of_messages, '_from', login_from)
    p.hset(login_of_messages, '_to', login_to)
    p.hset(login_of_messages, 'dataOfCreating', str(datetime.today()))
    p.hset(login_of_messages, 'body', body)
    p.zincrby(data.active_users, 1, login_from)
    p.lpush(data.messages, login_of_messages)
    p.rpush(data.messages_to_check,login_of_messages)

    p.publish(data.messages, login_of_messages)



    #if globalValue.isAdmin == True:
    #    p.hset(globalValue.login, 'password', globalValue.password)
    p.execute()
