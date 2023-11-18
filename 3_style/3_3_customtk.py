import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

# window 
window = ctk.CTk()
window.title('customtkinter app')
window.geometry('600x400')

# widgets 
string_var = ctk.StringVar(value = 'a custom string')
label = ctk.CTkLabel(
	window, 
	text = 'A ctk label', 
	fg_color = ('blue','red'), 
	text_color = ('black','white'),
	corner_radius = 10,
	textvariable = string_var)
label.pack()

button = ctk.CTkButton(
	window, 
	text = 'A ctk button', 
	fg_color = '#FF0', 
	text_color = '#000',
	hover_color = '#AA0',
	command = lambda: ctk.set_appearance_mode('light'))
button.pack()

frame = ctk.CTkFrame(window)
frame.pack()

slider = ctk.CTkSlider(frame)
slider.pack(padx = 20, pady = 20)

# exercise 
switch = ctk.CTkSwitch(
	window, 
	text = '',
	button_length=1,
	switch_width = 50,
	switch_height = 25,
 	height=100,
	
	corner_radius = 100
 							)
switch.pack()

# run
window.mainloop()