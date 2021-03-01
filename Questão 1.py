# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 19:00:47 2021

@author: bruno
"""

#Universidade Federal Rural de Pernambuco
#Bruno da Silva Ramos
#Questão 1 - Parte B (2. VA - Computação Aplicada ao Ensino da Física)
##############################################################################

#Importando as Bibliotecas!

import matplotlib.pyplot as plt

#Definindo Condições Iniciais

l = 0.01
h = 0.01
c = 0.001
t = 0
y = 1

tempo, eixoy = [], []

#Definindo o Loop

while t <= 10:
    tempo.append(t)
    eixoy.append(y)
    
    #Incrementando as 
    
    y = y + h*(-y*l - 2*c*t)
    t = t + h
        
#Criando o Gráfico

plt.plot(tempo, eixoy)
plt.xlabel("Tempo")
plt.ylabel("N(T)/N0")
plt.show()

#Letra B.

for n in range(len(eixoy)):
    f = eixoy[n]
    f = int(f*(100))
    if(f==85):
        index = n
        
#Achando o Tempo Correspondente.

print("O tempo t' é de: {:.2f} s".format(tempo[index]))