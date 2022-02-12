import tkinter as tk
from tkinter import *

window = Tk()
window.title = "Chi Squared Simulator"
canvas1 = tk.Canvas(window, width = 400, height = 300)
canvas1.pack()

entry1 = tk.Entry (window)
entry2 = tk.Entry (window)  
entry3 = tk.Entry (window) 
entry4 = tk.Entry (window)
entry5 = tk.Entry (window)  
entry6 = tk.Entry (window) 
entry7 = tk.Entry (window)
entry8 = tk.Entry (window)  
entry9 = tk.Entry (window) 
entry10 = tk.Entry (window)
entry11 = tk.Entry (window)  
entry12 = tk.Entry (window) 
canvas1.create_window(20, 20, window=entry1, width=20, height=20)
canvas1.create_window(50, 20, window=entry2, width=20, height=20)
canvas1.create_window(80, 20, window=entry3, width=20, height=20)
canvas1.create_window(110, 20, window=entry4, width=20, height=20)
canvas1.create_window(140, 20, window=entry5, width=20, height=20)
canvas1.create_window(170, 20, window=entry6, width=20, height=20)
canvas1.create_window(20, 50, window=entry7, width=20, height=20)
canvas1.create_window(50, 50, window=entry8, width=20, height=20)
canvas1.create_window(80, 50, window=entry9, width=20, height=20)
canvas1.create_window(110, 50, window=entry10, width=20, height=20)
canvas1.create_window(140, 50, window=entry11, width=20, height=20)
canvas1.create_window(170, 50, window=entry12, width=20, height=20)






window.mainloop()