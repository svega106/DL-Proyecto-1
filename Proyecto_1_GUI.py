import tkinter as tk
from tkinter import filedialog, Text
import os
from tkinter import *
from tkinter import ttk

root = tk.Tk()

canvas = tk.Canvas(root, height= 900, width= 1600, bg= "#263d42")
canvas.pack()

frame = tk.Frame(root,background= "#3e646c")
frame.place(relwidth = 0.8, relheight = 0.8, relx= 0.1, rely= 0.1)

root.mainloop()
  

