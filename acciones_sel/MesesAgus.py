import os
import openpyxl
from tkinter import filedialog
from tkinter import Tk
from openpyxl.styles import PatternFill  # Importamos el estilo para el color de fondo

# Ruta base donde se encuentran las carpetas de los meses
ruta_base = r"C:\Users\Diot en 0 ext\Desktop\Diot en 0 ext online complementaria\acuses\2025"

# Función para seleccionar la subcarpeta dentro de la ruta base
def seleccionar_subcarpeta():
    root = Tk()
    root.withdraw()  # Oculta la ventana principal
    carpeta_seleccionada = filedialog.askdirectory(initialdir=ruta_base, title="Selecciona la carpeta del mes")
    return carpeta_seleccionada

# Función para obtener los nombres de los PDFs en la carpeta seleccionada
def obtener_nombres_pdfs(carpeta):
    nombres_pdfs = []
    for archivo in os.listdir(carpeta):
        if archivo.endswith(".pdf"):
            # Extraer solo la parte entre los primeros dos puntos
            partes = archivo.split(".")
            if len(partes) > 1:
                identificador = partes[1]  # El valor entre el primer y segundo punto
                nombres_pdfs.append(identificador)  # Agregar el identificador a la lista
    return nombres_pdfs

# Función para leer el archivo Excel
def leer_excel(ruta_excel):
    wb = openpyxl.load_workbook(ruta_excel)
    hoja_fisca = wb["Fisica"]
    hoja_moral = wb["Moral"]
    return wb, hoja_fisca, hoja_moral

# Función para verificar si los PDFs están en las hojas Fisca y Moral
def verificar_pdfs(wb, hoja_fisca, hoja_moral, nombres_pdfs):
    # Estilos para las celdas
    verde = PatternFill(start_color="00FF00", end_color="00FF00", fill_type="solid")  # Color verde
    rojo = PatternFill(start_color="FF0000", end_color="FF0000", fill_type="solid")  # Color rojo

    # Verificar en la hoja Fisca
    for row in range(2, hoja_fisca.max_row + 1):  # Empezamos desde la fila 2 (para saltar el encabezado)
        nombre_fisca = hoja_fisca.cell(row=row, column=1).value  # Leer el nombre de la columna A
        if nombre_fisca and nombre_fisca in nombres_pdfs:
            hoja_fisca.cell(row=row, column=5).value = "Se encuentra"  # Colocar "Se encuentra" en la columna D
            hoja_fisca.cell(row=row, column=5).fill = verde  # Colocar color verde en la celda
        else:
            hoja_fisca.cell(row=row, column=5).value = "No se encuentra"  # Colocar "No se encuentra" en la columna D
            hoja_fisca.cell(row=row, column=5).fill = rojo  # Colocar color rojo en la celda
    
    # Verificar en la hoja Moral
    for row in range(2, hoja_moral.max_row + 1):  # Empezamos desde la fila 2
        nombre_moral = hoja_moral.cell(row=row, column=1).value  # Leer el nombre de la columna A
        if nombre_moral and nombre_moral in nombres_pdfs:
            hoja_moral.cell(row=row, column=5).value = "Se encuentra"  # Colocar "Se encuentra" en la columna D
            hoja_moral.cell(row=row, column=5).fill = verde  # Colocar color verde en la celda
        else:
            hoja_moral.cell(row=row, column=5).value = "No se encuentra"  # Colocar "No se encuentra" en la columna D
            hoja_moral.cell(row=row, column=5).fill = rojo  # Colocar color rojo en la celda
    
    # Guardar los cambios en el archivo Excel
    wb.save("DATA.xlsx")

def main():
    # Seleccionar la subcarpeta dentro de la ruta base
    carpeta = seleccionar_subcarpeta()
    if not carpeta:
        print("No se seleccionó ninguna carpeta.")
        return
    
    # Obtener los nombres de los PDFs en la carpeta seleccionada
    nombres_pdfs = obtener_nombres_pdfs(carpeta)

    # Seleccionar el archivo Excel
    ruta_excel = filedialog.askopenfilename(title="Selecciona el archivo Excel", filetypes=[("Excel Files", "*.xlsx")])
    if not ruta_excel:
        print("No se seleccionó ningún archivo Excel.")
        return
    
    # Leer el archivo Excel
    wb, hoja_fisca, hoja_moral = leer_excel(ruta_excel)

    # Verificar la existencia de los PDFs en las hojas Fisca y Moral
    verificar_pdfs(wb, hoja_fisca, hoja_moral, nombres_pdfs)
    print("Proceso completado. El archivo actualizado se guardó como 'archivo_actualizado.xlsx'.")

if __name__ == "__main__":
    main()
