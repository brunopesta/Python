nota = int(input(" Ingresa una nota (-1 para finalizar"))
lista_de_notas = []
while nota != -1:
    lista_de_notas.append(nota)
    nota = int(input(" Ingresa una nota (-1 para finalizar"))

cant = len(lista_de_notas)
suma = 0

for indice in range(cant):
    suma += lista_de_notas[indice]
    print(suma)
if len(lista_de_notas) != 0:
    print("El promedio es", (suma / len(lista_de_notas)))
else:
    print("El promedio es 0")
