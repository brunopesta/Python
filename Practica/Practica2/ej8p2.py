valores = [('aeioulnrst', 1),
           ('dg', 2),
           ('bcmp', 3),
           ('f,h,v,w,y', 4),
           ('k', 5),
           ('jx',8),
           ('qz',10)]

palabra = input('Ingrese una palabra')
contador =0


for i in range(len(palabra)):
    for j in range(len(valores)):
        if palabra[i] in valores[j][0]:
            contador += valores[j][1]

print(f'Puntaje de la palabra: {contador}')
