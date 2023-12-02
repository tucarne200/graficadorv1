import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo Excel
archivo_excel = 'Ejercicio de dcto.xlsx'
df = pd.read_excel(archivo_excel)

# Gráfico de barras para "Paquete"
plt.figure(figsize=(10, 6))
df['Paquete'].value_counts().nlargest(10).plot(kind='bar', title='Paquete más repetido')
plt.show()

# Gráfico de barras para "Línea"
plt.figure(figsize=(10, 6))
df['Línea'].value_counts().nlargest(10).plot(kind='bar', title='Línea más repetida')
plt.show()

# Gráfico de barras para "Categoría"
plt.figure(figsize=(10, 6))
df['Categoría'].value_counts().nlargest(10).plot(kind='bar', title='Categoría más repetida')
plt.show()

# Gráfico de pastel para "Precio de lista"
precio_bins = [0, 7000, 20000, 40000]
precio_labels = ['500-7000', '7001-20000', '20001-40000']

plt.figure(figsize=(8, 8))
df['Precio de lista'].plot(kind='hist', bins=precio_bins, rwidth=0.8, align='left', color=['blue', 'orange', 'green'], title='Precio de lista')
plt.xticks(precio_bins[:-1], precio_labels)
plt.show()

# Repite el proceso para "Precio B"

# Gráfico de barras para "Proveedor"
plt.figure(figsize=(10, 6))
df['Proveedor'].value_counts().nlargest(10).plot(kind='bar', title='Proveedor más repetido')
plt.show()

# Mayor "Existencia Actual" por "Código"
max_existencia = df.groupby('Código')['Existencia Actual'].max().nlargest(10).reset_index()
max_existencia.plot(kind='bar', x='Código', y='Existencia Actual', title='Mayor Existencia Actual por Código')
plt.show()

# Gráfico de barras para "Marca"
plt.figure(figsize=(10, 6))
df['Marca'].value_counts().nlargest(10).plot(kind='bar', title='Marca más repetida')
plt.show()

# Gráfico de pastel para "Publicar en Web"
plt.figure(figsize=(8, 8))
df['Publicar en Web'].value_counts().plot(kind='pie', autopct='%1.1f%%', title='Publicar en Web')
plt.show()

# Pausa la ejecución hasta que presiones Enter
input("Presiona Enter para salir...")
