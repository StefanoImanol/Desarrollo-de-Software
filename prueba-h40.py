import time
from datetime import datetime, timedelta

class CarritoReservas:
    def __init__(self, tiempo_limite_minutos=10):
        self.tiempo_limite = timedelta(minutes=tiempo_limite_minutos)
        self.carritos = {}  # key: usuario_id, value: {'entradas': list, 'timestamp': datetime}

    def reservar(self, usuario_id, entradas):
        ahora = datetime.now()
        self.carritos[usuario_id] = {
            'entradas': entradas,
            'timestamp': ahora
        }
        print(f"[{ahora}] Entradas reservadas para usuario {usuario_id}: {entradas}")

    def verificar_expiraciones(self):
        ahora = datetime.now()
        expirados = []
        for usuario_id, datos in self.carritos.items():
            if ahora - datos['timestamp'] > self.tiempo_limite:
                expirados.append(usuario_id)

        for usuario_id in expirados:
            self.liberar(usuario_id)

    def liberar(self, usuario_id):
        if usuario_id in self.carritos:
            print(f"[{datetime.now()}] Reserva expirada para usuario {usuario_id}. Entradas liberadas: {self.carritos[usuario_id]['entradas']}")
            del self.carritos[usuario_id]

    def mostrar_carritos(self):
        print("Estado actual de carritos:")
        for usuario_id, datos in self.carritos.items():
            print(f"- Usuario {usuario_id}: {datos['entradas']}, reservado a las {datos['timestamp']}")

# Ejemplo de uso
if __name__ == "__main__":
    sistema = CarritoReservas(tiempo_limite_minutos=1)

    sistema.reservar("usuario1", ["entrada_101", "entrada_102"])
    time.sleep(30)  # espera 30 segundos
    sistema.reservar("usuario2", ["entrada_201"])

    sistema.mostrar_carritos()

    print("\n--- Verificando expiraciones después de 90 segundos ---\n")
    time.sleep(90)
    sistema.verificar_expiraciones()
    sistema.mostrar_carritos()

