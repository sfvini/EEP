import math
'''
Quantos planos são determinados por quatro pontos distintos e não coplanares?
'''

def Q46():

'''
EXPLICAÇÃO DA IA
​Como o enunciado afirma que temos 4 pontos "não coplanares" (ou seja, eles não estão todos achatados no mesmo plano; formam uma figura 3D, como as pontas de uma pirâmide de base triangular chamada tetraedro), qualquer trio de pontos que você escolher formará um plano garantido.
'''

    res = math.factorial(4) / (math.factorial(3) * math.factorial(1))
    print(res)

if __name__ == "__main__":
  Q46()
