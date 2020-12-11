def es_primo(numero):
    for n in range(2, numero):
        if numero % n == 0:
            print("es divisible por " + str(n))
            return False
    return True


def run():
    numero = int(input("Ingresa el número que quieres saber si es Primo: "))
    if es_primo(numero):
        print(str(numero) + " Es un numero primo." )
    else:
        print(str(numero) + " No es un numero primo." )


if __name__ == "__main__":
    run()