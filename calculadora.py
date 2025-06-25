def main() -> None:
    # haciendo el codigo unico
    print("***** Calculadora by SeguraDev ***** \n")

    print(
        "Tomaremos 2 valores y realizaremos todas las operaciones matemáticas básicas con ellos \n"
    )
    # solicitamos los valores al usuario
    valor1: float = float(input("Introduzca el primer valor: \n"))
    valor2: float = float(input("Introduzca el segundo valor: \n"))

    # definimos los resultados
    resultadoSuma = operacion(valor1, valor2, "suma")
    resultado(resultadoSuma, "suma")
    resultadoResta = operacion(valor1, valor2, "resta")
    resultado(resultadoResta, "resta")
    resultadoMult = operacion(valor1, valor2, "multiplicacion")
    resultado(resultadoMult, "multiplicacion")
    resultadoDiv = operacion(valor1, valor2, "division")
    resultado(resultadoDiv, "division")


# funcion para definir las operaciones
def operacion(valor1: float, valor2: float, tipo: str) -> float:
    """
    Recibe 2 valores y un tipo.
    Luego devuelve el resultado de las operaciones en un flotante

    """
    match tipo:
        case "suma":
            return valor1 + valor2
        case "resta":
            return valor1 - valor2
        case "multiplicacion":
            return valor1 * valor2
        case "division":
            return valor1 / valor2
        case _:
            return 0.0


# funcion para definir los resultados e imprimirlos por pantalla
def resultado(resultado, tipo):
    print(f"El resultado de la {tipo} es: {resultado} \n")


main()
