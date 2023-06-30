import novo_carro
import semaforo
import time
import calc_media

def simula():
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
    while tempo <= 60:

        #controla o semáforo baseado num temporizador simples
        estado = semaforo.controlador_simples(tempo,estado)

        #adiciona 1 "segundo" a cada carro "por segundo" decorrido
        control_var = 0
        while control_var < len(carros):
            carros[control_var] = carros[control_var] + 1
            control_var = control_var + 1

        #entrada de novos carros
        carros = novo_carro.entrada_2_em_2(carros,tempo)

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
    calc_media.calc(carros,control_tempo)