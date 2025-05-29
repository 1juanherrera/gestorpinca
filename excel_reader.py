import pandas as pd

def cargar_datos(path='data/DUPLICADOS.xlsx', hoja="INVENTARIO", header=2):
    try:
        df = pd.read_excel(path, sheet_name=hoja, header=header)
        return df
    except Exception as e:
        print(f"Error al leer el Excel: {e}")
        return pd.DataFrame()
