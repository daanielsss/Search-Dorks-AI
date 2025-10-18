#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countResponseTimeRegressions' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY responseTimes as parameter.
#

def countResponseTimeRegressions(responseTimes):
    # identificar la posicion del numeor actual, a partir de esa posicion tomar los numeros anteriores, sumarlos y dividirlos entre la cantidad de numeros que son, tomar el valor del numero actual y si es mayor que el promedio de los anteriores agregar un uno al contador hasta terminar con la lista
    longitud = len(responseTimes) #4
    contador = 0
    
    for i in range(longitud):
        numero_actual = responseTimes[i]
        elementos_anteriores = responseTimes[:i]
        suma = sum(elementos_anteriores)
        if suma and  elementos_anteriores != 0:
            lonitudelementos= len(elementos_anteriores)
            average = suma/lonitudelementos
            
            if numero_actual > average:
                contador += 1
            
            else: 
                contador = 0  
        elif suma == 0:   
            return contador 

if __name__ == '__main__':
    responseTimes_count = int(input().strip())

    responseTimes = []

    for _ in range(responseTimes_count):
        responseTimes_item = int(input().strip())
        responseTimes.append(responseTimes_item)

    result = countResponseTimeRegressions(responseTimes)

    print(result)