from discord.ext import commands
import asyncio
import os
from keep_alive import keep_alive
keep_alive()

bot = commands.Bot(command_prefix='$')

@commands.command(aliases=['ttt'])
async def test(ctx, *args):
    await ctx.send(str(args))

@commands.command()
async def james(ctx):
    await ctx.send('Isaac is ricj')

@commands.command()
async def isaac(ctx):
    await ctx.send('James is ricj')

bot.add_command(test)
bot.add_command(james)
bot.run(os.environ['.env'])
