# Brandon Rivera - 
# Nils Muralles - 23727
# Matemática Discreta - Sección 30

import math

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
    prime_list = criba(int(math.sqrt(n) + 1))
    result = []
    
    for i in prime_list:
        if n % i == 0:
            result.append(False)
            result.append(i)
        else:
            continue
    
    if len(result) == 0:
        result.append(True)
        result.append(0)

    return result
        
        
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

def main():
    while True:

        print("Seleccione una opción:")
        print("1. Algoritmo de la criba")
        print("2. Prueba de primalidad")
        print("3. Algoritmo de Euclides")
        print("4. Algoritmo de Bézout")
        print("5. Salir")
        option = input("Opción: ")

        while True:
            try :
                option = int(option)
                break
            except ValueError:
                print("Por favor ingrese un número entero")
                option = input("Opción: ")
        
        if option == 1:
            n = int(input("Ingrese un número: "))
            print("Los números primos menores a", n, "son:")
            print(criba(n))

        elif option == 2:
            n = int(input("Ingrese un número: "))
            isprime = is_prime(n)
            prime = isprime[0]
            number = isprime[1]

            if prime:
                print("El número", n, " es primo")
            else:
                print("El número", n, "no es primo, pues lo divide", number)

        elif option == 3:
            x = int(input("Ingrese el primer número: "))
            y = int(input("Ingrese el segundo número: "))
            print("El mcd de ", x, "y", y,  " es:", euclidean(x, y))

        elif option == 4:
            a = int(input("Ingrese el primer número: "))
            b = int(input("Ingrese el segundo número: "))
            print("Los coeficientes de Bezout de ", a, "y", b ,"son", bezout(a, b))

        elif option == 5:
            print("Saliendo...")
            break

        else:
            print("Por favor ingrese una opción válida")
            continue
        

main()