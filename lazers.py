#requires https://pypi.python.org/pypi/websocket-client/
import websocket
import threading
import json,os,sys
from ChatExchange.SEChatWrapper import *
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
  a=json.loads(json.loads(data)['data'])['body']
  print a
  b=BeautifulSoup(a).find('a',{'class':'question-hyperlink'})
  print b
  s="[ LAZERS v2 ]  [%s](%s)" % (" ".join(b.contents),"http://gaming.stackexchange.com"+b['href'])
  print s
  wrap.sendMessage("35",s)
  #wrapm.sendMessage("89",s)

ws = websocket.create_connection("ws://sockets.ny.stackexchange.com/")
ws.send("41-questions-newest")
while True:
  a=ws.recv()
  if(a!= None and a!= ""):
    print a
    handlepost(a)
