# MinecraftServer-Discord-Bot
Have you ever wanted a discord bot that started your Minecraft server?


# Setup
This quick guide will show you how to create a Discord Bot and wire it up to your Python script.

### Setting up the bot
Setting up a Discord bot is much easier than you may think if you do it for your first time.
Here is how to do it:
1. Go to https://discord.com/developers
2. Create a new application
3. Call it what you want
4. Change the profile picture and make a description (optional)
5. Go to the "bot" section and buil a bot
6. Go to the "OAuth2" section and the "URL Generator" submenu
7. Chose "Bot" in the "URL Generator" and "Administrator" in the "Bot permissions"
8. Copy the link and add it to you Discord server

### Copying the token
You have now made the Discord Bot, but it does not know how to connect to the code you have.
You will therefore need to get the Discord Bot token:
1. Go back to the "bot" section
2. Copy the token (dont share it with anyone)
3. Paste the token into the code

### Setting up "!startserver" command
When you host a minecraft server on your pc, you most likely start it with a "start.bat" file.
This bot will run that "start.bat" file for you:
1. Place the bot code in the same folder as your server
2. Copy the file placement for the start file. example(C:\users\bot\desktop\server\start.bat)
3. Paste it into the code under the "!startserver" command


# Use
In any text channel of you Discord server that you have added the bot to, you can use the commands:
!test  -  test if the bot is working. If it replies, it works. If it dont reply, it is not working
!startserver  -  start the server by starting you "start.bat" file

Have fun and experiment with the bot yourself 
