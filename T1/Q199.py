import random

'''
Três máquinas A, B e C produzem 50%, 30% e 20%, respectivamente,
do total de peças de uma fábrica. As porcentagens de produção defeituosa
destas máquinas são 3%, 4% e 5%. Se uma peça é selecionada aleatoriamente,
ache a probabilidade de ela ser defeituosa. Se a peça selecionada é defeituosa,
encontre a probabilidade de ter sido produzida pela máquina C.
'''

def Q199():
    looping = 1000000
    defeito = 0
    defeitoemc = 0

    for _ in range(looping):
        # sorteia a maquina
        maquina = random.randint(1, 100)
        
        if maquina <= 50:
            if random.randint(1, 100) <= 3:  
                defeito += 1

        elif maquina <= 80:
            if random.randint(1, 100) <= 4:  
                defeito += 1

        else:
            if random.randint(1, 100) <= 5:
                defeito += 1
                defeitoemc += 1

    print(defeito / looping)
    print(defeitoemc / defeito)

if __name__ == "__main__":
    Q199()
