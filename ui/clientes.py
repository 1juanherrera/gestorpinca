import customtkinter as ctk

class Clientes(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Clientes")
        self.geometry("300x300")

        ctk.CTkLabel(self, text="Clientes").pack(pady=20)
        ctk.CTkButton(self, text="Cerrar", command=self.destroy).pack(pady=10)
