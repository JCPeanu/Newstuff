import PySimpleGUI

PySimpleGUI.ChangeLookAndFeel('GreenTan')
 
layout = [
    [PySimpleGUI.Text("It's the time of the year again!", size=(30, 1), justification='center', font=("Arial", 25), relief=PySimpleGUI.RELIEF_RIDGE)],
    [PySimpleGUI.Text("Input your monthly salary: ", size=(30, 1))],
    [PySimpleGUI.Input(default_text = 0, key  = "-INPUT-")],
    [PySimpleGUI.Text("Input your asset wroth: ", size=(30, 1))],
    [PySimpleGUI.Input(default_text = 0, key = "-INPUT2-")],
    [PySimpleGUI.Checkbox('Yes, I am exempt from paying taxes.', size=(50,1), key = "-INPUT3-", default = False)],
    [PySimpleGUI.Text("You have to pay: $ ", size=(40, 1), key = "-OUTPUT-")],
    [PySimpleGUI.Button('Recalculate')],
    [PySimpleGUI.Button('Quit')]
]
 
window = PySimpleGUI.Window('Tax Calculator', layout, default_element_size=(40, 1), grab_anywhere=False)
 
while True:
    event, values = window.read()
    money = int(values["-INPUT-"])
    asset_wth = int(values["-INPUT2-"])
    yes = values["-INPUT3-"]
    if event == PySimpleGUI.WIN_CLOSED or event == "Quit":
        break
    if event == "Recalculate":
        if money < 100 or yes:
            window['-OUTPUT-'].update("You have to pay: $0")
        elif asset_wth*0.2 > 1000:
            total = int((money*0.05))
            window['-OUTPUT-'].update("You have to pay: $" + str(total))
        else:
            total = int(money*0.05 + asset_wth*0.2)
            window['-OUTPUT-'].update("You have to pay: $" + str(total))
window.close()