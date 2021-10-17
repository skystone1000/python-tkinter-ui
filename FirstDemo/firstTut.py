# Setup
"""
    Install "pytk" module for using tkinter
"""

# Simple Project : https://www.youtube.com/watch?v=_lSNIrR1nZU

# Imports
from tkinter import *


# Key Down Function
def click():
    entered_text = textentry.get()  # This will collect text from the ext entry box
    output.delete(0.0, END)
    try:
        definition = my_compdictionary[entered_text]
    except:
        definition = "Sorry there is no such word"
    output.insert(END, definition)


# Exit Function
def close_window():
    window.destroy()
    exit()


# Main
window = Tk()
window.title("To Do List")

# Photo
photo1 = PhotoImage(file="./Assets/logo.png")
Label(window, image=photo1, bg="black").grid(row=0, column=0, sticky=E)

# Label
Label(window, text="Enter the word to get definition:", bg="black", fg="white", font="none 12 bold").grid(row=1,
                                                                                                          column=0,
                                                                                                          sticky=W)

# Text Entry Box
textentry = Entry(window, width=20, bg="white")
textentry.grid(row=2, column=0, sticky=W)

# Submit Button
Button(window, text="SUBMIT", width=6, command=click).grid(row=3, column=0, sticky=W)

# Label (Another label)
Label(window, text="\nDefinition:", bg="black", fg="white", font="none 12 bold").grid(row=4, column=0, sticky=W)

# Text Box
output = Text(window, width=75, height=6, wrap=WORD, background="white")
output.grid(row=5, column=0, columnspan=2, sticky=W)

# Dictionary
my_compdictionary = {
    'algorithm': 'Step by Step instructions to complete a task',
    'bug': 'Piece of code that causes a program to fail'
}

# Exit Label
Label(window, text="Click on following button to Exit:", bg="black", fg="white", font="none 12 bold").grid(row=6,
                                                                                                           column=0,
                                                                                                           sticky=W)

# Exit Button
Button(window, text="Exit", width=14, command=close_window).grid(row=7, column=0, sticky=W)

# Run Main Loop
window.mainloop()
