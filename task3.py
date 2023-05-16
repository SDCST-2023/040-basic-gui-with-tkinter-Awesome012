import tkinter as tk 
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("Example")

dogphoto = PhotoImage(file="dog.png")
label1 = tk.Label(window, image=dogphoto)

label2 = tk.Label(window,text="Pochacco!")

label3 = tk.Label(window,text="A cuddly little puppy! This is from the same\ncreators who brought you Keropi and Kero Kero", bg="#89CFF0")

label1.grid(row = 1, column = 3)
label2.grid(row = 1, column = 4)
label3.grid(row = 2, column = 1, columnspan = 6)

window.mainloop()