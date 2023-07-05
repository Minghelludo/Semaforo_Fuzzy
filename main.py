import simul
#simulação sinal simples
i = 0
media_30_seg = 0
media_fuzzy = 0
while i<100:
    media_30_seg += float(simul.simula(30))/100
    i+= 1
#simulação sinal fuzzy
i=0
while i<100:
    media_fuzzy += float(simul.simula_fuzzy(30))/100
    i+=1


print(f'Media para um semáforo de 30 segundos {media_30_seg}')
print(f'Media para um semáforo fuzzy {media_fuzzy}')