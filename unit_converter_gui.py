import tkinter as tk

# Create main window
window = tk.Tk()
window.title("Unit Converter")
window.geometry("400x300")
window.resizable(False, False)
window.configure(bg="#f0f0f0")

# Create label for instruction
label = tk.Label(window, text="Enter value to convert:")
label.pack(pady=10)

# Create entry box for user input
entry = tk.Entry(window)
entry.pack(pady=10)

# Conversion options
options = ["Centimeters to Inches", "Kilograms to Pounds", "Celsius to Fahrenheit"]

# Create dropdown (OptionMenu)
selected_option = tk.StringVar()
selected_option.set(options[0])  # default value
dropdown = tk.OptionMenu(window, selected_option, *options)
dropdown.pack(pady=10)

# Create result label
result_label = tk.Label(window, text="")
result_label.pack(pady=10)

# Function to do conversion
def convert():
    try:
        value = float(entry.get())
        option = selected_option.get()

        if option == "Centimeters to Inches":
            result = value / 2.54
        elif option == "Kilograms to Pounds":
            result = value * 2.20462
        elif option == "Celsius to Fahrenheit":
            result = (value * 9/5) + 32

        result_label.config(text=f"Result: {result:.2f}")
    except ValueError:
        result_label.config(text="Please enter a valid number.")

# Convert button
convert_button = tk.Button(window, text="Convert", command=convert)
convert_button.pack(pady=10)

# Run the main loop
window.mainloop()