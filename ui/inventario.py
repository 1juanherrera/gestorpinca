import customtkinter as ctk

class Inventario(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Inventario")
        self.geometry("300x300")

        ctk.CTkLabel(self, text="Inventario").pack(pady=20)
        ctk.CTkButton(self, text="Cerrar", command=self.destroy).pack(pady=10)
