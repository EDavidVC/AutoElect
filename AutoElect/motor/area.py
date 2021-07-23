from AutoElect.redirect import redirect_reply
from AutoElect.reply import send_OK
from AutoElect.reply import nextNav
from AutoElect.reply import nextNavigation
from AutoElect.values import Constants
import os
import time
class Area():
	def __init__(self, id, title, link, reply, isCharge):
		self.title = title
		self.link = link
		self.reply = reply
		self.isCharge = isCharge
		self.id = id
	def getTitle(self):
		return self.title
	def getLink(self):
		return self.link
	def getReply(self):
		return self.reply
	def getIsCharge(self):
		return self.isCharge
	def getId(self):
		return self.id
def StartArea(sArea, cant):
	cantTemp = 1
	actualNav = 0
	actualTemp = 0
	while(cantTemp <= cant):
		if(not sArea.isCharge):
			charge(sArea)
		Constants.chrome.get(sArea.getLink())
		print("Titulo	: " + str(sArea.title))
		print("Cantidad	: " + str(cantTemp) + "/" + str(cant))
		for nav in sArea.reply:
			nextNavigation(actualNav)
			for answer in nav:
				nextNav(actualTemp)
				time.sleep(Constants.velocity)
				redirect_reply(answer["_type"], answer["_answer"])
				if(answer["_isOk"]):
					send_OK()
				actualTemp = actualTemp + 1
				
			actualNav = actualNav + 1
			actualTemp = 0
		os.system("cls")
		cantTemp = cantTemp + 1
		actualNav = 0

def charge(sArea):
	actualNav = 0
	actualTemp = 0
	print("CARGANDO....")
	Constants.chrome.get(sArea.getLink())
	for nav in sArea.reply:
		nextNavigation(actualNav)
		for temp in nav:
			nextNav(actualTemp)
			actualTemp = actualTemp + 1
		actualTemp = 0
		actualNav= actualNav + 1
	actualNav = 0
	sArea.isCharge = True

