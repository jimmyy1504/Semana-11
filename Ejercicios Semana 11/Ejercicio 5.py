def calcular_factorial(n):
    """Retorna el factorial de un número."""
    if n == 0 or n == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, n + 1):
            factorial *= i
        return factorial

# Capturar el número por teclado
try:
    numero = int(input("Ingrese un número para calcular su factorial: "))
    if numero < 0:
        print("El factorial no está definido para números negativos.")
    else:
        print(f"El factorial de {numero} es {calcular_factorial(numero)}")
except ValueError:
    print("Por favor, ingrese un número entero válido.")