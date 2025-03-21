"""
Usaremos este script para enseñar Python a principiantes absolutos.
El script es un ejemplo de Fizz-Buzz implementado en Python.

El problema de FizzBuzz:
Para todos los enteros entre 1 y 99 (incluidos ambos):
    # imprimir fizz para múltiplos de 3
    # imprimir buzz para múltiplos de 5
    # imprimir fizzbuzz para múltiplos de 3 y 5
"""

def fizzbuzz(max_num):
   
    for i in range(1,max_num):
        
        if i%3==0 and i%5==0:
            print(i,"fizzbuzz")
        elif i%3==0:
            print(i,"fizz")
        elif i%5==0:
            print(i,"Buzz")

#----Iniciar el script
if __name__=='__main__':
    fizzbuzz('16')
