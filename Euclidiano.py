
def Euclidiano(x,y):
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
    
def main():
    a = int(input("Ingrese un entero a: "))
    b = int(input("Ingrese un entero b: "))
    print("El mcd es: " + str(Euclidiano(a,b)))

main()