import discord
from datetime import *
from discord import message
import os
from keep_alive import keep_alive
import threading
client = discord.Client()

prefix = '$' #we're using the dollar sign, right? - James

import bot_func
from bot_func import search #James - we also need to import the bot_func.py
#The above is a list of functions. Check the file for more details

#James - Arguments will be taken and separated by spaces 

def separate_str(cmdstr):
    counter = 1
    building_word = ''
    word_list = []
    for char in cmdstr:
        if counter != 1:
            if char == " ":
                if building_word != '':
                    word_list.append(building_word)
                building_word = ''
            elif char == "$":
                pass
            else:
                building_word += char
                    
        else:
            if char != prefix:
                word_list.clear()
                word_list.append(False)
        counter += 1
    if building_word != '':
        word_list.append(building_word)
    return word_list

def timer_msg(message_):
    print(message_) #You're going to have to do this yourself. @Isaac

def timer_start(sec, message_):
    t = threading.Timer(sec, timer_msg(message_))
    t.start()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game('$help'))

command = []
command_m = []
pending_msg = {}

#below two variables are meant to be used in conjunct with MessageCompiler.py
waitfor_msg = False #will the bot wait for the user to respond after the bots sends a prompt?
waitfor_msgctx = '' #What specific message will the bot wait for? If empty, that means there is no specific message that the bot waits for
#Any questions about these two variables, ask me - James

@client.event
async def on_message(message):
    pending_msg = {} #clearing after each use, resetting the values
    if message.author == client.user:
        return
    
    else:
        command = separate_str(str(message.content))
        if command[0] == False:
            pass
        elif command == []:
            pass
        else:
            if len(command) != 1:
                command_m = command.pop(0)
                pending_msg = search(command_m, args=command)
            else:
                pending_msg = search(command[0])
            try:
                if pending_msg['msg_type'] == 'txt':
                    if pending_msg['msg_args']['reply'] == True:
                        await message.reply(pending_msg['building_msg'], mention_author=False)
                    else:
                        await message.channel.send(pending_msg['building_msg'])
                elif pending_msg['msg_type'] == 'embed':
                    await message.channel.send(embed = pending_msg['building_msg'])
                elif pending_msg['msg_type'] == 'timer':
                    await message.channel.send(pending_msg['start_msg'])
                    timer_start(pending_msg['time'], "Finished timer for " + str(pending_msg['time']))
            except:
                pass

#below was the original code. If you still need to use it, here it is. - James
#Also, please don't delete it, I probably need to use it as a ref - James
'''
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
'''

var = os.environ['.env']  
keep_alive()     
client.run(os.environ['.env'])
#https://www.youtube.com/watch?v=SPTfmiYiuok


'''
last_uptime = datetime.now(pytz.timezone('US/Eastern'))
    last_uptime2 = time.time()
def universal_t():
    if message.content.startswith('$ut'):
        last_uptime3 = time.time() - last_uptime2
        timetk = []
        timetk.append(int(last_uptime3 / 86400))
        timetk.append(int((last_uptime3 % 86400) / 3600))
        timetk.append(int(((last_uptime3 % 86400) % 3600) / 60))
        timetk.append(int(((last_uptime3 % 86400) % 3600) % 60))
        return timetk'''
