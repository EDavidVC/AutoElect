from selenium import webdriver
from AutoElect.values import Constants

from AutoElect.motor import main
def initValues():
	Constants.chrome = webdriver.Chrome("data/chromedriver.exe")
	Constants.velocity = 0
	Constants.running = True
	Constants.isLoguin = False
	Constants.chargeAreas()
if(__name__ == "__main__"):
	initValues()
	main.start_main()