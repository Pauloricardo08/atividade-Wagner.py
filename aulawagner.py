try:
    num1 = float(input("digite o primeiro número: "))
    num2 = float(input("digite o segundo número: "))

    resultado = num1 / num2
    print(" resultado "), resultado)

except ValueError:
    print("entrada inválida! digite apenas números.")

except ZeroDivisionError:
    print("não é possível dividir por zero!")