from tkinter import *
from tkinter import messagebox
from word_machine import WordMachine
import math

word_machine = WordMachine()
# timer = None


def count_down(count=60):
    # global timer
    start_button.config(state="disabled")
    typed_word.config(state="normal")
    typed_word.focus()
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    timer_text.config(text=f"Time: {minutes}:{seconds}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        update_ui()
        start_button.config(state="normal")
        typed_word.config(state="disabled")
        calculate_end_score()


def calculate_end_score():
    word_machine.calculate_score()
    messagebox.showerror(title="Time's up!",
                         message=f"You typed {word_machine.score} words!\n\nOf the words you typed, you were "
                                 f"{word_machine.current_accuracy()}% accurate.")


def check_word(event):
    if len(typed_word.get()) > 0:
        word = typed_word.get()
        word_machine.check_word(word)
        word_machine.serve_another_word()
        update_ui()


def update_ui():
    typed_word.delete(0, "end")
    if word_machine.current_word > 0:
        previous_word.config(text=word_machine.words[word_machine.current_word - 1])
    else:
        previous_word.config(text="")
    current_word.config(text=word_machine.words[word_machine.current_word])
    next_word.config(text=word_machine.words[word_machine.current_word + 1])
    score_text.config(text=f"Score: {word_machine.score}")


def start_pressed():
    if word_machine.current_word > 0:
        word_machine.restart()
        update_ui()
        count_down()
    else:
        count_down()


# ------- SET UP UI ------- #
window = Tk()
window.title("Wordypants")
window.config(padx=20, pady=20)
window.minsize(width=200, height=300)

timer_text = Label(text="Time: 0:00")
timer_text.grid(row=0, column=0)

score_text = Label(text=f"Score: {word_machine.score}")
score_text.grid(row=0, column=2)

previous_word = Label(text="", width=8)
previous_word.config(font=("Arial", 20))
previous_word.grid(row=1, column=0)

current_word = Label(text=word_machine.words[word_machine.current_word], width=8)
current_word.config(font=("Arial", 26, "bold"))
current_word.grid(row=1, column=1, pady=10)

next_word = Label(text=word_machine.words[word_machine.current_word + 1], width=8)
next_word.config(font=("Arial", 20))
next_word.grid(row=1, column=2)

typed_word = Entry(width=10, state="disabled")
typed_word.grid(row=2, column=1, pady=20)

start_button = Button(text="Start!", command=start_pressed)
start_button.config(padx=20)
start_button.grid(row=3, column=1)

window.bind("<space>", check_word)
window.bind("<Return>", check_word)

window.mainloop()
