def calcular_descuento_renta(salario):
    """Calcula el descuento de renta (10%) sobre el salario."""
    return salario * 0.10

# Solicitar cantidad de empleados
try:
    num_empleados = int(input("Ingrese la cantidad de empleados: "))

    for i in range(num_empleados):
        salario = float(input(f"Ingrese el salario del empleado {i+1}: "))
        descuento = calcular_descuento_renta(salario)
        salario_neto = salario - descuento

        print(f"\nEmpleado {i+1}:")
        print(f"Salario bruto: ${salario:.2f}")
        print(f"Descuento de renta: ${descuento:.2f}")
        print(f"Salario neto a pagar: ${salario_neto:.2f}")

except ValueError:
    print("Por favor, ingrese valores numéricos válidos.")