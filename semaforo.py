#controlar simples pode modificar o tempo pelo divisor
def controlador_simples(tempo, estado, duracao):
    #se divisivel pelo tempo determinado, muda o sinal
    if (tempo % duracao) == 0:
        if not estado:
            return True
        elif estado:
            return False
        
    #precisa desse return c não sempre retorna falso fora do if
    return estado