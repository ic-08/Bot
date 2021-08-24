import discord
from datetime import *
import time
import pytz
import os 
from keep_alive import keep_alive
from timer import call_timer
client = discord.Client()

@client.event
async def on_ready():
    global last_uptime
    global last_uptime2
    print('We have logged in as {0.user}'.format(client))
    last_uptime = datetime.now(pytz.timezone('US/Eastern'))
    last_uptime2 = time.time()
    await client.change_presence(activity=discord.Game('$help'))

@client.event
async def on_message(message):
    global last_uptime , last_uptime2
    if message.author == client.user:
        return
    if message.content.startswith('$help'):
      embed = discord.Embed(
        title = 'Homelands Bot Help',
        description = "**Hi! Welcome to the Homelands Bot Help Manual**\nI am proud to be part of the Homeland's community!I can currently do a few things, altough by the start of school, I will be providing support, such as reminders, fun games, homework support, and more!\n Have fun and **GO HOMELANDS**!",
		    color = discord.Color.blue()

      )
      embed.set_footer(text="Written with python")
      embed.set_image(url='https://cdn.discordapp.com/attachments/842823949037076520/879383578742517780/unknown.png')
      embed.add_field(name='Prefix', value = '`$`' , inline =False)
      embed.add_field(name='Commands', value = '`hello` `help` `ut`' , inline =False)
      embed.add_field(name='Peel Link', value = '[www.peelschools.org](https://www.peelschools.org/Pages/default.aspx)' , inline =True)
      embed.add_field(name='School Holidays', value = '[Holidays](https://www.peelschools.org/calendar/Documents/School%20Year%20Calendar%202021-2022%20Regular%20Elementary%20and%20Secondary%20chart.pdf)' , inline =True)
	  
      await message.channel.send(embed=embed)
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
        await message.channel.send("Starting")
        await time.sleep(12)
        await message.channel.send("finished")
var = os.environ['.env']  
keep_alive()     
client.run(os.environ['.env'])
#https://www.youtube.com/watch?v=SPTfmiYiuok
