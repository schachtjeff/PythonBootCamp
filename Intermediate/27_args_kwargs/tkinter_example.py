import tkinter as tk

window = tk.Tk()
window.title("My window")
# change the size
window.minsize(width=500, height=300)

#Add label on the window with custom things
my_label = tk.Label(window, text="My label", font=("Arial", 25, "bold"))
my_label.pack()

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
button.pack()

#Entry component
input = tk.Entry(width=40)
input.pack()
print(input.get())



# Keep window on screen and always at the end
window.mainloop()