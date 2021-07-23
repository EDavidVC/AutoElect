import json
from AutoElect.motor.area import Area
chrome = None
velocity = None
running = None
isLoguin = False
areas = []
dirAreas = [
"data/_001.json",
"data/_002.json",
"data/_003.json",
"data/_004.json",
"data/_005.json"
]
def chargeAreas():
	global areas
	cantTemp = 0
	for dir in  dirAreas:
		with open(dir, encoding="utf-8") as file:
			data = json.load(file)
			title = data["title"]
			link = data["link"]
			reply = data["reply"]
			areas.append(Area(cantTemp, title, link, reply, False))
			cantTemp = cantTemp + 1
			print(areas)
