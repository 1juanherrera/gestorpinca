import customtkinter as ctk

class Costos(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Costos")
        self.geometry("300x300")

        ctk.CTkLabel(self, text="Costos").pack(pady=20)
        ctk.CTkButton(self, text="Cerrar", command=self.destroy).pack(pady=10)
