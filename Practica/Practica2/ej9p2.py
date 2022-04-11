estructura = [
'-*-*-',
'--*--',
'----*',
'*----',
]

[
'1*3*1',
'12*32',
'1212*',
'*1011',
]

def crearMatriz(matriz):
    """Agarra la lista 'estructura' y convierte cada string dentro en otra lista para convertirla en una matriz y facilitar su recorrido"""
    for i in range(len(estructura)):
        matriz.append(list(estructura[i]))
    
def recorrerMatriz(matriz):
    for x in range(len(matriz)):
        for y in range(len(matriz)):
             # verifico que la pos a evualuar es una casilla libre d bomba
            if (matriz[x][y] == '-'):
                cont = 0
                #Hago un try al rededor de la pos a evaluar por si existe un index out of range
                try:
                    if matriz[x-1][y-1]=='*':
                        cont +=1
                    if matriz[x][y-1]=='*':
                        cont +=1
                    if matriz[x+1][y-1]=='*':
                        cont +=1
                    if matriz[x+1][y]=='*':
                        cont +=1
                    if matriz[x+1][y+1]=='*':
                        cont +=1
                    if matriz[x][y+1]=='*':
                        cont +=1
                    if matriz[x-1][y+1]=='*':
                        cont +=1
                    if matriz[x+1][y]=='*':
                        cont +=1
                except:
                    print(f'this position matriz[{x}][{y}] doesn`t exist( index out of range)')
                matriz[x][y] = cont
    for n in range(len(matriz)):
        matriz[n]=matriz[n]
        print(matriz[n])

matriz = []
crearMatriz(matriz)
recorrerMatriz(matriz)