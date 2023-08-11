#Practica de Calculadora Intuitiva (Empirica)
# He recibido una que otra ayuda de amigos

def main():    
    print("Calculadora basica By SeguraDev")

    print("Tomaremos 2 valores y realizaremos todas las operaciones matematicas basicas con ellos")

    print("Introduzca el primer valor: ")
    valor1=float(input())
    print("Introduzca el segundo valor: ")
    valor2=float(input())

    resultadoSuma = operacion(valor1, valor2, "suma")    
    resultado(resultadoSuma, "suma")
    resultadoResta = operacion(valor1, valor2, "resta")
    resultado(resultadoResta, "resta")
    resultadoMult = operacion(valor1, valor2, "multiplicacion")
    resultado(resultadoMult, "multiplicacion")
    resultadoDiv = operacion(valor1, valor2, "division")
    resultado(resultadoDiv, "division")

def operacion(valor1, valor2, tipo):
    if tipo == "suma":
        return valor1 + valor2
    elif tipo == "resta": 
        return valor1 - valor2
    elif tipo == "multiplicacion":
        return valor1 * valor2
    elif tipo == "division":
        return valor1 / valor2     

def resultado (resultado, tipo):
    print("El resultado de la " + tipo + " es: " + str(resultado))
       
main()
