def calcular_presupuesto(monto_anual):
    """Calcula el presupuesto asignado a cada departamento."""
    porcentajes = {
        "Recursos Humanos": 0.50,
        "Manufactura": 0.25,
        "Empaquetado": 0.15,
        "Publicidad": 0.10
    }
    
    presupuesto_departamentos = {dept: monto_anual * porc for dept, porc in porcentajes.items()}
    
    for departamento, monto in presupuesto_departamentos.items():
        print(f"{departamento}: ${monto:.2f}")

# Solicitar el monto al usuario
monto_anual = float(input("Ingrese el presupuesto anual: "))
calcular_presupuesto(monto_anual)