def run():
    i = 3
    while i < 9 :
        i = i + 3
        if i % 2 != 0: # Identifica numeros impares y salta el ciclo
            continue
        elif i == 7: # "i" Nunca será 7, 7 es impar.
            break
        print(str(i)+ ": Es un número Par")
    

if __name__ == "__main__":
    run()
