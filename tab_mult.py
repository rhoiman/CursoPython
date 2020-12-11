def run():
    tabla = input("¿Cúal tabla de multiplicar quieres consultar?: ")
    
    for i in range(11):
        print (str(tabla) + " * " + str(i) + " = " + str(int(tabla)*i))
    

if __name__ == "__main__":
    run()
