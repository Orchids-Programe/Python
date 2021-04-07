import os
import keyboard
# on window platform
clear = lambda: os.system('cls')
#on linux platform
#clear = lambda: os.system('clear')
f = open('demofile.txt', encoding = 'utf-8')
content = f.readlines()
current = 0
def printLineUp():
     clear()
     global current
     current -=1
     if current <= -(len(content)):
        current = 0
     print(content[current])

def printLineDown():
     clear()
     global current
     current +=1
     if(current >= len(content)):
        current =0
     print(content[current%len(content)])

keyboard.add_hotkey('up', printLineUp)
keyboard.add_hotkey('down', printLineDown)
keyboard.wait('esc')