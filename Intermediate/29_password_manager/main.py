#Imports
import tkinter as tk


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
# Setup window
window = tk.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Create the canvas with size and thick outline?
canvas = tk.Canvas(window, width=200, height=200)
lock_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=0)

# Keep window open until close/exit
window.mainloop()