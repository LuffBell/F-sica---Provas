# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 22:09:45 2021

@author: bruno
"""

#Universidade Federal Rural de Pernambuco
#Bruno da Silva Ramos
#Questão 3 - Parte B (2. VA - Computação Aplicada ao Ensino da Física)
##############################################################################

#Importando as Bibliotecas!

import matplotlib.pyplot as plt

#Difinindo Condições Iniciais

a = 0.3
g = 9.8
v = 0
t = 0
h = 0.01
tempo, eixoy = [], []

#loop

while t<=30:
    tempo.append(t)
    eixoy.append(v)
    
    k1 = g - a*v
    k2 = g - a*(v+h*k1)
    
    v = v + (h/2)*(k1+k2)
    t = t + h

#Plotando o Gráfico

plt.plot(tempo, eixoy)
plt.xlabel('Tempo (t)')
plt.ylabel('V(t)')
plt.show()

#Procurando a velocidade terminal

vt = eixoy[len(eixoy)-1]
print("A velocidade terminal é de: {:.2f} m/s".format(vt))

vt = int(vt*100)  #Só para deixar mais fácil de procurar o tempo!

#Procurando em qual instante de tempo foi alcançado essa velocidade

for n in range(len(eixoy)):
    if (int(eixoy[n]*100)==vt):
        tempofinal = tempo[n]
        break
   
print("O tempo estimado para se atingir a velocidade terminal é de: {:.2f}s".format(tempofinal))