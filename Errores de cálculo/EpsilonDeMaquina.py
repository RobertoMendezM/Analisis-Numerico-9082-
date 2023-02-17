# -*- coding: utf-8 -*-
"""
Programa que calcula el epsilon de máquina

Libro: Einar Smith, Introduction to the Tools
 *          of Scientific Computing
 *          pág. 29

Created on Wed Mar 23 05:50:20 2022
update: Thu Apr 7

@author: Roberto Méndez Méndez
"""

class EpsilonDeMaquina:
    
    # Calculo correcto
    def epsilonMaquina():
        eps, i = 1.0 , 0
        while 1 + eps > 1:
            eps /= 2
            i += 1
        epsMachine = eps*2    
        print("El epsilon de máquina es: ", epsMachine)
        print("La potencia es: ", i)    
        
    # Calculo incorrecto    
    def epsilonMaquinaSad():
        eps, i = 1.0 , 0
        while eps > 0:
            eps /= 2
            i += 1
        print("El epsilon de máquina es: ", eps*2)
        print("La potencia es: ", i)        
    
    epsilonMaquina()
    
    print("Ahora utilicemos el método epsilonMaquinaSad()")
    epsilonMaquinaSad()
    print("¿Por qué el resultado fue tan diferente?")