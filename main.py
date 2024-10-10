from primes import *

def main():
    while True:

        print("Seleccione una opción:")
        print("1. Algoritmo de la criba")
        print("2. Prueba de primalidad")
        print("3. Algoritmo de Euclides")
        print("4. Coeficientes de Bézout")
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
            num = input("Ingrese un número: ")
            try:
                n = int(num)
                print("Los números primos menores a", n, "son:")
                print(str(criba(n)) + "\n")
            except ValueError:
                print("Ingrese un número entero para la criba \n")

        elif option == 2:
            num = input("Ingrese un número: ")
            try: 
                n = int(num)
                isprime = is_prime(n)
                prime = isprime[0]
                number = isprime[1]

                if prime:
                    print("El número", str(n), " es primo" + "\n")
                else:
                    print("El número", str(n), "no es primo, pues lo divide", str(number) + "\n")

            except ValueError:
                print("Ingrese un número entero para el test de primalidad \n")

        elif option == 3:
            first = input("Ingrese el primer número: ")
            second = input("Ingrese el segundo número: ")
            try:
                x = int(first)
                y = int(second)
                print("El mcd de ", str(x), "y", str(y),  " es:", str(euclidean(x, y)) + "\n")

            except ValueError:
                print("Ingrese dos números enteros para obtener el MCD \n")
                

        elif option == 4:
            n1 = input("Ingrese el primer número: ")
            n2 = input("Ingrese el segundo número: ")
            try:
                a = int(n1)
                b = int(n2)
                print(f"Los coeficientes de bozout para {a} y {b} son {bezout(a, b)[0]} y {bezout(a, b)[1]}, respectivamente\n")
            except ValueError:
                print("Ingrese dos números enteros para obtener los coeficientes de Bézout\n")

        elif option == 5:
            print("Saliendo...\n")
            break

        else:
            print("Por favor ingrese una opción válida\n")
            continue
        
if __name__ == "__main__":
    main()