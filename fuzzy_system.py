import simpful as sp

def controlador_fuzzy(n_carros, tempo_carro, tempo_sinal, estado):

    if tempo_sinal < 10:
        return estado

    FS = sp.FuzzySystem()

    S_1 = sp.FuzzySet(function = sp.Triangular_MF(a=0, b=0, c=4), term = "pouco")
    S_2 = sp.FuzzySet(function = sp.Triangular_MF(a=2, b=6, c=10), term = "normal")
    S_3 = sp.FuzzySet(function = sp.Triangular_MF(a=8, b =12, c=16), term = "muito")
    S_4 = sp.FuzzySet(function = sp.Triangular_MF(a=14, b =18, c=22), term = "demais")
    FS.add_linguistic_variable("quantidade", sp.LinguisticVariable([S_1, S_2, S_3, S_4], concept="quantidade de carros", universe_of_discourse=[0,22]))

    F_1 = sp.FuzzySet(function = sp.Triangular_MF(a=0, b=0, c=5), term = "baixo")
    F_2 = sp.FuzzySet(function = sp.Triangular_MF(a=5, b=10, c=15), term = "medio")
    F_3 = sp.FuzzySet(function = sp.Triangular_MF(a=10, b=15, c=20), term = "alto")
    FS.add_linguistic_variable("tempo", sp.LinguisticVariable([F_1, F_2, F_3], concept = "tempo de espera do primeiro carro", universe_of_discourse=[0,20]))

    T_1 = sp.FuzzySet(function = sp.Triangular_MF(a=0, b=2, c=4), term = "fechado")
    T_2 = sp.FuzzySet(function = sp.Triangular_MF(a=3, b=5, c=7), term = "igual")
    T_3 = sp.FuzzySet(function = sp.Triangular_MF(a=6, b=8, c=10), term = "aberto")
    FS.add_linguistic_variable("sinal", sp.LinguisticVariable([T_1, T_2, T_3], concept= "estado do sinal", universe_of_discourse=[0,10]))

    R1 = "IF (quantidade IS demais) OR (tempo IS alto) THEN (sinal IS aberto)"
    R2 = "IF (quantidade IS muito) AND (tempo IS medio) THEN (sinal IS aberto)"
    R3 = "IF (quantidade IS normal) AND (tempo IS medio) THEN (sinal IS igual)"
    R4 = "IF (quantidade IS pouco) OR (tempo IS baixo) THEN (sinal IS fechado)"
    FS.add_rules([R1, R2, R3, R4])

    FS.set_variable("quantidade",n_carros)
    FS.set_variable("tempo", tempo_carro)

    controlador = FS.Mamdani_inference()
    if controlador["sinal"] < 5:
        return False
    elif controlador["sinal"] >= 5:
        return True
