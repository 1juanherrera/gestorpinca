def filtrar_por_producto(df, producto):
    return df[df.apply(lambda row: producto in str(row.to_string()), axis=1)]