#! /usr/bin/python3
import tkinter as tk
import bingo
from tkinter import messagebox
import sys
from tkinter import ttk
# constants
BUTTON_WIDTH = 25
BINGOBUTTON_WIDTH = 10
SCREEN_GEOMETRY = "600x600"
ENTRY_WIDTH = 300

args = sys.argv
args_given = len(args)

# main window
root = tk.Tk()
root.title('BINGO TIMEEE!!!')
root.geometry(SCREEN_GEOMETRY)

#
# Error message
#
def showError(title : str = "Error", description : str = "Unknown error occured"):
   messagebox.showerror(title, "Error: " + description)

#
# Bingobutton
#
def bingoBtn(root, text ):
    def tick():
        btn.config(bg="red", activebackground="red", command=untick)
    def untick():
        btn.config(bg="white", activebackground="white", command=tick)


    btn = tk.Button(root, bg="white", activebackground="white",text=text, width=BINGOBUTTON_WIDTH, height=BINGOBUTTON_WIDTH//2, command=tick, justify=tk.LEFT, wraplength=80)
    return btn

#
# file entry window
#

def fileEntry():
    screen = tk.Frame(root)
    
    def submit():
        filename = fileEntry.get()
        try:
            b = bingo.Bingo(filename=filename)
            bingoScreen(b, b.isBig() and not 'selected' in tinyCheckbox.state()).pack()
            screen.destroy()
        except:
            showError("File not found", "Could not find the file :(")

    titleLbl = tk.Label(screen, text=f"Input filename:")

    fileEntry = tk.Entry(screen, width=ENTRY_WIDTH)
    submitBtn = tk.Button(screen, text='Submit', width=BUTTON_WIDTH, command=submit)
    tinyCheckbox = ttk.Checkbutton(screen, text='Force tiny bingo')
    titleLbl.pack()
    fileEntry.pack()
    submitBtn.pack()
    tinyCheckbox.pack()

    return screen

def bingoScreen(pBingo : bingo.Bingo, pIsBig):

    screen = tk.Frame(root)

    
    titleLbl = tk.Label(screen, text=f"BINGO:")
    titleLbl.pack()
    screen.pack()
    screen = tk.Frame(root)

    if pIsBig:
        size = 5
        texts = pBingo.getBingo(25)
    else:
        size = 4
        texts = pBingo.getBingo()

    for i in range(size**2):
        row = i // (size)
        col = i % (size)
        bingoBtn(screen, texts[i]).grid(row=row, column=col)

    return screen


if args_given == 2:
    b = bingo.Bingo(filename=args[1])
    bingoScreen(b, b.isBig()).pack()
elif args_given == 3:
    b = bingo.Bingo(filename=args[1])
    bingoScreen(b, args[2]!="-t" and b.isBig()).pack()
else:
    fileEntry().pack()
root.mainloop()
