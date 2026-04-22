#Imports
import tkinter as tk


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
# Setup window
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Create the canvas with size and thick outline?
canvas = tk.Canvas(window, width=200, height=200)
lock_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

# Labels
website_label = tk.Label(window, text="Website:")
website_label.grid(row=1, column=0)

email_user_label = tk.Label(window, text="Email/Username:")
email_user_label.grid(row=2, column=0)

password_label = tk.Label(window, text="Password:")
password_label.grid(row=3, column=0)

# Entry boxes
website_entry = tk.Entry(window, width=35)
website_entry.grid(row=1, column=1, columnspan=2)

email_entry = tk.Entry(window, width=35)
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = tk.Entry(window, width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = tk.Button(text="Generate Password")
generate_password_button.grid(row=3, column=2)

add_content_button = tk.Button(text="Add", width=36)
add_content_button.grid(row=4, column=1, columnspan=2)

# Keep window open until close/exit
window.mainloop()