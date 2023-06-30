#controlar simples pode modificar o tempo pelo divisor
def controlador_simples(tempo,estado):
    #se divisivel pelo tempo determinado, muda o sinal
    if (tempo % 15) == 0:
        if estado == False:
            print("Abrindo")
            return True
        elif estado == True:
            print("Fechando")
            return False
        
    #precisa desse return c não sempre retorna falso fora do if
    return estado