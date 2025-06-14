import re
from datetime import datetime

def validar_tarjeta(numero, fecha_vencimiento, cvv):
    # Validación simple del número (16 dígitos), fecha y CVV (3 dígitos)
    if not re.fullmatch(r"\d{16}", numero):
        return False, "Número de tarjeta inválido (debe tener 16 dígitos)."
    
    try:
        fecha_dt = datetime.strptime(fecha_vencimiento, "%m/%y")
        if fecha_dt < datetime.now():
            return False, "La tarjeta está vencida."
    except ValueError:
        return False, "Formato de fecha inválido. Usa MM/AA."

    if not re.fullmatch(r"\d{3}", cvv):
        return False, "CVV inválido (deben ser 3 dígitos)."
    
    return True, "Tarjeta válida y aceptada."

def procesar_pago():
    print("=== Pago con Tarjeta de Crédito ===")
    numero = input("Número de tarjeta (16 dígitos): ")
    vencimiento = input("Fecha de vencimiento (MM/AA): ")
    cvv = input("CVV (3 dígitos): ")

    valido, mensaje = validar_tarjeta(numero, vencimiento, cvv)
    if valido:
        print("✅ Pago procesado con éxito. ¡Gracias por tu compra!")
    else:
        print(f"❌ Error: {mensaje}")

# Ejecutar
if __name__ == "__main__":
    procesar_pago()
