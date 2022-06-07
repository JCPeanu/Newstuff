from tkinter import font
import PySimpleGUI
import random

with open("Josh.txt", "r") as my_file:
    Counter = 0
    Content = my_file.readlines()
    CoList = Content

PySimpleGUI.theme('Dark Brown')
layout = [[PySimpleGUI.Text('Palindromes Finder', font=("Georgia", 25))],
          [PySimpleGUI.Text('Input a list of words and I will search for a palindrome in it.\nPlease enter like my format.')],
          [PySimpleGUI.Multiline(default_text = "Racecar\nMadam\nSup", key = "-INPUT-")],
          [PySimpleGUI.Button('Find')],
          [PySimpleGUI.Text('Word: ', key = "-OUTPUT-")],
          [PySimpleGUI.Button('Exit')]]

window = PySimpleGUI.Window('Example 5', layout)
 
while True:  # Event Loop
    event, values = window.read()
    if event in (PySimpleGUI.WIN_CLOSED, 'Exit'):
        break
    while event in ('Find'):
        lst = values['-INPUT-'].splitlines()
        num = random.randint(0, len(lst) - 1)
        wrd = lst[num].lower()
        new_wrd = ""
        for i in range (len(wrd)-1, -1, -1):
            new_wrd += wrd[i]
        if wrd == new_wrd:
            window['-OUTPUT-'].update("Word: " + lst[num])
            break
        else:
            cnt = 0
            while wrd != new_wrd:
                num = random.randint(0, len(lst) - 1)
                wrd = lst[num].lower()
                new_wrd = ""
                cnt += 1
                for i in range (len(wrd)-1, -1, -1):
                    new_wrd += wrd[i]
                if wrd == new_wrd:
                    window['-OUTPUT-'].update("Word: " + lst[num])
                if cnt > len(lst) * 5:
                    window['-OUTPUT-'].update("Word: No Palindrome Found")
                    break
window.close()