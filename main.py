from discord.ext import commands
import asyncio
import os
from keep_alive import keep_alive
import discord

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
    
    if args != '()':
        msg = random.choice(predictions)
    else:
        msg = 'No prompt given. Try `$8ball <prompt>`'

    await ctx.send(msg)

#hi() is for saying hello. Ex: $hi, $hello
@bot.command(aliases=['hello', 'hi!', 'hello!', 'hi there', 'Hi there', 'Hi there!', 'Howdy!', 'howdy!', 'Hello', 'Hello!', 'Hi!', 'Hi'])
async def hi(ctx):
    await ctx.reply('Hello!', mention_author = False)

#help() is for asking for help. Ex: $help, $Help
@bot.command(aliases=['Help'])
async def help(ctx):
    await ctx.send('')

#test() is for testing. Ex: $test, $ttt
@bot.command(aliases=['ttt'])
async def test(ctx, *args):
    await ctx.send(str(args))

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="$help | $cmd for a list of commands"))

bot.run(os.environ['.env'])