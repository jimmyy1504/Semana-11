def calcular_comision(ventas, porcentaje_comision):
    """Calcula la comisión total por las ventas."""
    return ventas * porcentaje_comision

def calcular_sueldo_total(sueldo_base, comision_total):
    """Calcula el sueldo total sumando la comisión."""
    return sueldo_base + comision_total

# Solicitar datos al usuario
try:
    n_vendedores = int(input("Ingrese el número de vendedores: "))
    sueldo_base = float(input("Ingrese el sueldo base de cada vendedor: "))
    monto_venta = float(input("Ingrese el monto de cada venta: "))
    
    porcentaje_comision = 0.10  # 10% de comisión por cada venta
    ventas_por_vendedor = 3     # Cada vendedor realiza 3 ventas
    
    for i in range(n_vendedores):
        comision = calcular_comision(monto_venta * ventas_por_vendedor, porcentaje_comision)
        sueldo_total = calcular_sueldo_total(sueldo_base, comision)
        
        print(f"\nVendedor {i+1}:")
        print(f"Comisión por las tres ventas: ${comision:.2f}")
        print(f"Sueldo total con comisiones: ${sueldo_total:.2f}")

except ValueError:
    print("Por favor, ingrese valores numéricos válidos.")