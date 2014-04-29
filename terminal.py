#!/usr/bin/env python
import getpass
import logging
import os
import random
import threading
import time

from ChatExchange.chatexchange.wrapper import *


#logging.basicConfig(level=logging.INFO)

#Run `. setp.sh` to set the below testing environment variables

host = "SE"
room = "35"
if "ChatExchangeU" in os.environ:
    username = os.environ["ChatExchangeU"]
else:
    print "Username: "
    username = raw_input()
if "ChatExchangeP" in os.environ:
    password = os.environ["ChatExchangeP"]
else:
    password = getpass.getpass("Password: ")

a = SEChatWrapper(host)
a.login(username,password)

def omsg(msg,wrap):
    if 'content' not in msg:
        msg['content'] = '[no content]'
    print ""
    print ">> %s (%s) %s" % (msg['event_type'], msg['user_name'], msg['content'])
    print ""
    if(msg['content'].startswith("!!/random")):
        print msg
        ret = "@"+msg['user_name']+" "+str(random.random())
        print "Spawning thread"
        wrap.sendMessage(msg["room_id"],ret)


a.joinRoom(room)
a.watchRoom(room,omsg,1)
print "See http://meta.stackexchange.com/a/218443/178438 for information on event type codes"
print "Ready"
while(True):
    b=raw_input("<< ")
    a.sendMessage(room,b)
a.logout()
