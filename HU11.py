# Simulación de base de datos de eventos
# hola
eventos = [
    {"id": 1, "nombre": "Concierto Coldplay", "artista": "Coldplay"},
    {"id": 2, "nombre": "Festival de Jazz Lima", "artista": "Varios"},
    {"id": 3, "nombre": "Show de Bad Bunny", "artista": "Bad Bunny"},
    {"id": 4, "nombre": "Teatro Hamlet", "artista": "Compañía Nacional"},
    {"id": 5, "nombre": "Concierto de Shakira", "artista": "Shakira"},
]

def buscar_eventos(termino_busqueda):
    termino_busqueda = termino_busqueda.lower()
    resultados = []

    for evento in eventos:
        if termino_busqueda in evento["nombre"].lower() or termino_busqueda in evento["artista"].lower():
            resultados.append(evento)

    return resultados

# Interfaz de ejemplo
if __name__ == "__main__":
    print("=== Buscador de Eventos ===")
    busqueda = input("Introduce nombre del evento o artista: ")
    encontrados = buscar_eventos(busqueda)

    if encontrados:
        print("\nEventos encontrados:")
        for evento in encontrados:
            print(f"- {evento['nombre']} (Artista: {evento['artista']})")
    else:
        print("No se encontraron eventos con ese criterio.")
