import tkinter as tk

window = tk.Tk()
window.title("My window")
# change the size
window.minsize(width=500, height=300)
# Adding padding using config and padx/y
window.config(padx=20, pady=20)

#Add label on the window with custom things
my_label = tk.Label(window, text="My label", font=("Arial", 25, "bold"))
# Cannot mix grid and pack
#my_label.pack()
# place is very precise
#my_label.place(x=100, y=100)
my_label.grid(column=0, row=0)

# Change the text in either of the following
my_label["text"] = "New Text"
my_label.config(text="New Text")

#funciton to do with button
def button_clicked() -> None:
    print("Button clicked")
    # Gets the input box and then puts text in label
    new_text = input.get()
    my_label.config(text=new_text)

#Button
button = tk.Button(text="Click me", command=button_clicked)
#button.pack()
button.grid(column=1, row=1)

# Newer_button
new_button = tk.Button(text="Don't click me", command=button_clicked)
new_button.grid(column=2, row=0)

#Entry component
input = tk.Entry(width=40)
#input.pack()
input.grid(column=3, row=2)
print(input.get())



# Keep window on screen and always at the end
window.mainloop()