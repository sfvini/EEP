import math
'''
Numa fábrica com 10 trabalhadores, um grupo de 4 será selecionado para uma excursão, 
que será sorteada pela empresa. De quantas maneiras o grupo poderá ser formado se 
dois dos dez são casados e só irão juntos?
'''

def Q42():
    # Sem casal
    res1 = math.factorial(8) / (math.factorial(4) * math.factorial(4))
    print(res1)
                               
    # Com casal
    res2 = math.factorial(8) / (math.factorial(2) * math.factorial(6))
    print(res2)

# PERGUNTAR (precisa somar)

if __name__ == '__main__':
    Q42()
