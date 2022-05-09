import datetime
import csv
import os
from typing import Counter
ruta_completa = os.getcwd()
ruta_archivos_csv = os.path.join(ruta_completa,'BBB_nuevo.csv')

def leer_archivo():
    with open(ruta_archivos_csv,encoding= 'utf-8') as archivo:
        data_net = csv.reader(archivo,delimiter=',')
        header = next(data_net)
        datos = list(data_net)
    return datos

def dia_mas_comun(datos):
    dias_semana = ['lunes','martes','miercoles','jueves','viernes'
    'sabado','domingo']
    formato = "%d/%m/%Y %H:%M"


    lista = "".join(list(map(lambda x: str
    (datetime.datetime.strptime(x[0],formato).weekday()), datos)))

    masComun = Counter(lista).most_common(1)
    tupla = (dias_semana[int(masComun[0][0])],masComun[0][1])
    return tupla


def total(datos):
    formato = "%d/%m/%Y %H:%M"
    primer_Reg = datetime.datetime.strptime(datos[0][0],formato)
    ult_reg = datetime.datetime.strptime(datos[len(datos)-1][0],formato)
    time_Dif = primer_Reg - ult_reg
    return time_Dif

def main():
    datos= leer_archivo
    print(dia_mas_comun(datos))
    print(total(datos))

if __name__ == '__main__':
    main()


        