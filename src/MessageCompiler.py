#MessageCompiler

import discord

class Compiler:
    def __init__(self, ctx, content=None, *, spec_channel=None, type='txt', args=None, file=None, files=None, embed=None, embeds=None):
       
        self.ctx = ctx 
        #the context, ex: the message that was sent by a user | -> variable

        self.content = content 
        #the content of the message you're about to send | -> string

        self.spec_channel = spec_channel 
        #a specific channel that you're going to send to? | -> channelid

        self.type = type 
        #the type of message, 'txt', 'embed', 'file' | -> string
        
        self.args = args 
        #any additional arguments, such as who you're replying to | -> list
        
        self.file = file 
        #any file you're going to send | -> discord.file, file
        
        self.files = files 
        #multiple files, DO NOT CONFUSE WITH self.file | -> list of files
        
        self.embed = embed 
        #embed | -> discord.Embed
        
        self.embeds = embeds 
        #multiple embeds, DO NOT CONFUSE WITH self.embed | -> list of embeds
    
    async def categorize_msg():
        pass #checks type, args, file, files, embed, and embeds

    #add specific channel functionality
    async def received_msg():
        if Compiler.args['reply'] == True:
            if Compiler.args['reply_ping'] == True:
                await Compiler.ctx.reply(Compiler.content)
            else:
                await Compiler.ctx.reply(Compiler.content, mention_author=False)
        else:
            await Compiler.ctx.channel.send(Compiler.content)