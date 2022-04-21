import csv
from collections import Counter


ruta_archivo = 'C:\\Users\\Bruno\\OneDrive\\Escritorio\\Facultadf\\sem-py\\Python\\Actividades\\Actividad 1\\TOTAL_nuevo.csv'

archivo = open(ruta_archivo,"r", encoding='utf8')

csvreader = csv.reader(archivo, delimiter=',')
encabezado = next(csvreader)

def filtrar():
    lista_usuarios=[]
    for linea in csvreader:
        lista_usuarios.append(linea[1])
    return lista_usuarios

def imprimir_3(list,c):
    mas_comunes = c.most_common(3)
    print('Los mas comunes fueron')
    for i in range(3):
        print(f'{mas_comunes[i][0]:<18}')



lista_us = filtrar()
c = Counter(lista_us)
imprimir_3(lista_us,c)

