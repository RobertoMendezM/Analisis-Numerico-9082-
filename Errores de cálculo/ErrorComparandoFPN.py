# -*- coding: utf-8 -*-
"""
Curso: Análisis Numérico  2023-2


Forma correcta e incorrecta de comparar números de punto flotante

Libro: Adaptado de Liang, Introduction to Java Programming and Data Structures
 *          pág. 87

Created on 14 Feb 2023 

@author: Roberto Méndez Méndez
"""

class ErrorComparandoFPN:
    global EPSILONM 
    EPSILONM = 10**(-14)
    
    # Calculo Incorrecto
    def formaIncorrecta():
        x = 1.0 - 0.1 - 0.1 - 0.1 - 0.1 - 0.1
        print("Es x == 0.5 ", x == 0.5)    
        
    # Calculo Correcto    
    def formaCorrecta():
        x = 1.0 - 0.1 - 0.1 - 0.1 - 0.1 - 0.1
        if abs(x - 0.5) < EPSILONM:
            print(str(x) + " es aproximadamente 0.5" )        
    
   
    print("Hago la cuenta ")
    print("\t x = 1.0 - 0.1 - 0.1 - 0.1 - 0.1 - 0.1")
    print("Usando la forma clásica, comparo x == 0.5")
    formaIncorrecta()
    print("Usando la forma numérica")
    formaCorrecta()
    
    