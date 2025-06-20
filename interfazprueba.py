import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog, Label, Button, Canvas
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class AnalisisDatosGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Análisis de Datos")

        self.label = Label(root, text="Arrastra y suelta un archivo Excel aquí:")
        self.label.pack(pady=20)

        self.button = Button(root, text="Seleccionar Archivo", command=self.cargar_archivo)
        self.button.pack(pady=20)

    def cargar_archivo(self):
        archivo_path = filedialog.askopenfilename(filetypes=[("Archivos Excel", "*.xlsx;*.xls")])
        if archivo_path:
            self.realizar_analisis(archivo_path)

    def realizar_analisis(self, archivo_path):
        df = pd.read_excel(archivo_path)

        # Realizar análisis de datos y generar gráficos
        self.generar_graficos(df)

    def generar_graficos(self, df):
        # Resto del código para el análisis y visualización...
        fig, axes = plt.subplots(3, 2, figsize=(15, 15))

        # Agrega aquí el código para los gráficos según tus necesidades.
        df['Agente'].value_counts().plot(kind='bar', ax=axes[0, 0], color='skyblue')
        axes[0, 0].set_title('Carga de Trabajo por Agente')

        df['Ejecutivo pre asignado'].value_counts().plot(kind='bar', ax=axes[0, 1], color='salmon')
        axes[0, 1].set_title('Carga de Trabajo por Ejecutivo Pre Asignado')

        df['Ciudad'].value_counts().head(10).plot(kind='bar', ax=axes[1, 0], color='lightgreen')
        axes[1, 0].set_title('Ciudades más Repetidas')

        df['Estado'].value_counts().head(10).plot(kind='bar', ax=axes[1, 1], color='lightcoral')
        axes[1, 1].set_title('Estados más Repetidos')

        cliente_relacion = df['Cliente'].value_counts()
        cliente_relacion.plot(kind='pie', autopct='%1.1f%%', colors=['gold', 'lightcoral'], ax=axes[2, 0])
        axes[2, 0].set_title('Relación Cliente/No Cliente')

        giro_relacion = df['Giro'].apply(lambda x: 'Lleno' if pd.notna(x) else 'Vacío').value_counts()
        giro_relacion.plot(kind='pie', autopct='%1.1f%%', colors=['lightblue', 'lightpink'], ax=axes[2, 1])
        axes[2, 1].set_title('Relación Giro Lleno/Vacío')

        plt.tight_layout()

        # Muestra una ventana con los gráficos
        self.mostrar_ventana_graficos()

    def mostrar_ventana_graficos(self):
        plt.show()

if __name__ == "__main__":
    root = Tk()
    gui = AnalisisDatosGUI(root)
    root.mainloop()
