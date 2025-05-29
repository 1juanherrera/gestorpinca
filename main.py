from ui.menu import Menu
from excel_reader import cargar_datos
from logic import filtrar_por_producto

if __name__ == "__main__":
    df = cargar_datos()
    app = Menu(df, filtrar_por_producto)
    app.mainloop()
