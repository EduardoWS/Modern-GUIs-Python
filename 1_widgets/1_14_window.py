import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# window
window = tk.Tk()
window.title('More on the window')
window.geometry('600x400+100+200')
#window.iconbitmap('python.ico')
# Define o caminho completo para o arquivo de ícone no formato PNG
icon_path = '1_widgets/python.png' # no linux use .png e não .ico

try:
    # Carrega a imagem do arquivo PNG
    icon_image = Image.open(icon_path)
    icon_photo = ImageTk.PhotoImage(icon_image)

    # Define o ícone da janela
    window.tk.call('wm', 'iconphoto', window._w, icon_photo)
except Exception as e:
    # Se houver um erro, imprime uma mensagem indicando o problema
    print(f'Erro ao definir o ícone da janela: {e}')

# exercise:
# start window in the middle of the screen 
window_width = 1400
window_height = 600
display_width = window.winfo_screenwidth()
display_height = window.winfo_screenheight()

left = int(display_width / 2 - window_width / 2)
top = int(display_height / 2 - window_height / 2)
window.geometry(f'{window_width}x{window_height}+{left}+{top}')

# window sizes 
window.minsize(200, 100)
# window.maxsize(800, 700)
# window.resizable(True,False)

# screen attributes 
print(window.winfo_screenwidth())
print(window.winfo_screenheight())

# window attributes
window.attributes('-alpha', 1)
# window.attributes('-topmost', True)

# security event 
window.bind('<Escape>', lambda event: window.quit())

# window.attributes('-disable', True)
# window.attributes('-fullscreen', True)


# title bar 
window.overrideredirect(True)
grip = ttk.Sizegrip(window)
grip.place(relx = 1.0, rely = 1.0, anchor = 'se')

# run
window.mainloop()