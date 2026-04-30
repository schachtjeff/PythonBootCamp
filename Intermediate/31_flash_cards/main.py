#  Needs more enhancement

# Imports
import pandas as pd
import tkinter as tk
from tkinter import messagebox
from random import choice

# Constants
BACKGROUND_COLOR = "#B1DDC6"
LANG_LABEL_FONT = ("Arial", 40, "italic")
WORD_LABEL_FONT = ("Arial", 60, "bold")
SPANISH_TO_ENGLISH_CSV = "data/es-en-words.csv"
current_card = {}


# ---------------------------- Next CARD ------------------------------- #
def next_card() -> None:
    global current_card, flip_timer, words_to_learn
    window.after_cancel(flip_timer)
    words_to_learn = read_csv_to_df()
    current_card = choice(words_to_learn)
    canvas.itemconfig(card_language, text="Spanish", fill="black")
    canvas.itemconfig(card_word, text=current_card["Spanish"], fill="black")
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)

# ---------------------------- Flip CARD ------------------------------- #
def flip_card() -> None:
    canvas.itemconfig(card_language, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_image)

# ---------------------------- READ CSV ------------------------------- #
def read_csv_to_df():
    try:
        df_lang = pd.read_csv(SPANISH_TO_ENGLISH_CSV)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="File not found")
    else:
        df_in_dict = df_lang.to_dict(orient="records")
        return df_in_dict

# ---------------------------- Remove Word ------------------------------- #
# If the word is known, then we just remove the word from our data
def remove_word() -> None:
    words_to_learn.remove(current_card)
    pd.DataFrame(words_to_learn).to_csv("data/known_words.csv", index=False)
    next_card()


# ---------------------------- UI SETUP ------------------------------- #
# Setup window
window = tk.Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Change the language after 3 seconds
flip_timer = window.after(3000, func=flip_card)

# Create Canvas, card with texts
canvas = tk.Canvas(window, width=800, height=526)
card_front_image = tk.PhotoImage(file="images/card_front.png")
card_back_image = tk.PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_image)
card_language = canvas.create_text(400, 150, text="Language", font=LANG_LABEL_FONT)
card_word = canvas.create_text(400, 263, text="Word", font=WORD_LABEL_FONT)
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
card_button = tk.Button(image=card_front_image, highlightthickness=0)


# Buttons
cross_image = tk.PhotoImage(file="images/wrong.png")
cross_button = tk.Button(image=cross_image, highlightthickness=0, command=next_card)
cross_button.grid(row=1, column=0)

correct_image = tk.PhotoImage(file="images/right.png")
correct_button = tk.Button(image=correct_image, highlightthickness=0, command=next_card)
correct_button.grid(row=1, column=1)

# Generate the first card
next_card()

# Keep window open until close/exit
window.mainloop()

