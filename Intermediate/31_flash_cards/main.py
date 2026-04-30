# Imports
import tkinter as tk

# Constants
BACKGROUND_COLOR = "#B1DDC6"
LANG_LABEL_FONT = ("Arial", 40, "italic")
WORD_LABEL_FONT = ("Arial", 60, "bold")


# ---------------------------- FLIP CARD ------------------------------- #
def flip_card() -> None:
    pass

# ---------------------------- Wrong Answer ---------------------------- #
def wrong_ans() -> None:
    pass

# ---------------------------- Correct Answer -------------------------- #
def correct_ans() -> None:
    pass

# ---------------------------- UI SETUP ------------------------------- #
# Setup window
window = tk.Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Create Canvas, card with texts
canvas = tk.Canvas(window, width=800, height=526)
card_front_image = tk.PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_image)
canvas.create_text(400, 150, text="Language", font=LANG_LABEL_FONT)
canvas.create_text(400, 263, text="Word", font=WORD_LABEL_FONT)
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
card_button = tk.Button(image=card_front_image, highlightthickness=0, command=flip_card)


# Buttons
cross_image = tk.PhotoImage(file="images/wrong.png")
cross_button = tk.Button(image=cross_image, highlightthickness=0, command=wrong_ans)
cross_button.grid(row=1, column=0)

correct_image = tk.PhotoImage(file="images/right.png")
correct_button = tk.Button(image=correct_image, highlightthickness=0, command=correct_ans)
correct_button.grid(row=1, column=1)

# Keep window open until close/exit
window.mainloop()

