from . import globalValue
from . import menu
import time
from . import client
r= client.r
from. import UserObject
from.  import data
from . import window
from datetime import datetime, date




def enteringUser(string=""):
    print("Username:")
    if globalValue.isAdmin ==True:
        print(", Admin")
    login = input()
    globalValue.loginedUser =login
    if globalValue.isAdmin == True:
        print("Password:")
        password = input()
    userObject = r.hgetall(login)
    if userObject == {} or userObject is None:
        print("Registration completed")
        if globalValue.isAdmin ==True:
            UserObject.createUser(globalValue.loginedUser,globalValue.isAdmin,password)
            menu.changeMenu('admin')
        if globalValue.isAdmin == False:
            UserObject.createUser(globalValue.loginedUser,globalValue.isAdmin)
            p = r.pubsub()
            p.subscribe("get_" + globalValue.loginedUser)
            menu.changeMenu('simple')
            date = str(datetime.today())
            log = globalValue.loginedUser + " " + date + " user logged in!"
            r.rpush(data.log_events, log)

    else:
        if globalValue.isAdmin == True:
            try:
                if userObject['password']!= password:
                    enteringUser("Wrong password")

                else:
                    menu.changeMenu('admin')

                    return True
            except KeyError:
                menu.changeMenu('simple')
                p = r.pubsub()
                menu.changeMenu('simple')
                date = str(datetime.today())
                log = globalValue.loginedUser + " " + date + " user logged in!"
                r.rpush(data.log_events, log)

        else:
            p = r.pubsub()
            time.sleep(3)
            menu.changeMenu('simple')
            date = str(datetime.today())
            log = globalValue.loginedUser + " " + date + " user logged in!"
            r.rpush(data.log_events, log)
            return True