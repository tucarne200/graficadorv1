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
        ax
    root = Tk()
    gui = AnalisisDatosGUI(root)
    root.mainloop()
