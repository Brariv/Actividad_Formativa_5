# Seccion 30

import time
import numpy as np

def prime_test1(n):
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

def prime_test2(n):
    prime_list = criba(int(np.sqrt(n))13)
    
    for i in prime_list:
        if n % i == 0:
            return False
        else:
            return True
    
    

a = int(input("Ingrese un entero n: "))
Start_time = time.time()
print(prime_test2(a))
End_time = time.time()
print("El tiempo de ejecucion es: ", End_time - Start_time)

#print(criba(20))