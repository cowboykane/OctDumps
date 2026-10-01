# girl is this thing on

import tkinter as tk
import random

# When you come back to this tomorrow:

"""
1. Add a button to increase the counter
2. Add a button to decrease the counter
3. Make btn1 generate a random number 
4. create an option to completely clear the counter.
5. Get rid of these 
"""

root = tk.Tk()
root.geometry("500x500")
root.config(bg="blue")


def increase_counter():
    counter.set(counter.get() + 1)

def decrease_counter():
    counter.set(counter.get() - 1)

def random_counter():
    rand_num = random.randint(0, 100)
    counter.set(rand_num)

def clear_counter():
    counter.set(0)

# Title
title = tk.Label(root, text="Button game Teehee",
            font=("Consolas", 15))

# Buttons 
increase_btn = tk.Button(root, text="+",
                         activeforeground="red",
                         bd=2,
                         font=("Consolas", 15),
                         command=increase_counter)

decrease_btn = tk.Button(root, text="-",
                         activeforeground="green",
                         bd=2,
                         font=("Consolas", 15),
                         command=decrease_counter)

rand_button = tk.Button(root, text="Random",
                 font=("Consolas", 15),
                activeforeground="blue",
                bd=2,
                command=random_counter)

clear = tk.Button(root, text="Clear",
                  activeforeground="purple",
                  bd=2,
                  font=("Consolas", 10),
                  command=clear_counter)

# Counter Label
counter = tk.IntVar(value=0)

counter_label = tk.Label(root, textvariable=counter,
                        font=("Consolas", 30))



# Geometry Manager

title.place(x=50, y=10)
increase_btn.place(x=80, y=80)
rand_button.place(x=175, y=80)
decrease_btn.place(x=375, y=80)
counter_label.place(x=230, y=200)
clear.place(x=200, y=300)

root.mainloop()