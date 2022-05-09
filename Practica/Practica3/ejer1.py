""".1 Ejercicios
1. Encontrar qué tipo de shows tiene un país determinado.
1
• Realizar una función que informe todos los países que existen.
• Realizar una función que dado un país informe si es parte de la línea del show pasado como
argumento. Nota: utilice las funciones vistas de lambda(utilizando la función definida), map
para informar los tipos de shows (valores únicos) en que participa un país.
Analizar:
• ¿En qué número de columna está el país?
• Como en algunos casos hay varios países en un show debemos separarlos y quedarnos con
valores únicos.
2. Informe la lista de países del archivo en orden alfabéticamente creciente.
3. Informe los shows de un año determinado, realice una función que reciba un año y la línea
como argumentos."""

import csv
import os




ruta_completa = os.getcwd()
ruta_archivos_csv = os.path.join(ruta_completa,'netflix_titles.csv')


def leer_archivo():
    with open(ruta_archivos_csv,encoding= 'utf-8') as archivo:
        data_net = csv.reader(archivo,delimiter=',')
        header = next(data_net)
        datos = list(data_net)
    return datos

def filtrar(lista):
    '''Recibe una lista, la limpia, saca vacios y saca espacios al principio/final'''
    lista = list(map(lambda x: x.split(','), lista))
    aux = []
    for listado in lista:
        for l in listado:
            aux.append(l.strip())
    return list(filter(bool, set(aux)))

def informar_paises(lista):
    "Retorna una lista con todos los paises que aparecen en el archivo csv"
    return filtrar(list(map(lambda x: x[5], lista)))

def informar_show_type(pais,lista):
    paises = informar_paises(lista)

    if pais in paises:
        generos = list(filter(bool,set(map(lambda linea: linea[10] if pais in linea[5] else False, lista)))) #Utiliziamos un filter para filtrar todos los booleanos que haya ern esa lista
        """ el set, nos limpia de espacios en blanco en toda esa lista, despues utilizamos un map con un lambda iterador, y vamos preguntando si el pais que nos entea
        por parametro esta en esa linea del tv show, si es verdadero se nos va a guardar en nuestra lista el TV show, sino se pone en False
        Pero nos acordamos que vamos filtrado el false con el filter
        """
        return filtrar(generos)
    else:
        return False

def buscar_pais_show(pais,show,lista):
    """Informar si el pais pasado contiene el show pasado o no, en caso de que el pais pasado no este en la lista de paises del data_Set devuelve False"""
    nac = informar_paises(lista)
    if pais in nac:
        data= list((map(lambda x: True if (show == x[2] and pais in list(x[5].split(',')))else False , lista)))
        if True in data:
            return 'Contiene'
        else:
            return 'No contiene'
    else:
        return False


def ordenar(lista):
    paises = informar_paises(lista)
    paises.sort()
    return paises

def buscar_por_año(año,lista):
    aux = list(filter(bool,set(map(lambda x: x[2] if x[7] == año else False, lista))))
    return aux


def main():
    datos =leer_archivo()
    print(informar_paises(datos))
    print(informar_show_type('Argentina',datos))
    print(buscar_pais_show('Argentina','Casados Con Hijos',datos))
    print(ordenar(datos))
    print(buscar_por_año('1990',datos))

if __name__ == '__main__':
    main()
