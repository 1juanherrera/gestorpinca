import customtkinter as ctk
from PIL import Image, ImageTk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

class Menu(ctk.CTk):
    def __init__(self, df, filtrar_por_producto):
        super().__init__()
        self.df = df
        self.filtrar_por_producto = filtrar_por_producto

        self.iconbitmap("assets/icon.ico")

        self.title("Pinca S.A.S - Menú Principal")
        self.geometry("800x600")

        # Carga y Configuración de estilo de imagen
        image_path = "assets/pincalogo.png"
        image = ctk.CTkImage(light_image=Image.open(image_path), size=(150, 150))

        # Mostrar imagen
        image_label = ctk.CTkLabel(self, image=image, text="")
        image_label.pack(pady=10)

        # Botones del menú principal
        ctk.CTkButton(self, text="Calculadora", command=self.abrir_calculadora).pack(pady=15)
        ctk.CTkButton(self, text="Inventario", command=self.abrir_inventario).pack(pady=15)
        ctk.CTkButton(self, text="Clientes", command=self.abrir_clientes).pack(pady=15)
        ctk.CTkButton(self, text="Producción", command=self.abrir_produccion).pack(pady=15)
        ctk.CTkButton(self, text="Costos", command=self.abrir_costos).pack(pady=15)

    def abrir_calculadora(self):
        print("Aquí se abrirá la calculadora")

    def abrir_inventario(self):
        print("Aquí se abrirá el inventario (desglosado en materia prima y productos)")

    def abrir_clientes(self):
        print("Aquí se abrirá la sección de clientes")

    def abrir_produccion(self):
        print("Aquí se abrirá la sección de producción")

    def abrir_costos(self):
        print("Aquí se abrirá la sección de costos")
