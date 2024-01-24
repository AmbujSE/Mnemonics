from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
THEME_COLOR = "#375362"

window = Tk()
window.title("Mnemonics")
window.config(padx=20, pady=20, bg=GREEN)

title_label = Label(text="Timer", fg=YELLOW, bg=GREEN, highlightthickness=0, font=(FONT_NAME, 35, "bold"))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=500, bg="white")
text = canvas.create_text(100, 300, width=250, text="Words", font=("Arial", 10, "italic"), fill=THEME_COLOR)
canvas.grid(row=0, column=0, padx=50)

button1 = Button(text="Start", command=start_timer)
button1.grid(column=0, row=1)

window.mainloop()
