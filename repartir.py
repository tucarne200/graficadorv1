import pandas as pd
import tkinter as tk
from tkinter import filedialog

# Función para cargar el archivo Excel
def cargar_archivo():
    ruta_archivo = filedialog.askopenfilename(title="Seleccionar archivo Excel", filetypes=[("Archivos Excel", "*.xlsx;*.xls")])
    if ruta_archivo:
        return pd.read_excel(ruta_archivo)
    return None

# Función para distribuir equitativamente los nombres en la columna "Agente"
def distribuir_nombres(dataframe, nombres):
    total_filas = len(dataframe)
    nombres_repetidos = nombres * (total_filas // len(nombres)) + nombres[:total_filas % len(nombres)]
    dataframe['Agente'] = nombres_repetidos
    return dataframe

# Función para manejar la entrada de nombres desde la interfaz gráfica
def obtener_nombres_desde_interfaz():
    root = tk.Tk()
    root.withdraw()

    # Ventana emergente para ingresar nombres
    nombres_input = tk.simpledialog.askstring("Ingresar Nombres", "Ingrese los nombres separados por comas:")
    root.destroy()

    if nombres_input:
        return [nombre.strip() for nombre in nombres_input.split(',')]
    else:
        return []

# Función para guardar el archivo Excel modificado
def guardar_archivo(dataframe):
    ruta_guardar = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Archivos Excel", "*.xlsx")])
    if ruta_guardar:
        dataframe.to_excel(ruta_guardar, index=False)
        print(f"Archivo guardado en {ruta_guardar}")

# Función principal
def main():
    # Crear la interfaz gráfica
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal

    # Cargar el archivo Excel
    archivo_df = cargar_archivo()
    if archivo_df is None:
        print("No se seleccionó un archivo. Saliendo...")
        return

    # Obtener los nombres desde la interfaz gráfica
    nombres_input = obtener_nombres_desde_interfaz()

    # Distribuir equitativamente los nombres en la columna "Agente"
    archivo_modificado = distribuir_nombres(archivo_df.copy(), nombres_input)

    # Guardar el archivo modificado
    guardar_archivo(archivo_modificado)

if __name__ == "__main__":
    main()
