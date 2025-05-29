import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import pandas as pd

class InventarioView(ttk.Frame):
    def __init__(self, master, df, df_productos=None):
        super().__init__(master, padding=10)
        self.df = df
        self.df_productos = df_productos

        # --- ESTILOS PERSONALIZADOS ---
        style = ttk.Style()
        style.theme_use("flatly")
        style.configure("Treeview.Heading", background="#6c757d", foreground="white", font=("Arial", 16, "bold"))
        style.configure("Treeview", font=("Arial", 11), rowheight=30)
        style.configure("TButton", font=("Arial", 14, "bold"), padding=10)
        style.map("Treeview",
            background=[("selected", "#FF0000")],
            foreground=[("selected", "white")]
        )

        # Botón Atrás
        btn_atras = ttk.Button(
            self, text="Atrás", command=self.volver_al_menu, bootstyle="danger", width=14
        )
        btn_atras.pack(pady=(10, 0), anchor="w", padx=20)

        # Título
        self.titulo = ttk.Label(self, text="Inventario - Materia Prima", font=("Arial", 22, "bold"))
        self.titulo.pack(pady=(10, 0))

        # Botones de selección centrados
        botones_frame = ttk.Frame(self)
        botones_frame.pack(pady=(10, 0))
        btn_productos = ttk.Button(
            botones_frame, text="Productos", command=self.mostrar_productos, bootstyle="info", width=18
        )
        btn_productos.pack(side="left", padx=10)
        btn_materia_prima = ttk.Button(
            botones_frame, text="Materia Prima", command=self.mostrar_materia_prima, bootstyle="info", width=18
        )
        btn_materia_prima.pack(side="left", padx=10)

        # Definir columnas fijas (ajusta a los nombres de tu DataFrame)
        self.columnas = ["CODIGO", "NOMBRE", "COSTO UNITARIO"]

        # Tabla de inventario
        self.tree = ttk.Treeview(
            self,
            columns=self.columnas,
            show='headings'
        )
        for col in self.columnas:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor='center', width=200)
        self.tree.pack(expand=True, fill='both', pady=20, padx=20)

        self.mostrar_materia_prima()

    def mostrar_materia_prima(self):
        self.titulo.config(text="Inventario - Materia Prima")
        self.tree.delete(*self.tree.get_children())
        self.tree["columns"] = self.columnas
        for col in self.columnas:
            if col == "NOMBRE":
                self.tree.heading(col, text="  NOMBRE")
            elif col == "COSTO UNITARIO":
                self.tree.heading(col, text="      COSTO UNITARIO")
            else:
                self.tree.heading(col, text=col)
        # ...existing code...
        for col in self.columnas:
            if col == "NOMBRE":
                self.tree.column(col, anchor='w', width=300)
            elif col == "COSTO UNITARIO":
                self.tree.column(col, anchor='w', width=120)  # Cambiado a 'w' para alinear a la izquierda
            else:
                self.tree.column(col, anchor='center', width=100)
        # ...existing code...
        for _, row in self.df.iterrows():
            costo_unitario = f"$ {row['COSTO UNITARIO']:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
            self.tree.insert(
                "", "end",
                values=[
                    row["CODIGO"],
                    row["NOMBRE"],
                    costo_unitario,
                ]
            )

    def mostrar_productos(self):
        self.titulo.config(text="Inventario - Productos")
        self.tree.delete(*self.tree.get_children())
        self.tree["columns"] = self.columnas
        for col in self.columnas:
            if col == "NOMBRE":
                self.tree.heading(col, text="  NOMBRE")
            elif col == "COSTO UNITARIO":
                self.tree.heading(col, text="      COSTO UNITARIO")
            else:
                self.tree.heading(col, text=col)
        for col in self.columnas:
            if col == "NOMBRE":
                self.tree.column(col, anchor='w', width=300)
            elif col == "COSTO UNITARIO":
                self.tree.column(col, anchor='e', width=120)
            else:
                self.tree.column(col, anchor='center', width=100)
        if self.df_productos is not None:
            for _, row in self.df_productos.iterrows():
                costo_unitario = f"$ {row['COSTO UNITARIO']:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
                self.tree.insert(
                    "", "end",
                    values=[
                        row["CODIGO"],
                        row["NOMBRE"],
                        costo_unitario,
                    ]
                )
        else:
            self.tree.insert("", "end", values=["No hay productos", "", ""])

    def volver_al_menu(self):
        self.destroy()
        if hasattr(self.master, "mostrar_menu"):
            self.master.mostrar_menu()