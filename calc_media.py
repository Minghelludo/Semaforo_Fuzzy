def calc_simples(tempos1,tempos2, duracao):
    total = 0

    controle = 0
    while controle < len(tempos1):
        total = total + tempos1[controle]
        controle = controle+1

    controle = 0
    while controle < len(tempos2):
        total = total + tempos2[controle]
        controle = controle + 1
    
    quantidade = len(tempos1) + len(tempos2)
    media = total / quantidade
    return media

def calc_fuzzy(tempos1,tempos2):
    total = 0

    controle = 0
    while controle < len(tempos1):
        total = total + tempos1[controle]
        controle = controle+1

    controle = 0
    while controle < len(tempos2):
        total = total + tempos2[controle]
        controle = controle + 1
    
    quantidade = len(tempos1) + len(tempos2)
    media = total / quantidade
    return media