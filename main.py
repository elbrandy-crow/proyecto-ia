import tkinter as tk
from customtkinter import CTkButton, CTkLabel, CTk,CTkFrame
import os
from tkinter import PhotoImage

def open_trap_window():
    os.system("python form_trap.py")

def open_rock_window():
    os.system("python form_rock.py")

def open_bachata_window():
    os.system("python form_bachata.py")

root = CTk() 
root.geometry("500x600+350+20")
root.minsize(480,500)
root.config(bg ='#010101')
root.title("Iniciar Sesion")

frame = CTkFrame(root, fg_color='#010101')
frame.grid(column=0, row = 0, sticky='nsew',padx=50, pady =50)

frame.columnconfigure([0,1], weight=1)
frame.rowconfigure([0,1,2,3,4,5], weight=1)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

logo = PhotoImage(file='images/logo.png') 

# Etiqueta de título con un tamaño de fuente más grande
CTkLabel(frame, image = logo).grid(columnspan=2, row=0)

title_label = CTkLabel(frame, text="WHAT IS THE BPM", fg_color='#21F100', font=("Helvetica", 30))
title_label.grid(columnspan=2, row=1)

# Definir botones para cada género
trap_button =CTkButton(frame,  border_color='#21F100', fg_color='#010101',
	hover_color='#16161a',corner_radius=12,border_width=2,
    text='TRAP', command=open_trap_window)
trap_button.grid(column=0, row=2,padx=4, pady =30, columnspan=2)

rock_button = CTkButton(frame,  border_color='#21F100', fg_color='#010101',
	hover_color='#16161a',corner_radius=12,border_width=2,
    text='ROCK', command=open_rock_window)
rock_button.grid(column=0, row=3,padx=4, pady =30, columnspan=2)

bachata_button = CTkButton(frame,  border_color='#21F100', fg_color='#010101',
	hover_color='#16161a',corner_radius=12,border_width=2,
    text='BACHATA', command=open_bachata_window)
bachata_button.grid(column=0, row=4,padx=4, pady =30, columnspan=2)

root.mainloop()