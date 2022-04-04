import string


frase = """Tres tristes tigres, tragaban trigo en un trigal, en tres tristes trastos, tragaban
trigo tres tristes tigres."""

frase = frase.lower().replace(',','').replace('.','').split()

palabra = input("Ingrese un String")

def cuantasVeces(palabra,frase):
    cont=0
    for i  in range(len(frase)):
        if frase[i] == palabra:
            cont += 1

    
    
    return print('frase: ',frase, 'Letra', palabra, 'Resultado: ',cont)


#cuantasVeces(palabra,frase)

print(frase.count(palabra)) # te pasas toda la funcion que hice por la chota


