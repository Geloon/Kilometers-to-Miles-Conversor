from tkinter import *


def km_to_miles():
    km = float(km_input.get())
    miles = 0.6213711 * km
    kilometer_result_label.config(text=f"{miles}")


# Main window

window = Tk()
window.title("Kilometers to Miles converter by Geloon")
window.config(padx=120, pady=50)

# Input

km_input = Entry(width=7)
km_input.grid(column=1, row=0)

# Labels

kilometers_label = Label(text="Km")
kilometers_label.grid(column=2, row=0)
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)
kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=1)

# Button

calculate_button = Button(text="Calculate", command=km_to_miles)
calculate_button.grid(column=1, row=2)

window.mainloop()