import tkinter as tk
from tkinter import messagebox


def enter():

    name = name_entry.get()
    weight = int(weight_entry.get())
    location = location_entry.get()

    rodger = Customer(name, weight, location)
    rodger.charge()


class Customer:

    def __init__(self, name, weight, location):
        self.name = name
        self.weight = weight
        self.location = location

    def charge(self):
        if self.weight >= 10 and (self.location == "PAU"):
            window = tk.Toplevel(root)
            window.title("Receipt")
            window.geometry("400x200")

            label_1 = tk.Label(window, text=f"Dear Customer")
            label_1.pack()
            label_2 = tk.Label(window, text="The Price of your Delivery is N2,000")
            label_2.pack()
        elif self.weight < 10 and (self.location == "PAU"):
            window = tk.Toplevel(root)
            window.title("Receipt")
            window.geometry("400x200")

            label_1 = tk.Label(window, text="Dear Customer")
            label_1.pack()
            label_2 = tk.Label(window, text="The Price of your Delivery is N1,500")
            label_2.pack()
        elif self.weight >= 10 and (self.location == "Epe"):
            window = tk.Toplevel(root)
            window.title("Receipt")
            window.geometry("400x200")

            label_1 = tk.Label(window, text="Dear Customer")
            label_1.pack()
            label_2 = tk.Label(window, text="The Price of your Delivery is N5,00")
            label_2.pack()
        elif self.weight < 10 and (self.location == "Epe"):
            window = tk.Toplevel(root)
            window.title("Receipt")
            window.geometry("400x200")

            label_1 = tk.Label(window, text="Dear Customer")
            label_1.pack()
            label_2 = tk.Label(window, text="The Price of your Delivery is N4,00")
            label_2.pack()
        else:
            messagebox.showerror("Location", "We do not deliver to your location/drop of point")


root = tk.Tk()
root.title("Login form")
root.geometry("500x200")

name_label = tk.Label(root, text="Full Name")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

weight_label = tk.Label(root, text="Weight of Package")
weight_label.pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

location_label = tk.Label(root, text="Drop of Location")
location_label.pack()
location_entry = tk.Entry(root)
location_entry.pack()

enter_button = tk.Button(root, text="Enter", command=enter)
enter_button.pack()
enter_button.config(fg="red")

root.mainloop()
