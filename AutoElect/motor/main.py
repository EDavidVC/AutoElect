from AutoElect.motor.area import StartArea
from AutoElect.values import Constants
import os
import sys

list_us_pass = [
["Luis Francisco", "000824176", "luis12345"],
["Yony Brayan", "001219138", "yonybrayanccallo"]
]
def start_main():
	while(Constants.running):
		os.system("cls")
		if(not Constants.isLoguin):
			temp = 0
			print("SEECCIONE SU USUARIO")
			for user in list_us_pass:
				print(str(temp) +" "+ user[0])
				temp+=1
			us = int(input("INGRESE SU USUARIO: "))
			login(us)

		else:
			selectCourses()

def login(id):
	#Login
	#Charge page of Login
	Constants.chrome.get("https://arequipa-puno.electude.com/slogin")
	#SHOW
	print("Iniciando como: " +list_us_pass[id][0])
	#Insert USERNAME
	print("Inserting USER")
	Constants.chrome.find_element_by_name("name").send_keys(list_us_pass[id][1])
	print("OK..")
	#Insert Password
	print("Inserting Password")
	Constants.chrome.find_element_by_name("password").send_keys(list_us_pass[id][2])
	print("OK")
	print("LOGINNG......")
	Constants.chrome.find_element_by_class_name("button").submit()
	print("All is OK Your Account is Logged")
	Constants.isLoguin = True

def selectCourses():
	print("Selecciona curso")
	cantTemp = 0
	for s in Constants.areas:
		print(str(cantTemp) + " - " + s.getTitle() + " - " + str(s.getIsCharge()))
		cantTemp+=1

	print("x .-. Salir")
	select = input("INGRESE SU SELECCION: ")
	if(select == "x"):
		print("Saliendo")
		sys.exit()
	else:
		StartArea(Constants.areas[int(select)], int(input("Ingrese Cantidad: ")))

	