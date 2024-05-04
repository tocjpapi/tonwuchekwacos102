
# Algorithm for PAU Cafe System


#  Start

# ⦁	First of all I import Tkinter GUI and other neccesary modules needed to execute the program.

# ⦁	Setup the main GUI window. i.e background color,size and title.

# ⦁	I create a function that calculates charges based on what the user chose to buy from the catalogue.

# ⦁	If the total order is less than N2,500 the customer gets a 10% discount.

# ⦁	If the total order is greater than N2,500 and less than N5,000 the customer gets a 15% discount.

# ⦁	If the order is greater than N5,000 the customer gets a 25% discount.

# ⦁	Else if the order is less than N1,000 the customer gets no discount.

# ⦁	I design a User freindly GUI using Tkinter (as I should've imported by then).

# ⦁	I add a dropdown menu using ttk(tkinter themed widgets) and I make it read only so users can't  type on it causing bad UX and avoidable errors.

# ⦁	I create a function that takes values from the dropdown to the order dictionary.

# ⦁	I create a submit button function that has the order dictionary.

# ⦁	Ask the user for their name.

# ⦁	When they provide their name, run the  important part of the code.

# ⦁	All calculations begin after user clicks submit as to not overwhelm the user.

# ⦁	The price the user gets to play will be displayed in a new window as stated in the assignment.

# End




# Design Choices and reason.
# ⦁	For the colours. From my knowledge in UI design. I believe that choosing colors that are too much in contrast will be a bad idea because it unconciously strains the user's eyes. So I chose colors that give a sense of warmth.
 


# ⦁	For the font I chose a sans-serif font for a friendlier look.
 

# ⦁	I implemented a drop down menu because if this was an actual solution, it will probably work on a touchscreen and we shouldnt stress the user by triggering an onscreen keyboard.
 



import tkinter as tk
from tkinter import ttk, simpledialog, messagebox

#for image import
import os
import webbrowser



def calculate_charges(order_dict):
    total_price = sum(order_dict.values())
    discount = 0
    if total_price < 1000:
        discount = 0
    elif total_price < 2500:
        discount = 0.1
    elif total_price < 5000:
        discount = 0.15
    else:
        discount = 0.25
    discounted_price = total_price - (total_price * discount)
    return discounted_price


def submit():
    order_dict = {}
    update_order_dict(order_dict, combo1, quantity1)
    update_order_dict(order_dict, combo2, quantity2)
    update_order_dict(order_dict, combo3, quantity3)
    update_order_dict(order_dict, combo4, quantity4)
    update_order_dict(order_dict, combo5, quantity5)



    if order_dict:
        total_charges = calculate_charges(order_dict)
        name = simpledialog.askstring("Name", "Please enter your name:")
        if name:
            order_summary = f"{name}, you get to pay N{total_charges:.2f}\n\n"
            order_summary += "Your Order Details:\n"
            for item, price in order_dict.items():
                order_summary += f"{item}: N{price:.2f}\n"
            order_summary += f"\nTotal Charges: N{total_charges:.2f}"
            
            # Order Details
            order_window = tk.Toplevel(root)
            order_window.title("Order Summary")
            order_window.geometry("400x300")
            order_window.configure(bg="#1a1a1a")


            #absolute positioning of the window
            order_window.attributes("-topmost", True)  
            

            order_label = tk.Label(order_window, text=order_summary, font=("Segoe UI", 12), bg="#1a1a1a", fg="#fff")
            #Used pack to justify content to center
            order_label.pack(padx=20, pady=20)
            

            #clear All cells
            quantity1.delete(0, tk.END)
            quantity2.delete(0, tk.END)
            quantity3.delete(0, tk.END)
            quantity4.delete(0, tk.END)
            quantity5.delete(0, tk.END)
            combo1.set('')
            combo2.set('')
            combo3.set('')
            combo4.set('')
            combo5.set('')
    else:
        messagebox.showwarning("Warning", "Please select at least one item.")


def menu():
    image_path = os.path.join(os.path.dirname(__file__), "nuxt.png")
    if os.path.exists(image_path):
        print("Image Path:", image_path)
        try:
            webbrowser.open(image_path)
        except Exception as e:
            print("Choose a better image CJ")
    else:
        print("Cant see the image here")


def update_order_dict(order_dict, combo_box, quantity_box):
    if combo_box.get():
        item = combo_box.get().split(' [')[0]
        price = prices[combo_box.get()] * int(quantity_box.get())
        if item in order_dict:
            order_dict[item] += price
        else:
            order_dict[item] = price

root = tk.Tk()
root.title("PAU Café")
root.geometry("900x400")  
root.configure(bg="#1a1a1a")  

prices = {
    "Jollof Rice [N350]": 350,
    "Coconut Fried Rice [N350]": 350,
    "Jollof Spaghetti [N350]": 350,
    "Sweet Chilli Chicken [N1100]": 1100,
    "Grilled Chicken Wings [N400]": 400,
    "Fried Beef [N400]": 400,
    "Fried Fish [N500]": 500,
    "Boiled Egg [N200]": 200,
    "Sausages [N200]": 200,
    "Savoury Beans [N350]": 350,
    "Roasted Sweet Potatoes [N300]": 300,
    "Fried Plantains [N150]": 150,
    "Mixed Vegetable Salad [N150]": 150,
    "Boiled Yam [N150]": 150,
    "Water [N200]": 200,
    "Glass Drink (35cl) [N150]": 150,
    "PET Drink (35cl) [N300]": 300,
    "PET Drink (50cl) [N350]": 350,
    "Glass/Canned Malt [N500]": 500,
    "Fresh Yo [N600]": 600,
    "Pineapple Juice [N350]": 350,
    "Mango Juice [N350]": 350,
    "Zobo Drink [N350]": 350,
    "Eba [N100]": 100,
    "Poundo Yam [N100]": 100,
    "Semo [N100]": 100,
    "Atama Soup [N450]": 450,
    "Egusi Soup [N480]": 480
}

label = tk.Label(root, text="Catalogue", font=("Segoe UI", 32, "normal"), bg="#1a1a1a", fg="#999")
label.grid(row=0, column=0, columnspan=6, padx=10, pady=(40,40), sticky="w")  

label1 = tk.Label(root, text="Rice / Pasta", font=("Segoe UI", 11, "normal"), bg="#1a1a1a", fg="#999")
label1.grid(row=1, column=0, padx=(20,10), pady=(10,15), sticky="w")

options1 = ["Jollof Rice [N350]", "Coconut Fried Rice [N350]", "Jollof Spaghetti [N350]"] 
combo1 = ttk.Combobox(root, values=options1, state="readonly")
combo1.grid(row=2, column=0, padx=(20,10), pady=(0,10), sticky="w")

quantity1 = tk.Entry(root, width=5)
quantity1.insert(tk.END, '1')
quantity1.grid(row=2, column=1, padx=(0, 10), pady=(0,10), sticky="w")

label2 = tk.Label(root, text="Protein", font=("Segoe UI", 11, "normal"), bg="#1a1a1a", fg="#999")
label2.grid(row=1, column=2, padx=(10,20), pady=(10,15), sticky="w")

options2 = ["Sweet Chilli Chicken [N1100]", "Grilled Chicken Wings [N400]", "Fried Beef [N400]", "Fried Fish [N500]", "Boiled Egg [N200]", "Sausages [N200]"] 
combo2 = ttk.Combobox(root, values=options2, state="readonly")
combo2.grid(row=2, column=2, padx=(10,20), pady=(0,10), sticky="w")

quantity2 = tk.Entry(root, width=5)
quantity2.insert(tk.END, '1')
quantity2.grid(row=2, column=3, padx=(0, 10), pady=(0,10), sticky="w")

label3 = tk.Label(root, text="Side Dishes", font=("Segoe UI", 11, "normal"), bg="#1a1a1a", fg="#999")
label3.grid(row=1, column=4, padx=(10,20), pady=(10,15), sticky="w")

options3 = ["Savoury Beans [N350]", "Roasted Sweet Potatoes [N300]", "Fried Plantains [N150]", "Mixed Vegetable Salad [N150]", "Boiled Yam [N150]"] 
combo3 = ttk.Combobox(root, values=options3, state="readonly")
combo3.grid(row=2, column=4, padx=(10,20), pady=(0,10), sticky="w")

quantity3 = tk.Entry(root, width=5)
quantity3.insert(tk.END, '1')
quantity3.grid(row=2, column=5, padx=(0, 10), pady=(0,10), sticky="w")

label4 = tk.Label(root, text="Beverages", font=("Segoe UI", 11, "normal"), bg="#1a1a1a", fg="#999")
label4.grid(row=3, column=0, padx=(20,10), pady=(10,15), sticky="w")

options4 = ["Water [N200]", "Glass Drink (35cl) [N150]", "PET Drink (35cl) [N300]", "PET Drink (50cl) [N350]", "Glass/Canned Malt [N500]", "Fresh Yo [N600]", "Pineapple Juice [N350]", "Mango Juice [N350]", "Zobo Drink [N350]"] 
combo4 = ttk.Combobox(root, values=options4, state="readonly")
combo4.grid(row=4, column=0, padx=(20,10), pady=(0,10), sticky="w")

quantity4 = tk.Entry(root, width=5)
quantity4.insert(tk.END, '1')
quantity4.grid(row=4, column=1, padx=(0, 10), pady=(0,10), sticky="w")

label5 = tk.Label(root, text="Soups & Swallows", font=("Segoe UI", 11, "normal"), bg="#1a1a1a", fg="#999")
label5.grid(row=3, column=2, padx=(10,20), pady=(10,15), sticky="w")

options5 = ["Eba [N100]", "Poundo Yam [N100]", "Semo [N100]", "Atama Soup [N450]", "Egusi Soup [N480]"] 
combo5 = ttk.Combobox(root, values=options5, state="readonly")
combo5.grid(row=4, column=2, padx=(10,20), pady=(0,10), sticky="w")

quantity5 = tk.Entry(root, width=5)
quantity5.insert(tk.END, '1')
quantity5.grid(row=4, column=3, padx=(0, 10), pady=(0,10), sticky="w")

submit_button = tk.Button(root, text="Show Menu image", command=menu)
submit_button.place(x=20, y=350)

submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.place(x=800, y=350)

copyright_label = tk.Label(root, text="© Copyright PAU All Rights Reserved", font=("Segoe UI", 9, "normal"), bg="#1a1a1a", fg="#999")
copyright_label.place(x=340, y=355)

root.mainloop()





