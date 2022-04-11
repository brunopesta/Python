""" Generar una estructura con los nombres de los estudiantes y la suma de ambas notas.
• Calcular el promedio de las notas totales e informar que alumnos obtuvieron menos que el
promedio.
"""

import encodings


def CrearEstrucutra():
    with open(r"sem-py\Python\Practica\Practica2\eval1.txt") as arch_eval1:
        arch_eval1 = arch_eval1.read()
    with open(r"sem-py\Python\Practica\Practica2\eval2.txt") as archivo_evaluacion2:
        arch_eval2 = archivo_evaluacion2.read()
    with open (r"sem-py\Python\Practica\Practica2\nombres_1(1).txt", encoding = 'utf8') as arch_nombres:
        nombres = arch_nombres.read()

    nicknames = nombres.replace(",", "").replace("'", "").lower().split()
    eva1 = arch_eval1.replace(",", "").split()
    eva2 = arch_eval2.replace(",", "").split()

    lista = []
    for n in range(len(nicknames)):
        nota = 0
        nota += int(eva1[n])
        nota += int(eva2[n])
        lista.append((nicknames[n],nota))
    return lista

def calcularProm(lista):
    cant_tot = 0
    for n in range(len(lista)):
        cant_tot += lista[n][1]
    prom=0
    if (len(lista) != 0):
        prom = (cant_tot / len(lista))
    else:
        print("Esta vacia tun lista buen senior")
    return prom

def calcularBajoPromedio(lista,prom):
    alumnos_bajoprom = []
    for n in range(len(lista)):
        if (lista[n][1] < prom):
            alumnos_bajoprom.append(lista[n][0])
    return alumnos_bajoprom



lista_estructura = CrearEstrucutra()


print(
    f'El promedio de las notas es: {("{0:.2f}".format(calcularProm(lista_estructura)))}\nLos alumnos que quedaron por debajo del promedio son: {calcularBajoPromedio(lista_estructura,calcularProm(lista_estructura))}')




    