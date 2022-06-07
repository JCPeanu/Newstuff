# Examples on how to use PySimpleGUI :)
# importing the Graphical User Interface library
from tkinter import font
import PySimpleGUI  # as sg #if you want to put a shorter alias to the library
 
# Example 1
# """
# PySimpleGUI.Window(title="Example 1", background_color = "#5A5A5A", layout=[[]], margins=(160, 90)).read()
# """
 
# Example 2
# """
# The layout is what you put inside the window
layout = [ [PySimpleGUI.Text("Click the button to close")], [PySimpleGUI.Button("OK")] ]
 
# Create the window
window = PySimpleGUI.Window("Example 2", layout, margins=(80, 45))
 
# Create an event loop
while True: #keeps repeating this output as long as nothing is changed
    event, values = window.read()
    # End program if user closes window or presses the OK button
    if event == "OK" or event == PySimpleGUI.WIN_CLOSED:
        break
 
window.close()
# """
 
# Example 3
"""
# Define the window's contents
layout = [ [PySimpleGUI.Text("What's your name?")], 
           [PySimpleGUI.Input()], 
           [PySimpleGUI.Button('OK')] ]
 
# Create the window
window = PySimpleGUI.Window('Example 3', layout)
 
# Display and interact with the Window
event, values = window.read()
 
# Do something with the information gathered
print('Hello', values[0], "\b, nice to meet you!") #This is a Python command, so it's printed on the console
 
# Finish up by closing the window
window.close()
 
"""
 
# Example 4
"""
# Define the window's contents
layout = [ [ PySimpleGUI.Text("Input a color:") ],
           [ PySimpleGUI.Input(key='-INPUT-') ], #The input now must be referred by it's keyword
           [ PySimpleGUI.Text(size=(40,1), key='-OUTPUT-') ], #40 characters wide, 1 character high
           [ PySimpleGUI.Button('Ok'), PySimpleGUI.Button('Quit') ] ]
 
# Create the window
window = PySimpleGUI.Window('Example 4', layout, margins=(80, 45))
 
# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == PySimpleGUI.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    window['-OUTPUT-'].update(values['-INPUT-'].title() + " is nice, can you give me another color?") #
 
# Finish up by removing from the screen
window.close()
"""


# font_str = "Helvectica "
# font_size = 25
# layout = [
#     [PySimpleGUI.Text("Input a font name:", font = ('font_str', font_size), key = '-TEXT-')],
#     [PySimpleGUI.Input()],
#     [PySimpleGUI.Text("Input the font size: ", font = ('font_str', font_size))],
#     [PySimpleGUI.Input()],
#     [PySimpleGUI.Button('Ok'), PySimpleGUI.Button('QUIT')]
# ]
# window = PySimpleGUI.Window('Self Example', layout)
# text_elem = window['-TEXT-']
# while True:
#     event, values = window.read()
#     if event == PySimpleGUI.WINDOW_CLOSED or event == 'QUIT':
#         break
#     print(values[0])
#     print(values[1])
#     text_elem.update(font=(values[0], values[1]))


# Example 5
"""
PySimpleGUI.theme('Dark Brown')
layout = [[PySimpleGUI.Text('Theme browser', font=("Georgia", 25))],
          [PySimpleGUI.Text('Click a Theme color to see demo window')],
          [PySimpleGUI.Listbox(values=PySimpleGUI.theme_list(), size=(20, 12), key='-LIST-', enable_events=True)],
          [PySimpleGUI.Button('Exit')]]
 
window = PySimpleGUI.Window('Example 5', layout)
 
while True:  # Event Loop
    event, values = window.read()
    if event in (PySimpleGUI.WIN_CLOSED, 'Exit'):
        break
    PySimpleGUI.theme(values['-LIST-'][0])
    PySimpleGUI.popup_get_text('This is {}'.format(values['-LIST-'][0]))
 
window.close()
 
"""
 
# Example 6
"""
import tkinter #since PySimpleGUI imports the fonts from tkinter, we have to work with it
root = tkinter.Tk() #another window opens, just ignore it
PySimpleGUI.theme('Topanga')
layout = [[PySimpleGUI.Text('Font browser', font=("Arial", 25))],
          [PySimpleGUI.Text('Click a Theme color to see demo window')],
          [PySimpleGUI.Listbox(values=tkinter.font.families(), size=(20, 12), key='-LIST-', enable_events=True)],
          [PySimpleGUI.Button('Exit')]]
 
window = PySimpleGUI.Window('Example 6', layout)
 
while True:  # Event Loop
    event, values = window.read()
    if event in (PySimpleGUI.WIN_CLOSED, 'Exit'):
        break
    PySimpleGUI.theme("reddit")
    PySimpleGUI.popup_get_text('This is {}'.format(values['-LIST-'][0]), font=(values['-LIST-'][0], 50, "italic"))
 
window.close()
"""
 
# Example 7
"""
layout = [[PySimpleGUI.Graph(canvas_size=(400, 400), graph_bottom_left=(0, 0), graph_top_right=(400, 400),
                             background_color='red', enable_events=True, key='graph')],
          [PySimpleGUI.Text('Change circle color to:'), PySimpleGUI.Button('Red'), PySimpleGUI.Button('Blue'),
           PySimpleGUI.Button('Move')]]
 
window = PySimpleGUI.Window('Example 7', layout, finalize=True)
 
graph = window['graph']  # type: PySimpleGUI.Graph
circle = graph.draw_circle((75, 75), 25, fill_color='black', line_color='white')
point = graph.draw_point((75, 75), 10, color='green')
oval = graph.draw_oval((25, 300), (100, 280), fill_color='purple', line_color='purple')
rectangle = graph.draw_rectangle((25, 300), (100, 280), line_color='purple')
line = graph.draw_line((0, 0), (100, 100))
arc = graph.draw_arc((0, 0), (400, 400), 160, 10, style='arc', arc_color='blue')
poly = graph.draw_polygon(((10, 10), (20, 0), (40, 200), (10, 10)), fill_color='green')
while True:
    event, values = window.read()
    print(event, values)
    if event == PySimpleGUI.WIN_CLOSED:
        break
    if event in ('Blue', 'Red'):
        graph.TKCanvas.itemconfig(circle, fill=event)
    elif event == 'Move':
        graph.MoveFigure(point, 10, 10)
        graph.MoveFigure(circle, 10, 10)
        graph.MoveFigure(oval, 10, 10)
        graph.MoveFigure(rectangle, 10, 10)
        graph.MoveFigure(arc, 10, 10)
        graph.MoveFigure(poly, 10, 10)
 
window.close()
# """
 
# Final example!
# """
PySimpleGUI.ChangeLookAndFeel('GreenTan')
 
# ------ Menu Definition ------ #
menu_def = [['File', ['Open', 'Save', 'Exit', 'Properties']],
            ['Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
            ['Help', 'About...'], ]
 
# ------ Column Definition ------ #
column1 = [[PySimpleGUI.Text('Column 1', background_color='#F7F3EC', justification='center', size=(10, 1))],
            [PySimpleGUI.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 1')],
            [PySimpleGUI.Spin(values=('1', 'Spin Box 2', '3'), initial_value='Spin Box 2')],
            [PySimpleGUI.Spin(values=('1', '2', 'Spin Box 3'), initial_value='Spin Box 3')]]
 
layout = [
    [PySimpleGUI.Menu(menu_def)],
    [PySimpleGUI.Text('All graphic widgets in one window!', size=(30, 1), justification='center', font=("Arial", 25), relief=PySimpleGUI.RELIEF_RIDGE)],
    [PySimpleGUI.Text('Here is some text.... and a place to enter text')],
    [PySimpleGUI.InputText('This is my text')],
    [PySimpleGUI.Frame(layout=[ [PySimpleGUI.Checkbox('Checkbox', size=(10,1)),  PySimpleGUI.Checkbox('My second checkbox!', default=True)],
        [PySimpleGUI.Radio('My first Radio!     ', "RADIO1", default=True, size=(10,1)), PySimpleGUI.Radio('My second Radio!', "RADIO1")]],
            title='Options', title_color='red', relief=PySimpleGUI.RELIEF_SUNKEN, tooltip='Use these to set flags')],
    [PySimpleGUI.Multiline(default_text='This is the default Text should you decide not to type anything', size=(35, 3)),
        PySimpleGUI.Multiline(default_text='A second multi-line', size=(35, 3))],
    [PySimpleGUI.InputCombo(('Combobox 1', 'Combobox 2'), size=(20, 1)),
        PySimpleGUI.Slider(range=(1, 100), orientation='h', size=(34, 20), default_value=85)],
    [PySimpleGUI.InputOptionMenu(('Menu Option 1', 'Menu Option 2', 'Menu Option 3'))],
    [PySimpleGUI.Listbox(values=('Listbox 1', 'Listbox 2', 'Listbox 3'), size=(30, 3)),
        PySimpleGUI.Frame('Labelled Group',[[
        PySimpleGUI.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=25),
        PySimpleGUI.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=75),
        PySimpleGUI.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=10),
        PySimpleGUI.Column(column1, background_color='#F7F3EC')]])],
    [PySimpleGUI.Text('_'  * 80)],
    [PySimpleGUI.Text('Choose A Folder', size=(35, 1))],
    [PySimpleGUI.Text('Your Folder', size=(15, 1), auto_size_text=False, justification='right'),
        PySimpleGUI.InputText('Default Folder'), PySimpleGUI.FolderBrowse()],
    [PySimpleGUI.Submit(tooltip='Click to submit this window'), PySimpleGUI.Cancel()]
]
 
window = PySimpleGUI.Window('Final example!', layout, default_element_size=(40, 1), grab_anywhere=False)
 
event, values = window.read()
 
window.close()
 
PySimpleGUI.popup('Title',
            'The results of the window.',
            'The button clicked was "{}"'.format(event),
            'The values are', values)
# """



# import PySimpleGUI as sg

# '''
#     App that shows "how fonts work in PySimpleGUI".
# '''

# layout = [[sg.Text('This is my sample text', size=(20, 1), key='-text-')],
#           [sg.CB('Bold', key='-bold-', change_submits=True),
#            sg.CB('Italics', key='-italics-', change_submits=True),
#            sg.CB('Underline', key='-underline-', change_submits=True)],
#           [sg.Slider((6, 50), default_value=12, size=(14, 20),
#                      orientation='h', key='-slider-', change_submits=True),
#            sg.Text('Font size')],
#           [sg.Text('Font string = '), sg.Text('', size=(25, 1), key='-fontstring-')],
#           [sg.Button('Exit')]]

# window = sg.Window('Font string builder', layout)

# text_elem = window['-text-']
# while True:     # Event Loop
#     event, values = window.read()
#     if event in (sg.WIN_CLOSED, 'Exit'):
#         break
#     font_string = 'Helvetica '
#     font_string += str(int(values['-slider-']))
#     if values['-bold-']:
#         font_string += ' bold'
#     if values['-italics-']:
#         font_string += ' italic'
#     if values['-underline-']:
#         font_string += ' underline'
#     text_elem.update(font=font_string)
#     window['-fontstring-'].update('"'+font_string+'"')
#     print(event, values)

# window.close()