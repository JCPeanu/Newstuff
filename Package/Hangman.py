import PySimpleGUI
import random
 
#method that picks a random word from the text file
def pick_word():
    dictionary = open("Package/list_of_words_in_english.txt", "r")
    all_words = list()
    previous_word = " "
    last_word_reached = False
    while not last_word_reached:
            current_word = dictionary.readline()
            current_word = current_word.rstrip("\n")
            if current_word == previous_word:
                last_word_reached = True
            else:
                all_words.append(current_word)
            #print("Previous word is ", previous_word)
            #print("Current word is ", current_word)
            #print("...")
            previous_word = current_word
    dictionary.close()
    #print(all_words)
    word = random.choice(all_words).upper()
    return word
 
#pick the word
word = pick_word()
#print it on console
print(word)
 
# Define the window's contents
layout = [ [ PySimpleGUI.Text("Let's play hangman!") ],
           #https://github.com/PySimpleGUI/PySimpleGUI/blob/master/DemoPrograms/Demo_Color_Names_Smaller_List.py (list of colors)
           [ PySimpleGUI.Graph(canvas_size=(350, 350), graph_bottom_left=(0, 0), graph_top_right=(350, 350), background_color='NavajoWhite2', enable_events=False, key='graph')],
           [ PySimpleGUI.Text("Guess this word: "), PySimpleGUI.Text( size=(20,1), key='-WORD-') ],
           [ PySimpleGUI.Text("Letters used: "), PySimpleGUI.Text(size=(20,1), key='-LETTERS_USED-') ],
           [ PySimpleGUI.Text("Attempts left: "), PySimpleGUI.Text(size=(20,1), key='-ATTEMPTS_LEFT-') ],
           [ PySimpleGUI.Text("Enter next letter: "), PySimpleGUI.Input(size=(10,1), key='-INPUT-') ], #The input now must be referred by it's keyword
           [ PySimpleGUI.Text(size=(40,1), key='-ALERT-', text_color='red')], #40 characters wide, 1 character high
           [ PySimpleGUI.Button('Continue'), PySimpleGUI.Button('Give up'), PySimpleGUI.Button('Quit') ] ]
 
# Create the window. Since we are drawing, finalize=True must appear
window = PySimpleGUI.Window('Hangman!', layout, finalize=True)
 
#a nickname for the graph part of the window
graph = window['graph']
 
#draw the structure
graph.draw_line((20, 15), (160, 15), width=10)
graph.draw_line((90, 15), (90, 335), width=10)
graph.draw_line((85, 335), (250, 335), width=10)
graph.draw_line((250, 340), (250, 280), width=5)
#draw the head
graph.draw_circle((250, 245), 35, line_width=3)
#draw the body
graph.draw_rectangle((210, 210), (290, 90), line_width=3)
 
#letters_guessed is a list containing the letters previously input by the user
letters_guessed = list()
#name is self explanatory
opportunities_left = 5
#I'm using a boolean variable to stop manually the program to require user to press Submit again
#Remember the main window is being run through an infinite loop, so a manual stop is necessary here
move_on = True
#even though player wins by default, at the beginning of every loop it changes to false unless the user has guessed the word
player_wins = True
 
# Display and interact with the Window using an (infinite) Event Loop
while True:
    #checks letter by letter, if one letter is not in the letters guessed, then user has not won yet
    for letter in word:
        if letter.upper() not in letters_guessed: #I'm using upper to convert everything to uppercase, to maintain a standard
            player_wins = False
    #end game if player wins after checking every letter
    if player_wins == True:
        window["-ALERT-"].update("You won!!!")
    #but if the user hasn't won and there are no opportunities left, then the user lost
    elif opportunities_left == 0:
        window["-ALERT-"].update("You lost! The word was "+word.lower()+".")
    #Show the number of opportunities left in the space in the window destined for it
    window["-ATTEMPTS_LEFT-"].update(opportunities_left)
    #Display the letters guessed in their respective space
    window["-LETTERS_USED-"].update(' '.join(letters_guessed))
    #Now, the following variable is the w_rd to be gue__ed by the user, starting with an empt_ string
    guess_this = ""
    #if the letter is inside the list of letters guess, then display it
    for letter in word:
        if letter in letters_guessed:
            guess_this += letter
        #otherwise, hide it
        else:
            guess_this += " _ "
    #Now display that String in its respective space
    window["-WORD-"].update(guess_this)
    #Ok, now that everything is displayed, then read the input from the user
    event, values = window.read() #event->buttons, values->a list that contains the last letter input
    #But first, check if the letter is repeated, and halt the program until the user inputs a valid letter
    if values['-INPUT-'].upper() in letters_guessed:
        move_on = False
        window["-ALERT-"].update("This letter was already used!")
    #This part was the trickiest one, if the letter input is just the last one to be guessed, then the player won
    else:
        letters_guessed.append(values['-INPUT-'].upper())
        for letter in word:
            if values['-INPUT-'].upper() not in letters_guessed:
                player_wins = False
                break
            player_wins = True
    # See if user wants to quit or window was closed
    if event == PySimpleGUI.WINDOW_CLOSED or event == 'Quit':
        break
    #if the user presses the Give up button, show the answer
    if event == 'Give up':
        window["-ALERT-"].update("You lost! The word was "+word.lower()+".")
        opportunities_left = 0
    # This chain of conditionals checks manually if the letter isn't in the word, and reduce the opportunities by one
    #Notice the manual stop, if it weren't there, it would countdown to 0 in the first input
    if move_on and values['-INPUT-'].upper() not in word and opportunities_left == 5:
        #draw an arm
        graph.draw_rectangle((210, 210), (160, 170), line_width=3)
        opportunities_left = 4
        move_on = False
    if move_on and values['-INPUT-'].upper() not in word and opportunities_left == 4:
        #draw another arm
        graph.draw_rectangle((290, 210), (340, 170), line_width=3)
        opportunities_left = 3
        move_on = False
    if move_on and values['-INPUT-'].upper() not in word and opportunities_left == 3:
        #draw a leg
        graph.draw_rectangle((290, 90), (255, 20), line_width=3)
        opportunities_left = 2
        move_on = False
    if move_on and values['-INPUT-'].upper() not in word and opportunities_left == 2:
        #draw another leg
        graph.draw_rectangle((210, 90), (245, 20), line_width=3)
        opportunities_left = 1
        move_on = False
    if move_on and values['-INPUT-'].upper() not in word and opportunities_left == 1:
        #draw the face
        graph.draw_line((275, 255), (255, 265), width=3)
        graph.draw_line((245, 255), (225, 265), width=3)
        graph.draw_line((255, 255), (275, 265), width=3)
        graph.draw_line((225, 255), (245, 265), width=3)
        graph.draw_line((225, 225), (275, 225), width=3)
        opportunities_left = 0
        move_on = False
    #The continue variable is reset to allow the continuation of the code
    move_on = True
 
# Finish up by removing from the screen
window.close()