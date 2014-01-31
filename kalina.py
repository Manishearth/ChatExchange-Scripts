#!/usr/bin/python
# kalina.py
# by Manish Goregaokar
# requires https://github.com/Manishearth/ChatExchange
from random import choice
import json,os,sys,getpass
from ChatExchange.SEChatWrapper import *

if("ChatExchangeU" in os.environ):
  username=os.environ["ChatExchangeU"]
else:
  print "Username: "
  username=raw_input()
if("ChatExchangeP" in os.environ):
  password=os.environ["ChatExchangeP"]
else:
  password=getpass.getpass("Password: ")


wrap=SEChatWrapper("SE")
wrap.login(username,password)
evs=json.loads(wrap.br.postSomething("chats/35/events",{"since":0,"Mode":"Messages","msgCount":"20"}))['events']
uids=[ev['user_name'] for ev in evs]
wrap.sendMessage("35","_Sets @%s on fire_" % choice(uids))
