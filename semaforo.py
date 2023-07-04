#controlar simples pode modificar o tempo pelo divisor
def controlador_simples(tempo, estado, duracao):
    #se divisivel pelo tempo determinado, muda o sinal
    if (tempo % duracao) == 0:
        if estado == False:
            print("Abrindo")
            return True
        elif estado == True:
            print("Fechando")
            return False
        
    #precisa desse return c não sempre retorna falso fora do if
    return estado