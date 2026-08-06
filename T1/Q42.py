import random as r

'''
Um jogo de computador requer que um jogador encontre abrigo seguro em um local onde seus inimigos não podem entrar. Quatro portas aparecem para o jogador,
a partir do qual ele deve escolher entre uma e apenas uma. O jogador deve então fazer uma segunda escolha entre dois, quatro, um ou cinco buracos para descer, 
respectivamente, dependendo de qual porta ela atravessa. Em cada caso, apenas um buraco leva ao refúgio seguro. O jogador é apressado em tomar uma
decisão e em sua pressa faz escolhas aleatoriamente. Qual é a probabilidade de ter chegando com segurança ao refúgio?
'''
def Q42():
  Iteracoes = int(1e6)
  Sucessos = 0

  for i in range(Iteracoes):
    porta = r.randint(1, 4)

    if porta == 1:
      buracos = 2
    elif porta == 2:
      buracos = 4
    elif porta == 3:
      buracos = 1
    else:
      buracos = 5

    if r.randint(1, buracos) == 1:
      Sucessos = Sucessos + 1

  print(Sucessos / Iteracoes)

if __name__ == '__main__':
  Q42()
