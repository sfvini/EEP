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
    prodA = 0.50
    prodB = 0.30
    prodC = 0.20
  
    # Porcentagem de defeito
    defA = 0.03
    defB = 0.04
    defC = 0.05
    
    probDef = defA * prodA + defB * prodB + defC * prodC
    probDefC = (defC * prodC) / probDef

    print(probDef)
    print(probDefC)

if __name__ == "__main__":
    Q199()
