import customtkinter as ctk

class Calculadora(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora de Fórmulas")
        self.geometry("300x300")

        ctk.CTkLabel(self, text="Aquí va la calculadora").pack(pady=20)
        ctk.CTkButton(self, text="Cerrar", command=self.destroy).pack(pady=10)
