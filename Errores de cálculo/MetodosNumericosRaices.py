# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 11:34:41 2023

@author: rober
"""

class MetodosNumericosRaices:
    global EPSILONM 
    EPSILONM = 10**(-9)
    
    def f(x):
        y = 3*x**3 - 2*x**2 + 4*x - 5
        return y
    
    def metodoSecanteRaices(f, x1, x2):
        while abs(f(x1)) > EPSILONM :
            f2 = f(x2)
            f1 = f(x1)
            x1 = x1 - (x2 - x1)*f1/(f2 - f1)
            