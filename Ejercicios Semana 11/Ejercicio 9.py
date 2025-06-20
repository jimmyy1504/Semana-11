def imprimir_tabla_multiplicar(numero):
    """Imprime la tabla de multiplicar del número dado."""
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# Solicitar el número al usuario
try:
    numero = int(input("Ingrese un número entero: "))
    imprimir_tabla_multiplicar(numero)
except ValueError:
    print("Por favor, ingrese un número válido.")