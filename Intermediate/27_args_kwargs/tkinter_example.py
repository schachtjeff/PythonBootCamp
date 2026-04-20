import tkinter as tk

window = tk.Tk()
window.title("My window")
# change the size
window.minsize(width=500, height=300)

#Add label on the window with custom things
my_label = tk.Label(window, text="My label", font=("Arial", 25, "bold"))
my_label.pack()


# Keep window on screen and always at the end
window.mainloop()