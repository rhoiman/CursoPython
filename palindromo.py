def palindromo(palabra):
    palabra = (palabra.upper()).strip() 
    # convierte a mayuscula y elimina espacios [ .strip() ]
    if palabra == (palabra[::-1]): 
        # compara el string con el string invertido
        return True
    else:
        return False


def run():
    palabra = input("Ingresa una palabra o frase: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("Es palíndromo")
    else:
        print("No es palíndromo")


if __name__ == '__main__':
    run()
