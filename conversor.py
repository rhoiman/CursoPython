def convertir(tipo_peso, valor_dolar):
    pesos = float(input('¿Cúantos pesos ' + tipo_peso +  ' quieres convertir a dólares?: '))
    dolares = str(round((pesos/valor_dolar), 2))
    print('Son $' + dolares + 'USD')


menu = """
Conversor Dólar - Pesos - Bólivares
------------------------------------
1- Pesos colombianos a Dólar
2- Pesos argentinos a Dólar
3- Pesos mexicanos a Dólar

Seleccione una opción: """

opcion = input (menu)

if opcion == "1":
    convertir("colombianos", 3875)
elif opcion == "2":
    convertir("argentinos", 65)
elif opcion == "3":
    convertir("mexicanos", 20)
else:
    print(str(opcion) + " No es una opción valida. Fin del programa.")


# valor_dolar = float(input('¿Qué precio tiene hoy el dolar a razón de pesos mexicanos?: '))
# pesos = float(input('¿Cúantos pesos mexicanos quieres convertir a dólares?: '))
# dolares = str(round((pesos/valor_dolar), 2))
# print('Son $' + dolares + 'USD')
# dolares = float(input('¿Cúantos Dólares quieres convertir a Pesos mexicanos?: '))
# pesos = str(round((dolares/valor_dolar), 2))
# print('Son $' + pesos + 'MXN')