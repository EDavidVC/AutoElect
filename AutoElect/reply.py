from AutoElect.values import Constants
from selenium.webdriver import ActionChains
import time
#01 - NORMAL
def normal(answer): #01
	for i in Constants.chrome.find_elements_by_class_name("_mc"):
		if(i.text == answer and i.is_displayed()):
			Constants.chrome.execute_script("arguments[0].click();", i)
#02 - Press Element
def push_css(answer): #02_css
	for i in answer:
		element = Constants.chrome.find_element_by_css_selector(i)
		element.click()

def push_id(answer): #02_id
	for i in answer:
		Constants.chrome.execute_script("arguments[0].click();", Constants.chrome.find_element_by_id(i))

def push_class(answer): #02_class
	for i in answer:
		for element in Constants.chrome.find_elements_by_class_name(i):
			if(element.is_displayed()):
				element.click()

def push_id_cant(answer): #02_id_cant
	for i in answer:
		Constants.chrome.execute_script("arguments[0].click();", Constants.chrome.find_element_by_id(i))

#03 - changeStyle
#03_ids
def change_style_ids(answer):
	for i in answer:
		for element in Constants.chrome.find_elements_by_id(i):
			Constants.chrome.execute_script('arguments[0].style = "'+answer[i]+'"', element);



#04 - True or False
def trueOrFalse(answer): #04
	for i in answers:
		Constants.chrome.execute_script("arguments[0].click();", Constants.chrome.find_element_by_id(i).find_element_by_class_name(answer[i]))
#05 - Insert data in text box
def fill(answer): #05
	for input in Constants.chrome.find_elements_by_xpath("//input[@aria-label='Escribe una respuesta.']"):
		if(input.is_displayed()):
			input.send_keys(answer)

#06 - Drag and Drop
def drag_drop_id_id(answer):
	for i in answer:
		ActionChains(Constants.chrome).drag_and_drop(Constants.chrome.find_element_by_id(i),Constants.chrome.find_element_by_id(answer[i])).perform()

def drag_drop_css_css(answer):
	for i in answer:
		ActionChains(Constants.chrome).drag_and_drop(Constants.chrome.find_element_by_css_selector(i),Constants.chrome.find_element_by_css_selector(answer[i])).perform()

def drag_drop_x_x(answer):
	for i in answer:
		ActionChains(Constants.chrome).drag_and_drop(Constants.chrome.find_element_by_xpath(i),Constants.chrome.find_element_by_xpath(answer[i])).perform()

def drag_drop_id_offset(answer):
	ActionChains(Constants.chrome).drag_and_drop_by_offset(Constants.chrome.find_element_by_id(answer["element"]), int(answer["x"]), int(answer["y"])).click().perform()
#end - this function is active in the final of course
def end():
	Constants.chrome.find_element_by_class_name("_ok").submit()




def trueOrFalse(answers):
	for i in answers:
		Constants.chrome.execute_script("arguments[0].click();", Constants.chrome.find_element_by_id(i).find_element_by_class_name(answers[i]))		
def selectInTable(txtElement):
	for i in Constants.chrome.find_elements_by_css_selector("td"):
		if(i.text == txtElement):
			Constants.chrome.execute_script("arguments[0].click();", i)
			break

def send_OK():
	Constants.chrome.find_element_by_class_name("_ok").submit() #enviado

def nextNav(page):
	Constants.chrome.execute_script("arguments[0].click();", Constants.chrome.find_element_by_id("_pages").find_element_by_xpath("div[@class='_page _active']").find_element_by_class_name("_tabs").find_element_by_xpath("div[@num='"+str(page)+"']"))
	time.sleep(1)

def nextNavigation(page):
	Constants.chrome.execute_script("arguments[0].click();", Constants.chrome.find_element_by_id("_navigation").find_element_by_class_name("_tabs").find_element_by_xpath("//div[@num='"+str(page)+"']"))
	Constants.chrome.execute_script("arguments[0].click();", Constants.chrome.find_element_by_id("_pages").find_element_by_xpath("div[@class='_page _active']").find_element_by_class_name("_tabs").find_element_by_xpath("div[@num='0']"))