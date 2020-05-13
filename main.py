# Chris12902#0182
# 12 May 2020
# Kudos to https://www.youtube.com/watch?v=T8DLwACpe3o
# Thanks to Chemiclast, Zoom1220, and Whlteghost for helping QA test this program!

import time
import socket
import string
import re
import pyautogui
import keyboard

#Functions
def openSocket(HOST, PORT, PASS, IDENT, CHANNEL):
    print("signing into account " + IDENT)
    s = socket.socket()
    s.connect((HOST, PORT))
    s.send(bytes("PASS " + PASS + "\r\n", encoding='utf8'))
    s.send(bytes("NICK " + IDENT + "\r\n", 'UTF-8'))
    s.send(bytes("JOIN #" + CHANNEL + "\r\n", 'UTF-8'))
    print("sign in complete!")
    return s

def loadingComplete(line):
    if("End of /NAMES list" in line):
        return False
    else:
        return True
    
def joinRoom(s):
    print("joining chat...")
    readbuffer = ""
    Loading = True
    while Loading:
        readbuffer = readbuffer + str(s.recv(1024))
        temp = str.split(readbuffer, "\n")
        readbuffer = temp.pop()
        if "Improperly formatted auth" in readbuffer:
            print("error: improperly formatted auth")
            quit()
        Loading = loadingComplete(readbuffer)
    print("successfully joined chat!")
    sendMessage(s, "successfully joined the chat!")

def sendMessage(s, message):
    global CHANNEL
    messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
    s.send(bytes(messageTemp + "\r\n",'UTF-8'))
    print("sent " + messageTemp)

def getUser(line):
    separate = line.split(":", 2)
    user = separate[1].split("!", 1)[0]
    return user

def getMessage(line):
    message = line.split('PRIVMSG #'+getUser(line)+' :')
    message = message[len(message)-1].split("\\r\\n")[0]
    return message

def getX(line):
    separate = line.split(",")[0]
    separate = separate.split(" ")[1]
    print(separate)
    return separate[0]

def getY(line):
    separate = line.split(",")
    return separate[1]

def KeyPress(key):
    PressKey(key)
    time.sleep(0.5)
    ReleaseKey(key)

#Variables

readbuffer = ""
delay = 750 #in milliseconds

#These lines read the text file and set up the variables of the program. You absolutely do not want to edit these lines.
print("initializing settings...")
try:
    settingsFile = open("settings.txt","r")
except:
    print("error: settings file is invalid")
    quit()
sfLines = settingsFile.readlines()
PORT = sfLines[0][5:len(sfLines[0])-1]
PORT = int(PORT)
PASS = sfLines[1][5:len(sfLines[1])-1]
USERNAME = sfLines[2][9:len(sfLines[2])-1]
CHANNEL = sfLines[3][8:len(sfLines[3])-1]
settingsFile.close()
print("initialization complete")
print("now connecting to twitch's APIs")
s = openSocket("irc.twitch.tv", PORT, PASS, USERNAME, CHANNEL) #Connects to your Twitch profile
joinRoom(s)
while True:
    readbuffer = readbuffer + str(s.recv(1024))
    temp = str.split(readbuffer, "\n")
    readbuffer = temp[0]
    for line in temp:
        if "PING :tmi.twitch.tv" == line:
            s.send(bytes("PONG :tmi.twitch.tv", 'UTF-8'))
        user = getUser(line)
        message = getMessage(line)
        if "w" == message.lower() or "a" == message.lower() or "d" == message.lower() or "s" == message.lower() or "jump" in message.lower() or "click" in message.lower():
            print("took input from "+user+": "+message)
        if "w" == message.lower():
            repeats = 0
            while repeats < delay:
                keyboard.press_and_release('w')
                repeats = repeats + 1
        if "a" == message.lower():
            repeats = 0
            while repeats < delay:
                keyboard.press_and_release('a')
                repeats = repeats + 1
        if "d" == message.lower():
            repeats = 0
            while repeats < delay:
                keyboard.press_and_release('d')
                repeats = repeats + 1
        if "s" == message.lower():
            repeats = 0
            while repeats < delay:
                keyboard.press_and_release('s')
                repeats = repeats + 1
        if "jump" in message.lower():
            repeats = 0
            while repeats < 5:
                keyboard.press_and_release('space')
                repeats = repeats + 1
            if "jump+w" == message.lower():
                repeats = 0
                while repeats < delay:
                    keyboard.press_and_release('w')
                    repeats = repeats + 1
            if "jump+a" == message.lower():
                repeats = 0
                while repeats < delay:
                    keyboard.press_and_release('a')
                    repeats = repeats + 1
            if "jump+d" == message.lower():
                repeats = 0
                while repeats < delay:
                    keyboard.press_and_release('d')
                    repeats = repeats + 1
            if "jump+s" == message.lower():
                repeats = 0
                while repeats < delay:
                    keyboard.press_and_release('s')
                    repeats = repeats + 1
        if "click" in message.lower():
            try:
                X = getX(message)
                Y = getY(message)
                pyautogui.click(x=int(X),y=int(Y))
            except:
                pyautogui.click()
