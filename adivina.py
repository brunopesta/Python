import random
num_aleatorio = random.randrange(101)
gane = False
print("Tenés 5 intentos para adivinar un entre 0 y 100")
intento = 1
while (intento <= 5 
       and not gane):
    num_Ingresado = int(input('Ingresa tu número: '))
    if num_Ingresado == num_aleatorio:
        print(' ganaste y lo hiciste en  {} intentos!!!'.format(intento))
        gane = True
    else:
        print('le pifiaste, Seguí intentando.')
        intento += 1
if not gane:
    print('\n perdiste :(\n El número era: {}'.format(num_aleatorio))