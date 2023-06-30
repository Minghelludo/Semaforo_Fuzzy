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

#é possivel fazer uma entrada randomizada