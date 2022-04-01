import re
text = """"NumPy is the fundamental package for scientific computing with Python.

Website: https://www.numpy.org
Documentation: https://numpy.org/doc
Mailing list: https://mail.python.org/mailman/listinfo/numpy-discussion
Source code: https://github.com/numpy/numpy
Contributing: https://www.numpy.org/devdocs/dev/index.html
Bug reports: https://github.com/numpy/numpy/issues
Report a security vulnerability: https://tidelift.com/docs/security
It provides:

a powerful N-dimensional array object
sophisticated (broadcasting) functions
tools for integrating C/C++ and Fortran code
useful linear algebra, Fourier transform, and random number capabilities"""


# forma mas prolija, sacada de stackoverflow, la cual con la funcion findall
# que devuelve una lista con todos los segmentos del string que se asemejen a un http/https con cadena de caracteres detras
urls = re.findall(
    'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
for i in range(len(urls)):
    print(f'Url: {urls[i]}')


print(text)
print('*****************')
print(text.split())
# forma casera
listado = text.split("https")
for i in range(len(listado)):
    if listado[i][0] == ':':  # como el https sigue de :, al separar los string por https, siginifica que en cada string que la pos 0 sea : es un link
        j = 0
        lista = []  # recorro el string hasta encontrarme el salto de linea /n y voy agregando las letras del link a lista
        while listado[i][j] != '\n':
            lista.append(listado[i][j])
            j = j + 1
        # todos los char de lista los junto con un join y dsp imprimo el https con el link
        aux = ''.join(lista)
        print(f'Url: https{aux}')