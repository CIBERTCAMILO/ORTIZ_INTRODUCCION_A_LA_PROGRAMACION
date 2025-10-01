def convertir_pen_a_usd():
    # Solicitar al usuario el monto en soles (PEN)
    monto_pen = float(input("Ingrese el monto en soles (PEN): "))
    
    # Preguntar la tasa de cambio actual
    tasa_cambio = float(input("Ingrese la tasa de cambio actual (1 USD = ? PEN): "))
    
    # Calcular el equivalente en dólares (USD)
    monto_usd = monto_pen / tasa_cambio
    
    # Mostrar el resultado con dos decimales
    print("\nConversión en Global Change")
    print(f"Monto en soles: S/ {monto_pen:.2f}")
    print(f"Monto en dólares: $ {monto_usd:.2f}")

# Ejecutar la función
convertir_pen_a_usd()