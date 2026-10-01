# Prompt Generator...Because its october dude 

"""
1. Functionality:
    - User selects from a screen of options. 
        1. OTP Prompt Generator 
        2. General Prompt Generator

    - User selects OTP Prompt Generator:
        1. User types in 2 names.
        2. User hits "Generate" Button
        3. In a frame for the output, a prompt
        based on given names is generated.

    - User selects General Prompt Generator:
        1. One button, one output frame
        2. User hits "Generate" button. Boom, prompt!

2. Features/Needs/Research:
    - Research a better ui library. Tkinter is busted
    - How to code multiple windows/new window on command
    - Find something like paint.net for easier ui
    references
"""

import customtkinter as ctk
ctk.deactivate_automatic_dpi_awareness()

root = ctk.CTk()
root.geometry("500x500")





root.mainloop()