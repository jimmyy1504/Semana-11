def calcular_pago(horas_trabajadas):
    """Calcula el pago total según la cantidad de horas trabajadas."""
    tarifa_normal = 6.5   # Tarifa para las primeras 160 horas
    tarifa_extra = 7.5    # Tarifa para horas adicionales

    if horas_trabajadas <= 160:
        pago_total = horas_trabajadas * tarifa_normal
    else:
        pago_total = (160 * tarifa_normal) + ((horas_trabajadas - 160) * tarifa_extra)

    return pago_total

# Capturar las horas trabajadas por teclado
try:
    horas = int(input("Ingrese el número de horas trabajadas: "))
    pago = calcular_pago(horas)
    print(f"Total a pagar: ${pago:.2f}")
except ValueError:
    print("Por favor, ingrese un número válido.")