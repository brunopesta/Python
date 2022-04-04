"""4. Para la aceptación de un artículo en un congreso se definen las siguientes especificaciones que
deben cumplir y recomendaciones de escritura:
• título: 10 palabras como máximo
• cada oración del resumen:
– hasta 12 palabras: fácil de leer
– entre 13-17 palabras: aceptable para leer
– entre 18-25 palabras: difícil de leer
– mas de 25 palabras: muy difícil
Dado un artículo en formato string, defina si cumple las especificaciones del título y cuántas ora-
ciones tiene de cada categoría. El formato estándar en que recibe el string tiene la siguiente forma:"""

evaluar = """ título:  Experiences in Developing a Distributed Agent-based Modeling Toolkit
with Python
resumen: Distributed agent-based modeling (ABM) on high-performance computing resources
provides the promise of capturing unprecedented details of large-scale complex systems.
However, the specialized knowledge required for developing such ABMs creates barriers to
wider adoption and utilization. Here we present our experiences in developing an initial
implementation of Repast4Py, a Python-based distributed ABM toolkit. We build on our
experiences in developing ABM toolkits, including Repast for High Performance Computing
(Repast HPC), to identify the key elements of a useful distributed ABM toolkit. We leverage
the Numba, NumPy, and PyTorch packages and the Python C-API to create a scalable modeling
system that can exploit the largest HPC resources and emerging computing architectures.
"""

listado = evaluar.lower().split('resumen:')
titulo= listado[0]
resumen=listado[1]

def evaluarTitulo(titulo):
    titulo = titulo.split()
    titulo.remove(titulo[0]) #Removemos la palabra "TITULO" del titulo asi despues podemos comprara con el if la longitud del titulo
    if len(titulo) <= 10:
        print("ok")
    else:
        print("not ok")
    
evaluarTitulo(titulo)


def evaluarResumen(resumen):
    lista_frases= resumen.split('.')
    contador= {'facil':0, 'aceptable':0,'dificil':0, 'muy dificil':0}
    for i in range(len(lista_frases)):
        oracion = len(lista_frases[i].split())

        match oracion: #Vemos y actualizamos el contador a lo largo q recorremos la oracion
            
            case a if oracion <= 12:
                contador['facil'] += 1
            case b if 13 <= oracion <= 17:
                contador['aceptable'] += 1
            case c if 18 <= oracion <= 25:
                contador['dificil'] += 1
            case d if 25 < oracion:
                contador['muy dificil'] += 1
    return print('faciles: ', contador['facil'], 'aceptalbes: ', contador['aceptable'], 'dificil', contador['dificil'], 'Muy dificil', contador['muy dificil'])

evaluarResumen(resumen)