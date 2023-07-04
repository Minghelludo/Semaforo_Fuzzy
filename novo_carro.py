import random
#entra um carro novo a cada 2 "segundos"
def entrada_2_em_2(carros,tempo):
    if (tempo % 2) == 0:
        carros.append(0)
    return carros

#entra um carro novo a cada 3 "segundos"
def entrada_3_em_3(carros,tempo):
    if (tempo % 3) == 0:
        carros.append(0)
    return carros

#entra um carro num intervalo aleatório entre 1 e 10 segundos
def entrada_aleatoria(carros,tempo):
    num_aleatorio = random.randint(1,10)
    if (tempo % num_aleatorio) == 0:
        carros.append(0)
    return carros
