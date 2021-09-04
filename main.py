from discord.ext import commands
import os
from keep_alive import keep_alive
import discord

import bot_func
from bot_func import search

keep_alive()

import random

bot = commands.Bot(command_prefix='$')

## BELOW USED FOR BOT ##
def separate_str(string):
    building_word = ''
    word_list = []
    if string != '()' and string != "":
        for char in string:
            if char != " " and char != "(" and char != ")" and char != ",":
                building_word += char
            else:
                word_list.append(building_word)
                building_word = ''
    return word_list

### BOT'S COMMAND LIST BELOW! ###
### ALPHABETICAL ORDER PLEASE ###

'''
Notice: Before each command, there SHOULD be a comment detailing the command and how to use it.
For example:
#test() is for testing. Ex: $test, $ttt
'''

#_8ball is for 'determining the future' (not really). Ex: $_8ball <prompt>, $8ball <prompt>, $8b <prompt>
@bot.command(aliases=['8ball', '8b'])
async def _8ball(ctx, *args): #unfortunally, async def 8ball(): returned an error
    #list of predictions to (randomly) choose from
    predictions = [
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
    
    if str(args) != '()':
        msg = random.choice(predictions)
    else:
        msg = 'No prompt given. Try `$8ball <prompt>`'

    await ctx.send(msg)

#cmd() is for getting a list of cmds. For now it is a list, aiming to build a list like Dank Memer
@bot.command(aliases=['command', 'cmds', 'commands', 'com'])
async def cmd(ctx, *args):
    if str(args) != '()':
        pass #for looking up a specific cmd
    else:
        await ctx.send('`$cmd <optional: specific command>`')
        await ctx.send(search('CMD_GET_ALL')) #for getting a dictionary of all cmds
#https://www.i2symbol.com/symbols/corner link to unicode characters for stuff like this: └
#see Dank Memer pls help to see more

#credits is to show credits. Ex: $credits
@bot.command(aliases=['credit', 'contributors'])
async def credits(ctx):
    embd = discord.Embed(
        title = "CREDITS",
        color = discord.Color.teal()
    )
    embd.add_field('CONTRIBUTORS', value = "**Isaac**, your official macho man.\n**James**, wielder of the flying axe.\n**Daniel**, Hollywood alias 'Daniellus Di'Egro'.")
    embd.set_footer(text="Written with Python. With love, James 🪓.")

    await ctx.send(embed=embd)

#help() is for asking for help. Ex: $help, $Help
@bot.command(aliases=['Help'])
async def help(ctx):
    embd = discord.Embed(
        title = 'Homelands Bot Help',
        description = "**Hi! Welcome to the Homelands Bot Help Manual**\nI am proud to be part of the Homeland's community!I can currently do a few things, altough by the start of school, I will be providing support, such as reminders, fun games, homework support, and more!\n Have fun and **GO HOMELANDS**!",
        color = discord.Color.blue()
    )

    embd.set_footer(text="Written with Python.")
    embd.set_image(url='https://cdn.discordapp.com/attachments/842823949037076520/879383578742517780/unknown.png')
    embd.add_field(name='Prefix', value = '`$`' , inline =False)
    embd.add_field(name='Commands', value = '`$cmd` for more info.' , inline =False)
    embd.add_field(name='Peel Link', value = '[www.peelschools.org](https://www.peelschools.org/Pages/default.aspx)' , inline =True)
    embd.add_field(name='School Holidays', value = '[Holidays](https://www.peelschools.org/calendar/Documents/School%20Year%20Calendar%202021-2022%20Regular%20Elementary%20and%20Secondary%20chart.pdf)' , inline =True)

    await ctx.send(embed=embd)

#hi() is for saying hello. Ex: $hi, $hello
@bot.command(aliases=['hello', 'hi!', 'hello!', 'hi there', 'Hi there', 'Hi there!', 'Howdy!', 'howdy!', 'Hello', 'Hello!', 'Hi!', 'Hi'])
async def hi(ctx):
    await ctx.reply('Hello!', mention_author = False)

#test() is for testing. Ex: $test, $ttt
@bot.command(aliases=['ttt'])
async def test(ctx, *args):
    await ctx.send(str(args))


### BOT ON_READY EVENTS ###
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="$help | $cmd for a list of commands"))

bot.run(os.environ['.env'])