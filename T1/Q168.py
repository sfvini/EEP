import math
'''
De uma anlise de 100 empresas de exportação que trabalham com o continente africano,
chegou-se à conclusão de que os países de língua portuguesa são os principais clientes. Com
efeito, das empresas analisadas, 40 exportam para Angola, 50 para Moçambique e 25 exportam para 
ambos os países. Selecionando ao acaso uma empresa, qual a probabilidade de ela exportar para:
a.) Pelo menos um dos países.
b.) Nenhum dos países.
c.) Angola, mas não para Moçambique.
d.) Angola, sabendo que não exporta para Moçambique
'''
def Q42():
    ambos = 25
    mocambique = 25
    angola = 15
  
    # a)
    a = (ambos + mocambique + angola) / 100
    print(a)
                               
    # b)
    b = (100 - (ambos + mocambique + angola)) / 100
    print(b)
  
    # c)
    c = angola / 100
    print(c)
                           
    # d)
    d = angola / (100 - mocambique - ambos)
    print(d)
  
if __name__ == '__main__':
    Q42()
