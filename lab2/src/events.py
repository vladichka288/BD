import msvcrt
from . import globalValue
from . import menu
from . import data
from . import adminUserLogic
from . import simpleUserLogic
from . import authorization
from . import window
import os
from . import window
from datetime import datetime, date
from . import client
r = client.r
def up():
    if globalValue.currentWindow == window.getNameOfActiveWindow():
        while msvcrt.kbhit():
            msvcrt.getch()
        if globalValue.selected == 0:
            menu.show_menu()
            return
        globalValue.selected -= 1
        menu.show_menu()



def down():
    if globalValue.currentWindow == window.getNameOfActiveWindow():
        while msvcrt.kbhit():
            msvcrt.getch()
        if globalValue.isListForSending == True:
            if globalValue.selected == len(globalValue.listOfUsers) - 1:
                menu.show_menu()
                return
            globalValue.selected += 1
            menu.show_menu()
            return
        if globalValue.isAdmin == True:
            if globalValue.selected == len(data.adminMode)-1:
                menu.show_menu()
                return
            globalValue.selected += 1
            menu.show_menu()
            return
        if globalValue.isSimpleUser == True:
            if globalValue.selected == len(data.userMode)-1:
                menu.show_menu()
                return
            globalValue.selected += 1
            menu.show_menu()
            return
        if globalValue.isStartMenu == True:
            if globalValue.selected == len(data.startMenu)-1:
                menu.show_menu()
                return
            globalValue.selected += 1
            menu.show_menu()
            return

def shift():
    if globalValue.currentWindow == window.getNameOfActiveWindow():
       # global selected
        if globalValue.isAdmin == True and data.adminMode[globalValue.selected]!='exit':
                if data.adminMode[globalValue.selected] == 'log events':
                   adminUserLogic.log_events()
                if data.adminMode[globalValue.selected] == 'online users':
                    adminUserLogic.List_of_Users_these_are_online()
                if data.adminMode[globalValue.selected] == 'active users':
                    adminUserLogic.Rating_of_active_users()
                if data.adminMode[globalValue.selected] == 'active spamers':
                    adminUserLogic.Rating_of_active_spamers()
                menu.show_menu()
        elif globalValue.isAdmin == True and data.adminMode[globalValue.selected]=='exit':

             menu.changeMenu('start')
             globalValue.selected = 0
             menu.show_menu()
        elif globalValue.isSimpleUser == True and data.userMode[globalValue.selected]!='exit':
            #selected = 0
            if data.userMode[globalValue.selected] == 'Send message':
                menu.changeMenu('send_message')
                menu.show_menu()

            if data.userMode[globalValue.selected] == 'read messages':
                simpleUserLogic.read_income_messages()
            if data.userMode[globalValue.selected] == 'messages are checking for spam':
                simpleUserLogic.messages_are_checking_for_spam()
            if data.userMode[globalValue.selected] == 'messages are blocked due to spam':
                simpleUserLogic.messages_are_blocked_due_to_spam()
            menu.show_menu()
        elif globalValue.isSimpleUser == True and data.userMode[globalValue.selected]=='exit':
             date = str(datetime.today())
             log = globalValue.loginedUser + " " + date + " user logged out!"
             r.rpush(data.log_events, log)
             menu.changeMenu('start')
             globalValue.selected = 0
             menu.show_menu()

        elif globalValue.isStartMenu == True and data.startMenuArray[globalValue.selected]!='exit':
            if data.startMenuArray[globalValue.selected] == 'Admin':
                    menu.changeMenu('admin')
                    authorization.enteringUser()
                    globalValue.selected = 0
                    menu.show_menu()
            elif data.startMenuArray[globalValue.selected] == 'Simple User':
                    menu.changeMenu('simple')
                    authorization.enteringUser()
                    globalValue.selected = 0
                    menu.show_menu()
            elif data.startMenuArray[globalValue.selected] == 'Worker':
                    menu.changeMenu('worker')
                    globalValue.selected = 0
                    menu.show_menu()
        elif globalValue.isStartMenu == True and data.startMenuArray[globalValue.selected] == 'exit':
            os.abort()
        elif globalValue.isListForSending == True:
            simpleUserLogic.send_a_message()
            menu.changeMenu("simple")

            menu.show_menu()
