# Chris12902#0182
# 12 May 2020
# Kudos to https://www.youtube.com/watch?v=T8DLwACpe3o


from pynput.keyboard import Key, Controller
import time
import socket
import string
import pyautogui

#Functions
def openSocket(HOST, PORT, PASS, IDENT, CHANNEL):
    print("signing into account " + IDENT)
    s = socket.socket()
    s.connect((HOST, PORT))
    s.send(bytes("PASS " + PASS + "\r\n", encoding='utf8'))
    s.send(bytes("NICK " + IDENT + "\r\n", 'UTF-8'))
    s.send(bytes("JOIN #" + CHANNEL + "\r\n", 'UTF-8'))
    print("sign in complete")
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
    separate = line.split(",")
    return separate[0]

def getY(line):
    separate = line.split(",")
    return separate[1]

#Variables
readbuffer = ""
keyboard = Controller()
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
        if "jump" in message.lower():
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
        if "click" in message.lower():
            X = getX(message)
            Y = getY(message)
            pyautogui.click(x=X,y=Y)
