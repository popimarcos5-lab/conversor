temperatura =(str(input("temperatura: ")))
try:
    respuesta = input("celsius[c] o farenheit[f]:")
    resultado = str(respuesta)
    if (str(resultado) == "c"):
        print((int(temperatura) * 9/5) + 32)
    elif (str(resultado) == "f"):
        print((int(temperatura) - 32) * 5/9)
    else:
        print("sistema no reconocido")
except ValueError:
    print("valor no valido")
