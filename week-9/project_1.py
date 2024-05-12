import tkinter as tk
from tkinter import messagebox
import random

employees = ("Mary Evans", "Eyo Ishan", "Durojaiye Dare", "Adams Ali", "Andrew Ugwu", "Stella Mankinde", "Jane Akibo",
             "Ago James", "Michell Taiwo", "Abraham Jones", "Nicole Anide", "Kosi Korso", "Adele Martins",
             "Emmanuel Ojo", "Ajayi Fatima")

tasks = ("Loading", "Transporting", "Reveiwing Orders", "Customer Service", "Delivering Items")


class Employee:

    def __init__(self, name):
        self.name = name

    def check_employee(self):
        if self.name in employees:
            pass

    def take_attendance(self):
        if self.name in employees:
            pass

    def assign_task(self):
        if self.name in employees:
            task = random.choice(tasks)
            window = tk.Toplevel(root)
            window.title("Employee Data")
            window.geometry("1000x1000")

            label_1 = tk.Label(window, text=f"Welcome {self.name}\n")
            label_1.pack()
            label_2 = tk.Label(window, text=f"This is your task for today {task}")
            label_2.pack()

    def refuse_access(self):
        if self.name in employees:
            pass
        else:
            messagebox.showerror("Access DENIED", "You are not a memeber of staff")


def enter():
    name = name_entry.get()
    rodger = Employee(name)

    if name in employees:
        rodger.assign_task()
    else:
        rodger.refuse_access()


root = tk.Tk()
root.title("Login form")
root.geometry("500x200")
name_label = tk.Label(root, text="Full Name")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

enter_button = tk.Button(root, text="Enter", command=enter)
enter_button.pack()
enter_button.config(fg="red")

root.mainloop()
