from tkinter import *
from tkinter import ttk
import time

root = Tk()
root.title("Typing Speed Test")
root.minsize(1000, 600)
root.maxsize(1000, 600)
your_words = Text(root)
cpm_label = Label(root)
wpm_label = Label(root)
missed_label = Label(root)


def start():
    your_words.grid(column=0, row=1)
    your_words.focus()
    root.after(60000, get)


def get():
    text = your_words.get('1.0', 'end')
    chars_typed = len(text)
    words = text.split(" ")
    text_to_grade = type_test[:chars_typed]
    missed_letters = -1

    your_words.grid_remove()

    for i in range(0, chars_typed):
        if text[i] != text_to_grade[i]:
            missed_letters += 1

    print(chars_typed)
    print(words)
    print(missed_letters)
    print(text_to_grade)
    cpm_label.configure(text=f"Characters typed per minute = {chars_typed}")
    wpm_label.configure(text=f"Words typed per minute = {len(words)}")
    missed_label.configure(text=f"{missed_letters} typing errors")
    cpm_label.grid(row=3, column=0)
    wpm_label.grid(row=4, column=0)
    missed_label.grid(row=5, column=0)
    your_words.delete(1.0, 5.0)



type_test = 'This is the text you will be typing for your typing test. please take great care in \n' \
            'ensuring you are accurate, as the typing speed computation does not take into account \n' \
            'errors at this moment in time. I do not think I will have the time to design a new computation, \n' \
            'so please try to enjoy this typing test as is. I am considering taking some time to add two more \n' \
            'potential strings to test your typing skills. I plan to simply randomize which one of the three typing \n' \
            'modules will appear. So, how did you do? Did you finish it all? If so, you are truly a phenomenal typer. \n' \
            'If i could bake a dozen cookies and send them to you, I would!'

words_to_type = Canvas(root, width=996, height=300, bg='blue')

words_to_type.create_text(500, 150, text=type_test, font=18)
words_to_type.grid_configure(column=0, row=0, sticky=(N, W, E, S))


start_button = Button(text="Start", command=start).grid(column=0, row=2)

root.mainloop()
