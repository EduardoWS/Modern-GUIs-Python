import customtkinter as ctk
from settings import *
from PIL import Image, ImageTk
import tkinter as tk
import ttkbootstrap as ttk
from datetime import date

class App(ttk.Window):
    def __init__(self):
        super().__init__(themename = 'e-library')
        self.title('')
        # iniciar tela no centro
        width = self.winfo_screenwidth() 
        height = self.winfo_screenheight()
        x = int(width/2 - int(APP_SIZE[0])/2)
        y = int(height/2 - int(APP_SIZE[1])/2)
        self.geometry(f'{APP_SIZE[0]}x{APP_SIZE[1]}+{x}+{y}')
        
        #self.iconbitmap('empty.ico')
        self.resizable(False, False)
        
        # layout
        # self.columnconfigure(0, weight=1, uniform='a')
        # self.rowconfigure((0,1,2,3,4,5,6,7,8,9), weight=1, uniform='a')
        

        
        # widgets
        Widgets(self)
        
        self.mainloop()

class Widgets():
    def __init__(self, parent):
        
        # layout
        parent.columnconfigure(0, weight=1, uniform='a')
        parent.columnconfigure(1, weight=3, uniform='a')
        parent.rowconfigure((0,1,2,3,4,5,6), weight=1, uniform='a')
        
        # fonts
        font = ctk.CTkFont(family=FONT, size=MAIN_TEXT_SIZE, weight='bold')
        
        # frames
        main_frame = ctk.CTkFrame(parent, fg_color=LIGHT_BLUE, corner_radius=20)
        main_frame.grid(column=1, row=0, rowspan=2, sticky='new', padx=80, pady=40)
        
        
        text_logo = ctk.CTkLabel(master=main_frame, text='e-Library', text_color=BLACK, font=font,
                                 corner_radius=20)
        text_logo.pack(expand=True, fill='both', padx=30, pady=30)
        
        meter_frame = ctk.CTkFrame(master=parent, fg_color='transparent', corner_radius=20)
        meter_frame.grid(column=1, row=2, rowspan=5, sticky='nsew', padx=10, pady=10)
        
        meter = ttk.Meter(meter_frame,
                    amounttotal = 100,
                    amountused = 10,
                    stepsize=5,
                    interactive = True,
                    metertype = 'full',
                    subtext = 'Meta Anual de Leitura',
                    bootstyle = 'primary',
                    meterthickness=15
                    )
        meter.pack(expand=True, fill='both', padx=10, pady=10)
        
        
        # buttons
        font_buttons = ctk.CTkFont(family=FONT, size=24, weight='bold')
        frame_buttons = ctk.CTkFrame(master=parent, fg_color=DARK_GRAY)
        frame_buttons.grid(column=0, row=0, rowspan=7, sticky='nsew')
        frame_buttons.columnconfigure(0, weight=1, uniform='f')
        frame_buttons.rowconfigure((0,1,2,3,4,5,6,7,8,9), weight=1, uniform='f')
        
        self.parent = parent
        self.frame_buttons = frame_buttons
        
        window1 = self.Animated_Window1()
        
        book_image = Image.open('apps/e-library/images/open-book_1f4d6.png')
        book_ctk = ctk.CTkImage(book_image, size=(30,30))
        
        money_image = Image.open('apps/e-library/images/money-bag_1f4b0.png')
        money_ctk = ctk.CTkImage(money_image, size=(30,30))
        
        pin_image = Image.open('apps/e-library/images/pushpin_1f4cc.png')
        pin_ctk = ctk.CTkImage(pin_image, size=(30,30))
        
 
        
        # button1
        button1 = ctk.CTkButton(master=frame_buttons, text=' Meus Livros', 
                                command= window1.animate,
                                border_spacing=10,
                                fg_color='transparent',
                                text_color=LIGHT_BLUE,
                                hover_color=BLACK,
                                font=font_buttons,
                                corner_radius=0,
                                anchor='w',
                                #image=book_ctk
                                )
        button1.grid(column=0, row=2, sticky='ew')
        #button1.place(relx=0.5, rely=0.10, relwidth = 1, relheight = 0.1, anchor='center')
       
        
        
        # button2
        button2 = ctk.CTkButton(master=frame_buttons, text=' Lista de Desejos', 
                                fg_color='transparent',
                                border_spacing=10,
                                text_color=LIGHT_BLUE,
                                hover_color=BLACK,
                                font=font_buttons,
                                corner_radius=0,
                                anchor='w',
                                #image=money_ctk
                                )
        button2.grid(column=0, row=3, sticky='ew')
        #button2.place(relx=0.5, rely=0.25, relwidth = 1, relheight = 0.1, anchor='center')
        
 
        

        # button3
        button3 = ctk.CTkButton(master=frame_buttons, text=' Meta de Leitura', 
                                fg_color='transparent',
                                border_spacing=10,
                                text_color=LIGHT_BLUE,
                                hover_color=BLACK,
                                font=font_buttons,
                                corner_radius=0,
                                anchor='w',
                                #image=pin_ctk
                                )
        button3.grid(column=0, row=4, sticky='ew')
        #button3.place(relx=0.5, rely=0.40, relwidth = 1, relheight = 0.1, anchor='center')
        
        # button4
        button4 = ctk.CTkButton(master=frame_buttons, text='Creditos', 
                                fg_color=LIGHT_BLUE,
                                text_color=BLACK,
                                font=font_buttons,
                                )
        #button4.place(relx=0.5, rely=0.9, relwidth = 1, relheight = 0.1, anchor='center')
        
        

    def Animated_Window1(self):
        # animated widget
        animated_panel = SlidePanel(self.parent, 1.0, 0.25, self.frame_buttons)
        
        Window1(animated_panel)
        
        return animated_panel


class Window1():
    def __init__(self, parent):
        
        self.bool_window = False
        
        # layout
        parent.columnconfigure(0, weight=1, uniform='a')
        parent.rowconfigure((0,1,2,3,4,5,6,7,8,9), weight=1, uniform='a')
        
        
        # frames
        main_frame = ctk.CTkFrame(parent, corner_radius=20, fg_color='transparent')
        main_frame.grid(column=0, row=0, sticky='nsew', pady=0, padx=10)
        
        main_frame.columnconfigure(0, weight=1, uniform='b')
        main_frame.columnconfigure(1, weight=8, uniform='b')
        main_frame.rowconfigure(0, weight=1, uniform='b')
        
        back_frame = ctk.CTkFrame(main_frame, corner_radius=100, fg_color='transparent')
        back_frame.grid(column=0, row=0, sticky='ns', pady=0)
        
        font_buttons = ctk.CTkFont(family=FONT, size=24, weight='bold')
        frame_books = ctk.CTkFrame(master=parent, fg_color='transparent', corner_radius=20)
        frame_books.grid(column=0, row=2, rowspan=7, sticky='nswe', padx=15)
        
        frame_add_book = ctk.CTkFrame(master=parent, fg_color='transparent', corner_radius=20)
        frame_add_book.grid(column=0, row=9, sticky='ns', padx=15, pady=10)
        




        # text top
        font = ctk.CTkFont(family=FONT, size=INPUT_FONT_SIZE, weight='bold')
        text_top = ctk.CTkLabel(master=main_frame, text='Meus Livros', text_color=BLACK, font=font,
                                fg_color=LIGHT_BLUE,
                                 corner_radius=20)
        text_top.grid(column=1, row=0, sticky='nsew', pady=0, padx=5)
        
        # back button
        voltar = ctk.CTkButton(master=back_frame, text='>>', 
                                command= parent.animate,
                                fg_color=LIGHT_BLUE,
                                text_color=BLACK,
                                font=font_buttons,
                                corner_radius=100)
        voltar.pack(padx=5, pady=0, expand=True, fill='both')
        
        # add book button
        add_book = ctk.CTkButton(master=frame_add_book, text='+', 
                                command= self.window_add_book,
                                fg_color=LIGHT_BLUE,
                                text_color=BLACK,
                                font=font_buttons,
                                corner_radius=100)
        add_book.pack(expand=True, fill='both')
        
    def window_add_book(self):
        if not self.bool_window:
            global extra
            extra = ctk.CTkToplevel()
            extra.title('Adicionar Livro')
            extra.geometry('500x400')
            extra.resizable(False, False)
            
            # layout
            extra.columnconfigure(0, weight=1, uniform='c')
            extra.rowconfigure((0,1,2,3,4,5,6,7,8,9), weight=1, uniform='c')
            
            # frames
            main_frame = ctk.CTkFrame(extra, corner_radius=20, fg_color='transparent')
            main_frame.grid(column=0, row=2, rowspan=8, sticky='nsew', pady=10, padx=10)
            
            main_frame.columnconfigure(0, weight=1, uniform='d')
            main_frame.rowconfigure((0,1,2,3,4,5,6,7,8,9), weight=1, uniform='d')
            
            title_frame = ctk.CTkFrame(main_frame, corner_radius=20, fg_color='transparent')
            title_frame.grid(column=0, row=2, sticky='nsew', pady=5)
            
            author_frame = ctk.CTkFrame(main_frame, corner_radius=20, fg_color='transparent')
            author_frame.grid(column=0, row=3, sticky='nsew', pady=5)
            
            year_frame = ctk.CTkFrame(main_frame, corner_radius=20, fg_color='transparent')
            year_frame.grid(column=0, row=4, sticky='nsew', pady=5)
            
            score_frame = ctk.CTkFrame(main_frame, corner_radius=20, fg_color='transparent')
            score_frame.grid(column=0, row=5, rowspan=9, sticky='nsew', pady=5)

            
            # widgets
            font_entry = ctk.CTkFont(family=FONT, size=18, weight='bold')
            
            title_label = ctk.CTkLabel(master=title_frame, text='Título:', text_color=WHITE, font=font_entry,
                                    #    fg_color=LIGHT_BLUE,
                                       corner_radius=20)
            title_label.pack(side='left')
            
            # title_entry = ctk.CTkEntry(master=title_frame, font=font_entry,
            #                            border_color=LIGHT_BLUE, height=20,
            #                            placeholder_text='Digite o título do livro')
            title_entry = ttk.Entry(title_frame, font=font_entry, 
                                    foreground=LIGHT_BLUE)
            title_entry.pack(side='left', fill='x', expand=True)
            
            
            author_label = ctk.CTkLabel(master=author_frame, text='Autor:', text_color=WHITE, font=font_entry,
                                    #    fg_color=LIGHT_BLUE,
                                       corner_radius=20)
            author_label.pack(side='left')
            # author_entry = ctk.CTkEntry(master=author_frame, font=font_entry,
            #                            border_color=LIGHT_BLUE, height=20)
            author_entry = ttk.Entry(author_frame, font=font_entry,
                                    foreground=LIGHT_BLUE)
            author_entry.pack(side='left', fill='x', expand=True)
            
            
            year_label = ctk.CTkLabel(master=year_frame, text='Ano:   ', text_color=WHITE, font=font_entry,
                                      #    fg_color=LIGHT_BLUE,
                                       corner_radius=20)
            year_label.pack(side='left')
            # year_entry = ctk.CTkEntry(master=year_frame, font=font_entry,
            #                         border_color=LIGHT_BLUE, height=20, width=70
            #                            )
            year_int = tk.IntVar(value = date.today().year)
            year_spin = ttk.Spinbox(year_frame, from_ = 1900, 
                                    to = date.today().year, width=4,
                                    increment = 1, textvariable = year_int,
                                    command=lambda: print(year_int.get()))
            year_spin.pack(side='left')
            obs_label = ctk.CTkLabel(master=year_frame, text='*ano em que você terminou a leitura', text_color=WHITE, font=font_entry,
     
                                       )
            obs_label.pack(side='right', padx=5)
            
            
            
            
            
            
            
            
            
            
            
            self.bool_window = True
            
            # Adicionando uma função para ser chamada quando a janela é fechada
            extra.protocol("WM_DELETE_WINDOW", self.on_window_close)
        else:
            # TODO: Emitir um alerta de que a janela já está aberta
            pass
            
    def on_window_close(self):
        # Esta função será chamada quando a janela for fechada
        global extra
        extra.destroy()  # Destrua a janela Toplevel
        self.bool_window = False  # Defina a variável bool_window como False
   
            
            
            
    
            
                
        
        

        

class SlidePanel(ctk.CTkFrame):
    def __init__(self, parent, start_pos, end_pos, frame_buttons):
        super().__init__(master = parent)
        self.frame_buttons = frame_buttons

        # general attributes 
        self.start_pos = start_pos 
        self.end_pos = end_pos 
        self.width = abs(start_pos - end_pos)

        # animation logic
        self.pos = self.start_pos
        self.in_start_pos = True

        # layout
        self.place(relx = self.start_pos, rely = 0, relwidth = self.width, relheight = 1)
        

    def animate(self):
        if self.in_start_pos:
            self.animate_forward(frame_buttons=self.frame_buttons)
        else:
            self.animate_backwards()

    def animate_forward(self, frame_buttons=None):
        if self.pos > self.end_pos:
            self.pos -= 0.05
            self.place(relx = self.pos, rely = 0, relwidth = self.width, relheight = 1)
            self.after(16, self.animate_forward)
        else:
            # if frame_buttons:
            #     for widget in frame_buttons.winfo_children():
            #         widget.destroy()
            self.in_start_pos = False
            

    def animate_backwards(self):
        if self.pos < self.start_pos:
            self.pos += 0.05
            self.place(relx = self.pos, rely = 0, relwidth = self.width, relheight = 1)
            self.after(16, self.animate_backwards)
        else:
            self.in_start_pos = True




if __name__ == '__main__':
    App()