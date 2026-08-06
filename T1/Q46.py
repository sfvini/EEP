import math
'''
Quantos planos são determinados por quatro pontos distintos e não coplanares?
'''

def Q46():
    res = math.factorial(4) / (math.factorial(3) * math.factorial(1))
    print(res)

if __name__ == "__main__":
  Q46()
