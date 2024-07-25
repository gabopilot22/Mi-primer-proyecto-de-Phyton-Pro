import random

lista="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

pregunta=int(input("introduce el numero de digitos para tu contraseña que sea mayor a 5 y menor a 25"))

almacenar=""

for i in range(pregunta):
    if pregunta>=5 and pregunta<=25:
        gen=random.choice(lista)

        almacenar+=gen

    else:
        break

print (almacenar)
