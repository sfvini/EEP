import math
'''
Três máquinas A, B e C produzem 50%, 30% e 20%, respectivamente,
do total de peças de uma fábrica. As porcentagens de produção defeituosa
destas máquinas são 3%, 4% e 5%. Se uma peça é selecionada aleatoriamente,
ache a probabilidade de ela ser defeituosa. Se a peça selecionada é defeituosa,
encontre a probabilidade de ter sido produzida pela máquina C.
'''
def Q199():
    # Porcentagem de produção
    pA = 0.50
    pB = 0.30
    pC = 0.20
  
    # Porcentagem de defeito
    dA = 0.03
    dB = 0.04
    dC = 0.05

    pD = dA * pA + dB * pB + dC * pC
    pDC = (dC * pC) / pD

    print(pD)
    print(pDC)

if __name__ == "__main__":
    Q199()
