import random as r
'''
Uma fábrica tem três máquinas que fixam parafusos. O percentual de operações feitas por cada
máquina em relação ao total é de 10%, 35% e 55%, respectivamente. Além disso, sabe-se que 5%, 
3% e 1% das operações das respectivas três máquinas apresentam defeito. Qual é a probabilidade 
de que um parafuso selecionado aleatoriamente no final das execuções de produção do dia estar com falha?
'''
def Q18():
    Iteracoes = int(1e6)
    Sucessos = 0
    
    for _ in range(Iteracoes):
        maquina = r.random()
        
        if maquina < 0.10:
            if r.random() < 0.05:
                Sucessos += 1
        elif maquina < 0.45: 
            if r.random() < 0.03:
                Sucessos += 1
        else:
            if r.random() < 0.01:
                Sucessos += 1
			
	print(Sucessos / Iteracoes)
		
if __name__ == "__main__":
	Q18()
	pass
