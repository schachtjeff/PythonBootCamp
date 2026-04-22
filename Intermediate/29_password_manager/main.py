#Imports
import tkinter as tk
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# From Day 5
#Password Generator Project
def generate_password() -> str:
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for letter in range(nr_letters)]
    password_numbers = [choice(numbers) for number in range(nr_numbers)]
    password_symbol = [choice(symbols) for symbol in range(nr_symbols)]

    password_list = password_letters + password_numbers + password_symbol
    shuffle(password_list)

    # Old code
    #for char in range(nr_letters):
    #  password_list.append(random.choice(letters))
    #for char in range(nr_symbols):
    #  password_list += random.choice(symbols)
    #for char in range(nr_numbers):
    #  password_list += random.choice(numbers)

    password = "".join(password_list)
    password_entry.insert(0, password)
    #pyperclip -> copy to the clipboard
    pyperclip.copy(password)
    #pyperclip.paste()

    #for char in password_list:
    #  password += char
    #print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
# Save into data.txt -> 'website | email | password'
# Delete entries after adding
def add_data_to_file() -> None:
    website_data = website_entry.get()
    password_data = password_entry.get()
    email_data = email_entry.get()

    # check if website or password is empty
    if len(website_data) or len(password_data) or len(email_data):
        messagebox.showerror(title="Oops", message="Please fill all fields")
    else:
        # Add message box
        is_ok = messagebox.askokcancel(title=website_data, message=f"These are the details entered:\n"
                                                           f"Email: {email_data}\n"
                                                           f"Password: {password_data}\n"
                                                           f"Ok to save?")

        if is_ok:
            data = f"{website_data} | {email_data} | {password_data}\n"
            file = open("data.txt", "a")
            file.write(data)
            file.close()

            # Delete entries from beginning to tkinter's end
            website_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
            # Reset the email entry to original, is there one?
            #email_entry.delete(0, "hello@email.com")


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
website_entry.focus()

email_entry = tk.Entry(window, width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "hello@email.com")

password_entry = tk.Entry(window, width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = tk.Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_content_button = tk.Button(text="Add", width=36, command=add_data_to_file)
add_content_button.grid(row=4, column=1, columnspan=2)

# Keep window open until close/exit
window.mainloop()