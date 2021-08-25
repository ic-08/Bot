#Code starts here. Write your name {Isaac}
from threading import Thread
import time
import sys

def home():
    return "Hello. I am alive!"

def run():
  if message.content.startswith('$timer'):
        message.channel.send('timer text!')
        sys.exit()

def call_timer():
    t = Thread(target=run)
    t.start()