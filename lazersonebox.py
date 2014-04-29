#requires https://pypi.python.org/pypi/websocket-client/
import websocket
import threading
import json,os,sys,getpass
from ChatExchange.chatexchange.wrapper import *
from BeautifulSoup import *

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


def handlepost(data):
  try:
    a=json.loads(json.loads(data)['data'])
  except:
    return False
  tags=a['tags']
  tagtext=" ".join(["[tag:"+t+"]" for t in tags])
  b=BeautifulSoup(a['body']).find('a',{'class':'question-hyperlink'})
  s="http://gaming.stackexchange.com"+b['href']
  print s
  wrap.sendMessage("35",s)

ws = websocket.create_connection("ws://sockets.ny.stackexchange.com/")
ws.send("41-questions-newest")
while True:
  a=ws.recv()
  if(a!= None and a!= ""):
    print a
    handlepost(a)
