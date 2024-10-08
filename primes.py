# Brandon Rivera - 
# Nils Muralles - 23727
# Matemática Discreta - Sección 30

import numpy as np

def prime_test_1(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(3, n):
            if n % i == 0:
                return False
            else:
                return True

def criba(n):
    primes = []
    not_primes = set()

    for i in range(2, n):
        if i in not_primes:
            continue

        for j in range(i*2, n+1, i):
            not_primes.add(j)

        primes.append(i)

    return primes

def is_prime(n):
    prime_list = criba(int(np.sqrt(n)))
    
    for i in prime_list:
        if n % i == 0:
            return False
        else:
            return True
        
def euclidean(x,y):
    #El numero mayor es asignado como a y el menor como b
    if x < y: 
        a = y
        b = x
    else:
        a = x
        b = y

    while b != 0: #Mientras b no sea 0, se continua el algoritmo
        n = a // b #Cantidad de veces que cabe b en a
        c = a - (n * b)
        a = b
        b = c
    
    return a #El mcd es el ultimo valor de a
    
def bezout(a, b):
    bezout_quotients = np.array((1, 2)) # Arreglo donde se guardan los coeficientes de Bézout
    matrixes = [] # Arreglo que almacena las matrices Q1 Q2 ... Qn
    M = np.eye(2)
    detM = 1

    r = a % b
    while r != 0:
        r = a % b
        q = int(a / b)
        Q = np.array([[q, 1], [1, 0]]) # Matriz Qn
        matrixes.append(Q)
        a = b
        b = r 

    if (len(matrixes) % 2 == 1): # Si se multiplicó una cantidad impar de matrices, el determinante es -1
        detM = -1
        
    for matrix in matrixes:
        M = np.dot(M, matrix)

    bezout_quotients[0] = M[1, 1]
    bezout_quotients[1] = (M[0, 1]) * - 1

    if detM == 1:
        return bezout_quotients
    else: 
        return bezout_quotients * -1