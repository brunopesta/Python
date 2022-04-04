frase = input("Ingrese una palabra/frase").lower()

frase = frase.split()


def prueba():
    cont=0
    dop = []
    heterograma = True
    for n in range(len(frase)):
        for j in range(len(frase[n])):
            if frase[n][j] not in dop:
                dop.append(frase[n][j])
            else:
                heterograma = False
    if heterograma:
        print(" es un heterograma")
    else:
        print(' No es un heterograma')

prueba()
