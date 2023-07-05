import novo_carro
import semaforo
import time
import calc_media
import fuzzy_system as fz

def simula(duracao):
    #var int pra controlar o tempo gasto dentro do sinal
    carros = []
    #array para controlar o tempo médio gasto de cada carro, ao sair o tempo decorrido é movido para esse array
    control_tempo = []
    #var int simular o temporizador
    tempo = 0
    #sinal aberto = True fechado = False
    #o estado inicial sempre é o contrário dessa variável para os simples
    estado = False
    #variavel pra servir de controle das coisas
    control_var = 0
    
    #duração da simulação
    while tempo <= duracao*5:

        #controla o semáforo baseado num temporizador simples
        estado = semaforo.controlador_simples(tempo, estado, duracao)

        #adiciona 1 "segundo" a cada carro "por segundo" decorrido
        control_var = 0
        while control_var < len(carros):
            carros[control_var] = carros[control_var] + 1
            control_var = control_var + 1

        #entrada de novos carros
        carros = novo_carro.entrada_aleatoria(carros,tempo)

        #cotrola a saida
        if estado == True and len(carros) > 0:
            control_tempo.append(carros[0])
            carros.pop(0)
        
        #ajuda testar
        print("Tempo:",tempo)
        print(carros)
        print(control_tempo)
        print("\n\n")
        

        #aumenta o tempo e impede de criar loop infinito
        tempo = tempo+1

        #deixa a simulação temporizada cada loop ocorre com intervalos de 1 segundo
        #time.sleep(1)
    
    #ajuda testar
    print(carros)
    print(control_tempo)
    calc_media.calc_simples(carros,control_tempo, duracao)



def simula_fuzzy(duracao):
    #var int pra controlar o tempo gasto dentro do sinal
    carros = []
    #array para controlar o tempo médio gasto de cada carro, ao sair o tempo decorrido é movido para esse array
    control_tempo = []
    #var int simular o temporizador
    tempo = 0
    #sinal aberto = True fechado = False
    #o estado inicial sempre é o contrário dessa variável para os simples
    estado = False
    #variavel pra servir de controle das coisas
    control_var = 0
    #variavel para criar um tempo minimo de funcionamente do sinal no fuzzy system
    tempo_troca_de_estado =0
    controle_estado = False
    
    #duração da simulação
    while tempo <= duracao*5:

        #checa o tempo do carro parado a mais tempo, caso nao tenha nenhum = 0
        if len(carros) == 0:
            tempo_carro = 0
        else:
            tempo_carro = carros[0]
        
        #controlador fuzzy
        estado = fz.controlador_fuzzy(len(carros),tempo_carro,tempo_troca_de_estado, estado)

        #checagem se trocou de estado
        if controle_estado != estado:
            tempo_troca_de_estado = 0
            controle_estado = estado
            if estado == True:
                print("Abrindo")
            else:
                print("Fechando")

        #adiciona 1 "segundo" a cada carro "por segundo" decorrido
        control_var = 0
        while control_var < len(carros):
            carros[control_var] = carros[control_var] + 1
            control_var = control_var + 1

        #entrada de novos carros
        carros = novo_carro.entrada_aleatoria(carros,tempo)

        #cotrola a saida
        if estado == True and len(carros) > 0:
            control_tempo.append(carros[0])
            carros.pop(0)
        
        #ajuda testar
        print("Tempo:",tempo)
        print(carros)
        print(control_tempo)
        print("\n\n")
        

        #aumenta o tempo e impede de criar loop infinito
        tempo = tempo+1
        tempo_troca_de_estado = tempo_troca_de_estado + 1

        #deixa a simulação temporizada cada loop ocorre com intervalos de 1 segundo
        #time.sleep(1)
    
    #ajuda testar
    print(carros)
    print(control_tempo)
    calc_media.calc_fuzzy(carros,control_tempo)