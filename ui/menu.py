import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk
from ui.inventario import InventarioView

class Menu(ttk.Window):
    def __init__(self, df, filtrar_por_producto):
        super().__init__(themename="flatly")
        self.df = df
        self.filtrar_por_producto = filtrar_por_producto

        self.iconbitmap("assets/icon.ico")
        self.title("Pinca S.A.S")
        self.geometry("900x800")

        self.mostrar_menu()

    def abrir_calculadora(self):
        print("Aquí se abrirá la calculadora")

    def abrir_inventario(self):
        self.menu_frame.destroy()
        self.inventario_frame = InventarioView(self, self.df)
        self.inventario_frame.pack(expand=True, fill="both")

    def abrir_clientes(self):
        print("Aquí se abrirá la sección de clientes")

    def abrir_produccion(self):
        print("Aquí se abrirá la sección de producción")

    def abrir_costos(self):
        print("Aquí se abrirá la sección de costos")
    
    def mostrar_menu(self):
        self.menu_frame = ttk.Frame(self, padding=30)
        self.menu_frame.pack(expand=True, fill="both")

        # Imagen (usa ImageTk para ttkbootstrap)
        image_path = "assets/pincalogo.png"
        img = Image.open(image_path).resize((150, 150))
        photo = ImageTk.PhotoImage(img)
        image_label = ttk.Label(self.menu_frame, image=photo)
        image_label.image = photo  # Referencia para evitar garbage collection
        image_label.pack(pady=10)

        # Título grande y en negrita
        titulo = ttk.Label(
            self.menu_frame,
            text="Menú Principal",
            font=("Arial", 24, "bold")
        )
        titulo.pack(pady=(0, 20))

        # --- ESTILO PERSONALIZADO PARA BOTONES ---
        # ...dentro de mostrar_menu o __init__...
        style = ttk.Style()
        for bootstyle in ["primary", "info", "success", "warning", "danger"]:
            style.configure(f"{bootstyle}.TButton", font=("Arial", 16, "bold"), padding=10)

        ttk.Button(self.menu_frame, text="Calculadora", command=self.abrir_calculadora, bootstyle="primary", width=22).pack(pady=15)
        ttk.Button(self.menu_frame, text="Inventario", command=self.abrir_inventario, bootstyle="info", width=22).pack(pady=15)
        ttk.Button(self.menu_frame, text="Clientes", command=self.abrir_clientes, bootstyle="success", width=22).pack(pady=15)
        ttk.Button(self.menu_frame, text="Producción", command=self.abrir_produccion, bootstyle="warning", width=22).pack(pady=15)
        ttk.Button(self.menu_frame, text="Costos", command=self.abrir_costos, bootstyle="danger", width=22).pack(pady=15)