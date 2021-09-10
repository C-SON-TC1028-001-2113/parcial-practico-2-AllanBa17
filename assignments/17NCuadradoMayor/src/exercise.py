

def main():
    numero = int(input("Escribe un numero : "))
    #escribe tu código abajo de esta línea
    i = 1
    while i**2<=numero:
        i = i+1
    if i**2>numero:
        print(i)

if __name__=='__main__':
    main()
