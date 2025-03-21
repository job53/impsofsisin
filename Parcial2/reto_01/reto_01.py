"""    
Usaremos este script para enseñar Python a principiantes.
El script es un ejemplo de Fizz-Buzz implementado en Python.

El problema de FizzBuzz:
Para todos los enteros entre 1 y 99 (incluidos ambos):
    # imprimir fizz para múltiplos de 3
    # imprimir buzz para múltiplos de 5
    # imprimir fizzbuzz para múltiplos de 3 y 5
"""

def fizzbuzz(max_num):
    "Este metodo implementa FizzBuzz"
    
    tres_mul = 'fizz'
    cinco_mul = 'buzz'
    num1 = 3
    num2 = 5 

    # Busca en Google 'range in python' para ver su funcionamiento
    for i in range(1,max_num):
        # % o modulo
        if i%num1==0 and i%num2==0:
            print(i,tres_mul+cinco_mul)
        elif i%num1=0:
            print(i,tres_mul)
        elif i%num2==0:
            print(i,cinco_mul)

#----Iniciar el script
if __name__=='__main__':
    fizzbuzz(100)
