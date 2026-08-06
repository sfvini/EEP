import random as r

'''
Suponha que uma moeda justa seja lançada duas vezes. Seja A o evento que uma cara ocorre no
primeiro lance, e B o evento que uma cara ocorra no segundo lance. São eventos independentes A
e B?
'''
def Q46():
  Iteracoes = int(1e6)

  A = 0 
  B = 0  
  A_e_B = 0  

  for i in range(Iteracoes):
    lance1 = r.randint(0, 1)
    lance2 = r.randint(0, 1)

    if lance1 == 1:
      A = A + 1

    if lance2 == 1:
      B = B + 1

    if lance1 == 1 and lance2 == 1:
      A_e_B = A_e_B + 1

  prob_A = A / Iteracoes
  prob_B = B / Iteracoes
  prob_A_e_B = A_e_B / Iteracoes

  if abs(prob_A_e_B - (prob_A * prob_B)) < 0.005:
    print("Sim")
  else:
    print("Não")


if __name__ == "__main__":
  Q46()
