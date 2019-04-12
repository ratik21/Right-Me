
import pyxhook
from autocorrect import spell
import pyautogui
import enchant
import short_gui as short_gui
d = enchant.Dict("en_US")
word = ""
new_hook=pyxhook.HookManager()
#selection = 'suggestion'
selection = 'suggestion'
def change(word):
	global selection
	selection = word

def printCorrect(word):
	word_new = spell(word)
	if word_new!=word:
		for i in word:
			pyautogui.press('backspace')
		pyautogui.press('backspace')
		pyautogui.typewrite(word_new+" ") 

def print_suggested_word(word_new):
	global word
	for i in word:
		pyautogui.press('backspace')
	pyautogui.press('backspace')
	pyautogui.typewrite(word_new+" ")

def OnKeyPress(event):
	global word
	global new_hook
	if event.Ascii == 96:
		new_hook.cancel()
	if (event.Ascii >= 65 and event.Ascii <= 90) or (event.Ascii >= 97 and event.Ascii <= 122): 
		word += event.Key
	if event.Ascii == 32:
		if selection == "corrector":
			printCorrect(word)
		else:
			short_gui.set_list(suggest_list(word))
		word = ""

def suggest_list(word):
	global d
	return d.suggest(word)

def main():
	global new_hook
	#listen to all keystrokes
	new_hook.KeyDown=OnKeyPress
	#hook the keyboard
	new_hook.HookKeyboard()
	#start the session
	new_hook.start()
