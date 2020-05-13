# TwitchPlaysRoblox

# General info
Hello! This is TwitchPlaysRoblox, a Twitch bot that plays a Roblox game by taking in commands from the chat, similarly to TwitchPlaysPokemon.
In order to use this bot, you will first need to change a few lines in settings.txt. I will walk you through how to do this.
To use this program, you will need to install Python 3. It does not matter which version of Python you use as long as it is above 3. Additionally, be sure to install the module "pynput" using `pip install pynput`.
You will need to set up a new account to use this program. I do not know if you can set up your account with Twitch's developer tools and still use said account for streaming, but if you can actually do this (I did not refer to the Twitch developer tools' guidelines in creating this bot, and I have not used Twitch in at least a year) I'd say go ahead and do that instead of making another account.
If you need any extra help, feel free to contact me on Discord at chris12902#0182

# How to use this program
When you first install this program, your settings file should appear as the following:

port=0

pass=BOT PASSWORD HERE

username=BOT USERNAME HERE

channel=YOUR USERNAME HERE

In this file, you should set the port to the port of your Twitch stream, the password to the oauth path in your twitchapps, the username to the username of the bot you're going to use to monitor the chat, and channel to the username you'd use to log into your Twitch account. For example, if I was signing into a Twitch account named "jackeryzTTV", I would set the channel to "jackeryzTTV". REMEMBER: NEVER GIVE OUT THE PASSWORD TO YOUR TWITCH BOT. OTHERWISE, SOMEONE COULD BREAK INTO YOUR ACCOUNT AND TERRORIZE YOUR STREAM.

Afterwards, you just need to run the Python file, and the bot should start running immediately. Be sure to close the Python file when you finish streaming. Please report any bugs that you may encounter!
