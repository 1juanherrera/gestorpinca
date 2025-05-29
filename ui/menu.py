import customtkinter as ctk
from PIL import Image
from ui.inventario import InventarioView

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

class Menu(ctk.CTk):
    def __init__(self, df, filtrar_por_producto):
        super().__init__()
        self.df = df
        self.filtrar_por_producto = filtrar_por_producto

        self.iconbitmap("assets/icon.ico")
        self.title("Pinca S.A.S")
        self.geometry("800x600")

        self.mostrar_menu()  # SOLO esta línea, elimina el bloque duplicado

    def abrir_calculadora(self):
        print("Aquí se abrirá la calculadora")

    def abrir_inventario(self):
        # Quita el menú
        self.menu_frame.destroy()
        # Muestra el inventario
        self.inventario_frame = InventarioView(self, self.df)
        self.inventario_frame.pack(expand=True, fill="both")

    def abrir_clientes(self):
        print("Aquí se abrirá la sección de clientes")

    def abrir_produccion(self):
        print("Aquí se abrirá la sección de producción")

    def abrir_costos(self):
        print("Aquí se abrirá la sección de costos")
    
    def mostrar_menu(self):
        self.menu_frame = ctk.CTkFrame(self)
        self.menu_frame.pack(expand=True, fill="both")

        image_path = "assets/pincalogo.png"
        image = ctk.CTkImage(light_image=Image.open(image_path), size=(150, 150))
        image_label = ctk.CTkLabel(self.menu_frame, image=image, text="")
        image_label.pack(pady=10)

        ctk.CTkButton(self.menu_frame, text="Calculadora", command=self.abrir_calculadora).pack(pady=15)
        ctk.CTkButton(self.menu_frame, text="Inventario", command=self.abrir_inventario).pack(pady=15)
        ctk.CTkButton(self.menu_frame, text="Clientes", command=self.abrir_clientes).pack(pady=15)
        ctk.CTkButton(self.menu_frame, text="Producción", command=self.abrir_produccion).pack(pady=15)
        ctk.CTkButton(self.menu_frame, text="Costos", command=self.abrir_costos).pack(pady=15)