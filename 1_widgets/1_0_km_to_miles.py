import tkinter as tk        # lógica de interface
#from tkinter import ttk    # widgets de interface
import ttkbootstrap as ttk  # tema de interface (deixa bonito)

# functions
def convert():
    try:
        km_input = float(entry_int.get())
        miles_output = km_input / 1.609
        output_string.set(f"Miles: {miles_output:.2f}")
    except ValueError:
        pass
    

# window
#window = tk.Tk()
window = ttk.Window(themename='darkly')
window.title("Demo")
window.geometry("300x200") # width x height

# title
title_label = ttk.Label(master=window, text="\nKm to Miles", font = 'Helvetica 24 bold')
title_label.pack()

# input field
input_frame = ttk.Frame(master=window)
entry_int = tk.IntVar()  # variável que armazena o valor do entry, como um int (não é necessário, mas é uma boa prática)
entry = ttk.Entry(master=input_frame, textvariable=entry_int) # textvariable é a variável que armazena o valor do entry
button = ttk.Button(master=input_frame, text="Convert", command=convert) # não usar () no command, senão a função é executada na hora
entry.pack(side="left", padx=10)
button.pack(side="left")
input_frame.pack(pady=20)

# output field
output_string = tk.StringVar()
output_label = ttk.Label(master=window, text="Miles: ", font = 'Helvetica 18', textvariable=output_string)
output_label.pack(pady=10)

# run
window.mainloop()
