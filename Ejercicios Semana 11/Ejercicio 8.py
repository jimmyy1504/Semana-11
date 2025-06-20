def calcular_importe_final(importe):
    """Calcula el importe final aplicando los descuentos según el monto de compra."""
    if importe > 500:
        descuento = 0.12  # 12% de descuento
    elif importe > 300:
        descuento = 0.10  # 10% de descuento
    else:
        descuento = 0.05  # 5% de descuento

    importe_final = importe - (importe * descuento)
    return importe_final

# Solicitar el importe de la compra al usuario
try:
    importe_compra = float(input("Ingrese el importe de la compra (€): "))
    if importe_compra < 0:
        print("El importe no puede ser negativo.")
    else:
        print(f"El importe final a pagar es: {calcular_importe_final(importe_compra):.2f} €")
except ValueError:
    print("Por favor, ingrese un número válido.")