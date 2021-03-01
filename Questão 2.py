# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 20:35:20 2021

@author: bruno
"""

#Universidade Federal Rural de Pernambuco
#Bruno da Silva Ramos
#Questão 2 - Parte B (2. VA - Computação Aplicada ao Ensino da Física)
##############################################################################

#Importando as Bibliotecas!

import matplotlib.pyplot as plt
import numpy as np

#Definindo as Condições Iniciais

h = 0.1
y = -1
t = 0

tempo, eixoy = [], []

#Loop

while t<=10:
    tempo.append(t)
    eixoy.append(y)
    
    k1 = -3*(y + 1) + 3*(2*np.cos(3*t) - 3*t)
    
    k2 = -3*((y+h*k1)+1) + 3*(2*np.cos(3*(t+h)) - 3*(t+h))
    
    y = y + (h/2)*(k1 + k2)
    t = t + h

    
#Plotando o Gráfico

plt.plot(tempo, eixoy)
plt.xlabel("Tempo")
plt.ylabel("y(t)")
plt.show()
                              
                        