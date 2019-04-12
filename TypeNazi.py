print("Initialising your app ....... ")
import pyxhook
from autocorrect import spell
import pyautogui
import enchant
word = ""
new_hook=pyxhook.HookManager()
def printCorrect(word):
	word_new = spell(word)
	if word_new!=word:
		for i in word:
			pyautogui.press('backspace')
		pyautogui.press('backspace')
		pyautogui.typewrite(word_new+" ") 
		#print(word_new, end=' ', flush=True)

def OnKeyPress(event):
	global word
	global new_hook
	if event.Ascii == 96:
		new_hook.cancel()
	if (event.Ascii >= 65 and event.Ascii <= 90) or (event.Ascii >= 97 and event.Ascii <= 122): 
		word += event.Key
	if event.Ascii == 32:
		printCorrect(word)
		word = ""

def main():
	global new_hook
	#listen to all keystrokes
	new_hook.KeyDown=OnKeyPress
	#hook the keyboard
	new_hook.HookKeyboard()
	#start the session
	new_hook.start()
#main()
"""
word = ""


printcor

onkeypress
	global word
	word += newchar

class TypeCOrr:
	def __init__
		self.word = ""

	def onkey

"""	
