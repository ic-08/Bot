#debug tests that I needed to do
#This will most likely be removed in the initial release.

import time
import threading

def hello():
    print("hello, Timer")

def inter():
    print("Intercept")

t = threading.Timer(3.0, hello)
t.start()

t = threading.Timer(1.5, inter)
t.start()