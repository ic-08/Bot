#Functions - James (haha, flip), 
import discord
from datetime import *
import pytz
import time
import random

last_uptime = datetime.now(pytz.timezone('US/Eastern'))
last_uptime2 = time.time()   
#these will be values that we will return to Bot.py in order to send the message, with these args
building_msg = ""
msg_type = ""
msg_args = {
    'reply' : False,
    'reply_ping' : True,
    'file' : None
}
#the above args are supposed to fit neatly inside msg_list
msg_list = {}

def timer_setup(time):
    day = time // (24 * 3600)
    time = time % (24 * 3600)
    hour = time // 3600
    time %= 3600
    minutes = time // 60
    time %= 60
    seconds = time

    return "%d days, %d hours, %d, minutes, and %d seconds." % (day, hour, minutes, seconds)

#Alphabetical order, please, also add examples as comments before each one
#executes the functions, longer functions will be called
#shorter functions will not have a separate function.
#please separate each if statement with an empty line.

def search(cmd, args=[]): 
    msg_list = {} #resetting the values
    msg_args = {
        'reply' : False,
        'reply_ping' : True,
        'file' : None
    }
    building_msg = ""
    msg_type = ""

    #ex: $hello, $hi
    if cmd == 'hello' or cmd == 'hi': 
        building_msg = "Hello!"
        msg_type = "txt"
        msg_args['reply'] = True
        msg_args['reply_ping'] = False

    #ex: $8b, $8ball
    if cmd == '8b' or cmd == '8ball':

        prompts = [
            'It is certain.',
            'It is decidedly so.',
            'Without a doubt.',
            'Yes definitely.',
            'You may rely on it.',
            'As I see it, yes.',
            'Most likely.',
            'Outlook good.',
            'Yes.',
            'Signs point to yes.',
            'Reply hazy, try again.',
            'Ask again later.',
            'Better not tell you now.',
            'Cannot predict now.',
            'Concentrate and ask again.',
            "Don't count on it.",
            'My reply is no.',
            'My sources say no.',
            'Outlook not so good.',
            'Very doubtful.'
        ]
        try:
            print(args[0])
            building_msg = str(random.choice(prompts))
        except:
            building_msg = 'No prompt after command try `$8b {prompt}'
        msg_type = 'txt'

    #ex: $help
    elif cmd == 'help':
        embed = discord.Embed(
        title = 'Homelands Bot Help',
        description = "**Hi! Welcome to the Homelands Bot Help Manual**\nI am proud to be part of the Homeland's community!I can currently do a few things, altough by the start of school, I will be providing support, such as reminders, fun games, homework support, and more!\n Have fun and **GO HOMELANDS**!",
		    color = discord.Color.blue())

        embed.set_footer(text="Written with python")
        embed.set_image(url='https://cdn.discordapp.com/attachments/842823949037076520/879383578742517780/unknown.png')
        embed.add_field(name='Prefix', value = '`$`' , inline =False)
        embed.add_field(name='Commands', value = '`hello` `help` `ut` `8ball`' , inline =False)
        embed.add_field(name='Peel Link', value = '[www.peelschools.org](https://www.peelschools.org/Pages/default.aspx)' , inline =True)
        embed.add_field(name='School Holidays', value = '[Holidays](https://www.peelschools.org/calendar/Documents/School%20Year%20Calendar%202021-2022%20Regular%20Elementary%20and%20Secondary%20chart.pdf)' , inline =True)

        building_msg = embed
        msg_type = "embed"
    
    #ex: $timer 2630 (James - I really hate timers.)
    if cmd == 'timer':
        try:
            if int(args[0]) != 0:
                arrival = timer_setup(int(args[0]))
                msg_type = "timer"
                msg_args['start_msg'] = "Starting timer for " + str(args[0]) + " seconds. Expected arrival time in: " + str(arrival)
                msg_args['time'] = int(args[0])
        except:
            pass

    #ex: $ut
    elif cmd == 'ut':
        global last_uptime3, last_uptime2, last_uptime
        last_uptime3 = time.time() - last_uptime2
        timetk = []
        timetk.append(int(last_uptime3 / 86400))
        timetk.append(int((last_uptime3 % 86400) / 3600))
        timetk.append(int(((last_uptime3 % 86400) % 3600) / 60))
        timetk.append(int(((last_uptime3 % 86400) % 3600) % 60))
        building_msg = f"I have been awake for {timetk[0]} days, {timetk[1]} hours, {timetk[2]} minutes, {timetk[3]} seconds\nAwake at : {last_uptime}"
        msg_type = "txt"

    #WARNING! Please don't change the if statements to elif
    #I need it to go through each one, not to fulfill an if/elif statement and skip the rest
    msg_list['building_msg'] = building_msg
    msg_list['msg_type'] = msg_type
    msg_list['msg_args'] = msg_args
    #Since you can't send a message in this file, we'll instead send back arguments for the bot.py file
    return msg_list
