import math
'''
De quantas formas é possível dividir 20 pessoas:
(a) em dois grupos de 10.
(b) em quatro grupos de 5.
(c) em três grupos de 6 e um de 2.
'''
def Q18():
    a =  math.factorial(20) / (math.factorial(10) * math.factorial(10))
    b =  (math.factorial(20) / (math.factorial(5) * math.factorial(15))) * (math.factorial(15) / (math.factorial(5) * math.factorial(10))) * (math.factorial(10) / (math.factorial(5) * math.factorial(5)))
    c =  (math.factorial(20) / (math.factorial(6) * math.factorial(14))) * (math.factorial(14) / (math.factorial(6) * math.factorial(8))) * (math.factorial(8) / (math.factorial(6) * math.factorial(2)))

    print(a)
    print(b)
    print(c)

if __name__ == "__main__":
    Q18()
