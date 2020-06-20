from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import pyperclip 
import pyautogui
import time
import queue
from pynput.keyboard import Key, Controller

global keyboard 
keyboard = Controller()

def paste(data):
	pyperclip.copy(data);
	keyboard.press(Key.cmd)
	keyboard.press('v')
	keyboard.release('v')
	keyboard.release(Key.cmd)
	time.sleep(0.1)


def initCards(numCards):
	# add 30 empty cards to quizlet
	#Coordinates
	xcard = 630
	ycard = 610
	xhead = 60
	yhead = 340
	pyautogui.moveTo(xcard,ycard)
	for i in range(1, numCards):
		time.sleep(0.5)
		pyautogui.scroll(-100) 
		pyautogui.click()

	#scroll to top of page
	time.sleep(2)
	pyautogui.scroll(1000) 
	#Click on header box
	pyautogui.moveTo(xhead, yhead)
	pyautogui.click()


#create button location
x = 1200
y = 120

# exit share screan location
x1 = 890
y1 = 165

# create new set button
x2 = 488
y2 = 120


time.sleep(5)
secs_between_keys = 1

fileName = "10A.html"

raw_html = open(fileName).read()
soup = BeautifulSoup(raw_html, 'html.parser')

# will contain all box headings
headings = []

boxes = soup.find_all("thead")

for i in boxes:
	text = i.find("button").getText().strip()
	headings.append(text)

vocabSection = soup.find_all("tbody")


for i in range(0, len(boxes)):
	pyautogui.moveTo(x2, y2) #click create new set
	pyautogui.click()
	time.sleep(5)
	initCards(30)
	time.sleep(3)
	heading = headings[i]
	paste(heading)
	pyautogui.typewrite("\t\t", interval = secs_between_keys)
	section = vocabSection[i]
	vocabList = section.find_all("tr")
	for vocab in vocabList:
		french = vocab.find("th").find("button", "c-no-button js-target").getText().strip()
		english = vocab.find("td").find("button", "c-no-button c-table__translation js-translation").getText().strip()
		paste(french)
		pyautogui.typewrite("\t", interval = secs_between_keys)
		paste(english)
		pyautogui.typewrite("\t", interval = secs_between_keys)
	pyautogui.moveTo(x, y) #click create button
	pyautogui.click()
	time.sleep(6)
	pyautogui.moveTo(x1, y1) #click dont share butten
	pyautogui.click()
	time.sleep(5)
