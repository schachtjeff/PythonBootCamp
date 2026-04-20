#Imports
import tkinter as tk

# Setup window
window = tk.Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Calculate function
def miles_to_km_applied_label() -> None:
    new_km_value = float(user_input.get()) * 1.60934
    km_conversion_label.config(text=new_km_value)

# Add labels
is_equal_to_label = tk.Label(window, text="is equal to")
is_equal_to_label.grid(row=1, column=0)
miles_label = tk.Label(window, text="Miles")
miles_label.grid(row=0, column=2)
km_label = tk.Label(window, text="Km")
km_label.grid(row=1, column=2)
km_conversion_label = tk.Label(window, text="0")
km_conversion_label.grid(row=1, column=1)

# Add entry box
user_input = tk.Entry(window, width=10)
user_input.grid(row=0, column=1)

# Add button box
calc_button = tk.Button(text="Calculate", command=miles_to_km_applied_label)
calc_button.grid(row=2, column=1)


# Keep window on screen and always at the end
window.mainloop()