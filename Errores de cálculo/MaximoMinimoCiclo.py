# -*- coding: utf-8 -*-
"""
Programa que muestra el uso de la 
clase Fraction y como 

9/21 es distinto de  Fraction(9,21)

aunque teoricamente representan lo mismo
computacionalmente no es así

curso: Análisis Numérico  2023-2

Created on Thu Mar  2 07:46:06 2023

@author: rober
"""
from fractions import Fraction

class OperacionesSobreListas:


    v = [Fraction(9,21), Fraction(3,5), Fraction(26,42)]
    vfail = [9/21, 3/5, 26/42]
 
    def maximo(v):
        max = v[0];
        for x in v:
            if x > max:
                max = x
        return max    
 
    def minimo(v):
        min = v[0];
        for x in v:
            if x < min:
                min = x
        return min  
 
    def main(v, vfail, maximo, minimo):
        print ("La lista es ", v)
        print ("El máximo como fracción es ", maximo(v))
        print ("El mínimo como fracción es ", minimo(v))
        print ("El máximo es ", maximo(vfail))
        print ("El mínimo es ", minimo(vfail))
        print ("Usando las funciones nax y min de Python")
        print ("El número máximo es: ", max(v))
        print ("El número mínimo es: ", min(v))
        print ("El número máximo es: ", Fraction(max(vfail)))
        print ("El número minimo es: ", Fraction(min(vfail)))
        
 
    main(v, vfail, maximo, minimo)
  