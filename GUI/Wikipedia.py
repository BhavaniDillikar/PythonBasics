import wikipedia
from tkinter import *
from tkinter.messagebox import showinfo
win = Tk()
win.title('Wikipedia')
win.geometry('200x70')

def searchWiki():
    search = entry.get()
    answer = wikipedia.summary(search)
    showinfo("Wikipedia Answer", answer)


# Creating Label
label = Label(win, text="Wiki Search :")
label.grid(row=0, column=0)

# Creating TextBox/Entry
entry = Entry(win)
entry.grid(row=0, column=1)

# Creating Button
button = Button(win, text="Search", command=searchWiki)
button.grid(row=1, column=1, padx=10)

win.mainloop()