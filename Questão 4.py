# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 09:43:43 2021

@author: bruno
"""

#Universidade Federal Rural de Pernambuco
#Bruno da Silva Ramos
#Questão 4 - Parte B (2. VA - Computação Aplicada ao Ensino da Física)
##############################################################################

#Importando as Bibliotecas!

import matplotlib.pyplot as plt

#Definindo Condições Iniciais

r = 0.05
c = 0.1
b = 0.1
m = 0.01
h = 0.1
t = 0
n = 0.3
p = 0.7
tempo, ny, py = [], [], []

#Loop

while t<=2000:
    tempo.append(t)
    ny.append(n)
    py.append(p)
    
    #Para o N(t)
    
    kn1 = r*n - c*n*p
    kn2 = r*(n+(h*kn1)/2) - c*(n+(h*kn1)/2)*p
    kn3 = r*(n+(h*kn2)/2) - c*(n+(h*kn2)/2)*p
    kn4 = r*(n+h*kn3) - c*(n+h*kn3)*p
    
    #Para o P(t)
    
    kp1 = b*n*p - m*p
    kp2 = b*n*(p+(h+kp1)/2) - m*(p+(h*kp1)/2)
    kp3 = b*n*(p+(h+kp2)/2) - m*(p+(h*kp2)/2)
    kp4 = b*n*(p+h*kp3) - m*(p+h*kp3)
    
    #Incrementando as Variaveis
    
    n = n + (h/6)*(kn1+2*kn2+2*kn3+kn4)
    p = p + (h/6)*(kp1+2*kp2+2*kp3+kp4)
    t = t + h

#Plotando os Gráficos

plt.plot(tempo, ny, "g--", tempo, py, "b--")
plt.ylabel("P(t) azul -- N(t) verde")
plt.xlabel("Tempo")
plt.show()

print('São possiveis ver 7 gerações de presas e predatores!')

plt.plot (ny, py)
plt.xlabel("N(t)")
plt.ylabel("P(t)")
plt.show()