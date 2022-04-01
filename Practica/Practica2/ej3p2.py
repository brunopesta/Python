from cgi import test


text = "Julian jugaba a la pelota muy mal entonces le pegaron pero eso no uqiere decir que nosotrs tengamos que ser tan malos para llegar a seguir pegandole"

def leerCaracter():
    while True:
        letra = input('Ingrese una letra')
        if letra.isalpha() and 1 == len(letra):
            return letra
        else:
            print('No se ingreso una letra')

letra = leerCaracter()
palabras = []

# Manjeo de String para que no tenga puntos y comas + pasarlo a minusculas y separarlo en una lista
text = text.replace(".", '') # remplazamos los puntos por espacios
text = text.replace(",", '') #remplazamos las comas por espacios
text = text.lower().split() #Lo hacemos con minusculas todo el texto

for i in range(len(text)):
    if text[i][0].startswith(letra):
        if text[i] not in palabras:
            palabras.append(text[i])
print(palabras)
print(type(text))