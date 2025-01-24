from tkinter import  Frame, Button
import customtkinter
from functools import partial

root = customtkinter.CTk()
root.geometry("1200x600")
# Create Numpad
# Callback for Numpad
def btn_click(i):
    print(f"clicked {i}")


# Layout for Numpad
btns_frame = Frame(root)
btns_frame.pack()
a_Board = [[col + row * 8 for col in range(8)] for row in range(8)]
for row in range(len(a_Board)):
    for col in range(len(a_Board[row])):
        i = a_Board[row][col]
        # Doesn't work, i is always 8 in btn_click()
        # b = Button(btns_frame, text=str(i), command=lambda: btn_click(i))
        b = customtkinter.CTkButton(btns_frame, text=str(i), command=partial(btn_click, i), height=50, width=50)
        b.grid(row=row +1, column=col)

root.mainloop()