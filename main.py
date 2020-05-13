# Chris12902#0182
# 12 May 2020
# Kudos to https://www.youtube.com/watch?v=T8DLwACpe3o

import socket
import string
from pynput.keyboard import Key, Controller

#Functions
def openSocket(HOST, PORT, PASS, IDENT, CHANNEL):
    s = socket.socket()
    s.connect((HOST, PORT))
    s.send("PASS " + PASS + "\r\n")
    s.send("NICK " + IDENT + "\r\n")
    s.join("JOIN #" + CHANNEL + "\r\n")
    return s

def joinRoom(s):
    readbuffer = ""
    Loading = True
    while Loading:
        readbuffer = readbuffer + s.recv(1024)
        temp = string.split(readbuffer, "\n")
        readbuffer = temp.pop()
        for line in temp:
            Loading = LoadingComplete(line)
    sendMessage(s, "successfully joined the chat!")

def loadingComplete(line):
    if("End of /NAMES list" in line):
        return False
    else:
        return True

def sendMessage(s, message):
    global CHANNEL
    messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
    s.send(messageTemp + "\r\n")
    print("Sent: " + messageTemp)

def getUser(line):
    separate = line.split(":", 2)
    user = separate[1].split("!", 1)[0]
    return user

def getMessage(line):
    separate = line.split(":", 2)
    message = separate[2]
    return message

#Variables
readbuffer = ""
keyboard = Controller()
#These lines read the text file and set up the variables of the program. You absolutely do not want to edit these lines.
settingsFile = open("settings.txt","r")
sfLines = settingsFile.readlines()
PORT = sfLines[0][5:len(sfLines[0])-1]
PORT = int(PORT)
PASS = sfLines[1][5:len(sfLines[1])-1]
USERNAME = sfLines[2][9:len(sfLines[2])-1]
CHANNEL = sfLines[3][8:len(sfLines[3])-1]
settingsFile.close()

s = openSocket("irc.twitch.tv", PORT, PASS, USERNAME, CHANNEL) #Connects to your Twitch profile
joinRoom(s)

while True:
    readbuffer = readbuffer + s.recv(1024)
    temp = string.split(readbuffer, "\n")
    readbuffer = temp.pop()
    for line in temp:
        if "PING" in line:
            s.send(line.replace("PING", "PONG"))
        user = getUser(line)
        message = getMessage(line)
        if "w" == message.lower():
            keyboard.press('w')
            time.sleep(0.3)
            keyboard.release('w')
        if "a" == message.lower():
            keyboard.press('a')
            time.sleep(0.1)
            keyboard.release('a')
        if "d" == message.lower():
            keyboard.press('d')
            time.sleep(0.1)
            keyboard.release('d')
        if "s" == message.lower():
            keyboard.press('s')
            time.sleep(0.1)
            keyboard.release('s')
        if "jump" == message.lower():
            keyboard.press(Key.space)
            if "jump+w" == message.lower():
                keyboard.press('w')
            if "jump+a" == message.lower():
                keyboard.press('a')
            if "jump+d" == message.lower():
                keyboard.press('d')
            if "jump+s" == message.lower():
                keyboard.press('s')
            time.sleep(0.1)
            keyboard.release(Key.space)
            if "jump+w" == message.lower():
                keyboard.release('w')
            if "jump+a" == message.lower():
                keyboard.release('a')
            if "jump+d" == message.lower():
                keyboard.release('d')
            if "jump+s" == message.lower():
                keyboard.release('s')
        
