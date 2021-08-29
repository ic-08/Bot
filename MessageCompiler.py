#MessageCompiler

import discord

class Compiler:
    def __init__(self, ctx, content=None, *, client, spec_channel=None, type='txt', args=None, file=None, files=None, embed=None, embeds=None, wait=False, waitfor=None, waitspec=False, editable=False, editlist={}):
       
        self.ctx = ctx 
        #the context, ex: the message that was sent by a user | -> variable

        self.content = content 
        #the content of the message you're about to send | -> string

        self.client = client #to do it: compiler(ctx=_context, _content, client=_Client)
        #the client | -> discord.Client()

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

        self.wait = wait
        #if true, waits for message | -> bool

        self.waitfor = waitfor
        #what should the bot wait for in the follow up? | -> string

        self.waitspec = waitspec
        #if true, waits for message from specific person, rather than anyone | -> bool

        self.editable = editable
        #if editable, saves to editlist, see below. | -> bool

        self.editlist = editlist
        #the ctx variables saved here will be deleted after a set amount of time detailed in the key:value | -> dict

    #add specific channel functionality
    async def send_msg():
        if Compiler.args['reply'] == True:
            if Compiler.args['reply_ping'] == True:
                await Compiler.ctx.reply(Compiler.content)
            else:
                await Compiler.ctx.reply(Compiler.content, mention_author=False)
        else:
            await Compiler.ctx.channel.send(Compiler.content, )