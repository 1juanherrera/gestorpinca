import customtkinter as ctk

class Produccion(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Produccion")
        self.geometry("300x300")

        ctk.CTkLabel(self, text="Produccion").pack(pady=20)
        ctk.CTkButton(self, text="Cerrar", command=self.destroy).pack(pady=10)
