import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


# window
window = tk.Tk()

centro_x = window.winfo_screenwidth()/2 - 600/2     # Largura da tela / 2 - Largura da janela / 2
centro_y = window.winfo_screenheight()/2 - 400/2    # Altura da tela / 2 - Altura da janela / 2

window.geometry(f'600x400+{int(centro_x)}+{int(centro_y)}')  # Largura x Altura + Esquerda + Topo
window.title('teste')
# Define o caminho completo para o arquivo de ícone no formato PNG
icon_path = '1_widgets/python.png'

try:
    # Carrega a imagem do arquivo PNG
    icon_image = Image.open(icon_path)
    icon_photo = ImageTk.PhotoImage(icon_image)

    # Define o ícone da janela
    window.tk.call('wm', 'iconphoto', window._w, icon_photo)
except Exception as e:
    # Se houver um erro, imprime uma mensagem indicando o problema
    print(f'Erro ao definir o ícone da janela: {e}')

# window sizes
window.minsize(200, 100)
# window.maxsize(800, 500)        # (não é muito comum usar)
# window.resizable(True,False)    # x, y (não é muito comum usar)

# screen attributes
print(window.winfo_screenwidth())   # largura da tela
print(window.winfo_screenheight())  # altura da tela

# window attributes
# window.attributes('-topmost', True)  # Coloca a janela no topo
# window.attributes('-alpha', 0.1)      # transparência (0.0 - 1.0) (não funciona no linux)

# security event
window.bind('<Escape>', lambda event: window.quit())

#window.attributes('-fullscreen', True)  # Coloca a janela em tela cheia

# title bar
# window.overrideredirect(True)  # Remove a barra de título da janela (buga no linux)
grip = ttk.Sizegrip(window)
grip.place(relx=1.0, rely=1.0, anchor='se') # Cria um widget para redimensionar a janela

# run
window.mainloop()