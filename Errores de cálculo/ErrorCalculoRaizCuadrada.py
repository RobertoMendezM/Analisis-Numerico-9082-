# -*- coding: utf-8 -*-
"""
Curso: Análisis Numérico  2023-2

Error de Propagación

Libro: Einar Smith, Introduction to the Tools
 *          of Scientific Computing
 *          pág. 24     

Created on Tue Jan 31 10:02:43 2023
@author: Roberto Méndez Méndez
"""

from math import sqrt
n = 10; x = 2
for _ in range(n): 
    x = sqrt(x)
print("La " + str(n) +"-esima raíz de 2 es: " + str(x))
for _ in range(n): x = x**2
print(x)