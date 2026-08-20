import random

'''
Um paciente foi indicado por um urologista para realizar um exame de toque retal, com o intuito
de verificar uma inflamação em sua próstata, que pode ser resultado de um sarcoma. Sarcoma é
uma forma de câncer que acomete 1% dos pacientes que apresentam este tipo de inflamação, e requer 
uma investigação mais profunda sobre o quadro clínico do paciente. O laudo do exame de toque, feito 
por especialista experiente, indicou positivamente o desenvolvimento de sarcoma.

Considere os eventos:
D: o paciente é acometido da doença.
C: o paciente é diagnosticado corretamente para a doença a partir do exame de toque.

Um médico experiente faz o diagnóstico correto em 95% dos casos quando o sarcoma está realmente presente 
(valor chamado sensibilidade do teste) e em 98% dos casos quando a doença não se desenvolveu (valor chamado 
especificidade do teste). Determine a probabilidade de o paciente ter desenvolvido sarcoma, dado que houve um
resultado positivo do exame.
'''

def Q231():
    looping = 10000000  
    p_doenca = 0.01

    positivo_com_doenca = 0.95
    positivo_sem_doenca = 0.02  # 1.0 - 0.98

    total_positivos = 0
    doentes_positivos = 0

    for _ in range(looping):
        
        # Verificar se o paciente tem doença
        tem_doenca = 0 
        if random.random() < p_doenca:
             tem_doenca = 1

        # Probabilidade de exame positivo
        positivo = 0
        if tem_doenca == 1:
            positivo = positivo_com_doenca
        else: 
            positivo = positivo_sem_doenca

        # Faz o exame e conta os exames positivos e os casos que tem doença com exame positivo     
        if random.random() < positivo:
            total_positivos += 1
            if tem_doenca == 1:
                doentes_positivos += 1
    
    print(doentes_positivos / total_positivos)

if __name__ == "__main__":
    Q231()
