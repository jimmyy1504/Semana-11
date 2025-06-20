import math

def calcular_area_circulo(radio):
    """Devuelve el área de un círculo dado su radio."""
    return math.pi * radio ** 2

# Capturar el radio del círculo por teclado
try:
    radio = float(input("Ingrese el radio del círculo: "))
    if radio < 0:
        print("El radio no puede ser negativo.")
    else:
        print(f"El área del círculo es: {calcular_area_circulo(radio):.2f}")
except ValueError:
    print("Por favor, ingrese un número válido.")