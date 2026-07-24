import random as r
'''
Um jogo de computador requer que um jogador encontre um refúgio seguro num local onde os
seus inimigos não conseguem entrar. Quatro portas aparecem à sua frente, sendo que ele deve
escolher uma para entrar. A seguir, o jogador deve fazer uma segunda escolha entre dois, qua-
tro, um ou cinco buracos para descer, dependendo, respectivamente, da porta que ela atrav-
essa. Em cada caso, um buraco leva ao porto seguro. O jogador é pressionado em tomar uma decisão
e em sua pressa faz escolhas aleatórias. Qual é a probabilidade de ela chegar em segurança ao refúgio?
'''
def Q17():
	Iteracoes = int(1e5)
	Sucessos = 0
	Buracos = [2,4,1,5]
	Refugio = [1,2,1,5]
	for i in range(Iteracoes):
		porta = r.randint(0,3)
		buraco = r.randint(1, Buracos[porta])
		if buraco == Refugio[porta]
			Sucessos += 1
		
if __name__ == "main":
	Q17()
	pass
