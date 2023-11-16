from customtkinter import CTkFrame, CTkLabel, CTkButton, CTk


class RatingWidget(CTkFrame):
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.create_widgets()

    def create_widgets(self):
        self.label = CTkLabel(self, text="Avaliação:")
        self.label.grid(row=0, column=0, padx=5)

        # Use o ttk.Scale para criar a escala deslizante
        self.scale = ttk.Scale(self, from_=0, to=10, orient=tk.HORIZONTAL, length=200)
        self.scale.grid(row=0, column=1, padx=5)

        self.label_value = CTkLabel(self, text="Nota: 0")
        self.label_value.grid(row=0, column=2, padx=5)

        # Configura um rastreador de variável para monitorar a mudança de valor
        self.scale_var = tk.DoubleVar()
        self.scale["variable"] = self.scale_var
        self.scale_var.trace_add("write", self.update_label)

    def update_label(self, *args):
        # Atualiza o rótulo de acordo com o valor da escala
        self.label_value["text"] = f"Nota: {self.scale_var.get()}"

# Exemplo de uso
if __name__ == "__main__":
    root = CTk()
    root.title("Avaliação do Livro")

    rating_widget = RatingWidget(root)
    rating_widget.pack(padx=20, pady=20)

    root.mainloop()