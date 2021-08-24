import discord
from datetime import *
import time


client = discord.Client()

@client.event
async def on_ready():
    global last_uptime
    global last_uptime2
    print('We have logged in as {0.user}'.format(client))
    last_uptime = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
    last_uptime2 = time.time()

@client.event
async def on_message(message):
    global last_uptime , last_uptime2
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    if message.content.startswith('$ut'):
        last_uptime3 = time.time() - last_uptime2
        timetk = []
        timetk.append(int(last_uptime3 / 86400))
        timetk.append(int((last_uptime3 % 86400) / 3600))
        timetk.append(int(((last_uptime3 % 86400) % 3600) / 60))
        timetk.append(int(((last_uptime3 % 86400) % 3600) % 60))
        await message.channel.send(f"I have been awake for {timetk[0]} days, {timetk[1]} hours, {timetk[2]} minutes, {timetk[3]} seconds")
        await message.channel.send(f"Awake at : {last_uptime}")
    if message.content.startswith('$timer'):
        await message.channel.send('!help')
        
client.run('ODIyNDg4NjcwMTUzNDc0MDk4.YFTARA._8ZuIZgjDeX0RBT3etRsLYhsufI')
#https://www.youtube.com/watch?v=SPTfmiYiuok
