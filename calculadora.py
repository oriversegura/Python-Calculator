# Practica de Calculadora Intuitiva (Empirica)
# He recibido una que otra ayuda de amigos programadores


def main():
    # haciendo el codigo unico
    print("Calculadora basica By SeguraDev")

    print(
        "Tomaremos 2 valores y realizaremos todas las operaciones matematicas basicas con ellos"
    )
    # solicitamos los valores al usuario
    print("Introduzca el primer valor: ")
    valor1 = float(input())
    print("Introduzca el segundo valor: ")
    valor2 = float(input())

    # definimos los resultados
    resultadoSuma = operacion(valor1, valor2, "suma")
    resultado(resultadoSuma, "suma")
    resultadoResta = operacion(valor1, valor2, "resta")
    resultado(resultadoResta, "resta")
    resultadoMult = operacion(valor1, valor2, "multiplicacion")
    resultado(resultadoMult, "ultiplicacion")
    resultadoDiv = operacion(valor1, valor2, "division")
    resultado(resultadoDiv, "division")


# funcion para definir las operaciones
def operacion(valor1, valor2, tipo):
    """
    Recibe 2 valores y un tipo.
    Luego devuelve el resultado de las operaciones

    """
    if tipo == "suma":
        return valor1 + valor2
    elif tipo == "resta":
        return valor1 - valor2
    elif tipo == "multiplicacion":
        return valor1 * valor2
    elif tipo == "division":
        return valor1 / valor2


# funcion para definir los resultados e imprimirlos por pantalla
def resultado(resultado, tipo):
    """
    Recibe el resultado de las operaciones y el tipo de operaciones

    """
    print(f"El resultado de la {tipo} es: {resultado}")


if __name__ == "__main__":
    main()
