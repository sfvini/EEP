import math

'''
Um paciente foi indicado por um urologista para realizar um exame de toque retal, com o intuito
de verificar uma inflamação em sua próstata, que pode ser resultado de um sarcoma. Sarcoma é
uma forma de câncer que acomete 1% dos pacientes que apresentam este tipo de inflamação, e requer 
uma investigação mais profunda sobre o quadro clínico do paciente. O laudo do exame de toque, feito 
por especialista experiente, indicou positivamente o desenvolvimento de sarcoma.

Considere os eventos:
D: o paciente é acometido da doença.
C: o paciente é diagnosticado corretamente para a doençaa a partir do exame de toque.

Um médico experiente faz o diagnóstico correto em 95% dos casos quando o sarcoma está realmente presente 
(valor chamado sensibilidade do teste) e em 98% dos casos quando a doença não se desenvolveu (valor chamado 
especificidade do teste). Determine a probabilidade de o paciente ter desenvolvido sarcoma, dado que houve um
resultado positivo do exame.
'''

def Q231():
    doenca = 0.01
    sem_doenca = 0.99

    positivo_doenca = 0.95
    positivo_sem_doenca = 0.02 # 100-98

# Resultado postivo do exame
    positivo = (positivo_doenca * doenca) + (positivo_sem_doenca * sem_doenca)

# Estar doente com o teste positivo
    res = (positivo_doenca * doenca) / positivo
    print(res)

if __name__ == "__main__":
    Q231()
