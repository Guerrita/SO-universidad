# Definir la lista de procesos
procesos = [{'nombre': 'P1', 'tiempo': 8},
            {'nombre': 'P2', 'tiempo': 4},
            {'nombre': 'P3', 'tiempo': 9},
            {'nombre': 'P4', 'tiempo': 5},
            {'nombre': 'P5', 'tiempo': 2}]

# Definir el quantum
quantum = 3

# Definir la función para el algoritmo de Round Robin
def round_robin(procesos, quantum):
    tiempo_total = 0
    procesos_restantes = len(procesos)
    cola_procesos = procesos.copy()
    while procesos_restantes > 0:
        for i in range(len(cola_procesos)):
            if cola_procesos[i]['tiempo'] > 0:
                if cola_procesos[i]['tiempo'] > quantum:
                    tiempo_total += quantum
                    cola_procesos[i]['tiempo'] -= quantum
                else:
                    tiempo_total += cola_procesos[i]['tiempo']
                    cola_procesos[i]['tiempo'] = 0
                    procesos_restantes -= 1
            else:
                procesos_restantes -= 1
    return tiempo_total

# Llamar a la función y mostrar el resultado
tiempo_total = round_robin(procesos, quantum)
print('Tiempo total:', tiempo_total)