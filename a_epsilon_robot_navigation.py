# Importar las bibliotecas necesarias
import heapq  # Para utilizar la cola de prioridad (min-heap)
import matplotlib.pyplot as plt  # Para la visualización gráfica del mapa

# Mapa de ejemplo: 0 = libre, 1 = bloqueado
# El robot debe encontrar una ruta desde el inicio (0,0) hasta el objetivo (4,4)
terrain = [
    [0, 0, 0, 1, 0],  # Fila 0
    [0, 1, 0, 1, 0],  # Fila 1
    [0, 1, 0, 0, 0],  # Fila 2
    [0, 0, 0, 1, 0],  # Fila 3
    [1, 0, 0, 0, 0]   # Fila 4
]

# Coordenadas de inicio y fin del robot
start = (0, 0)  # El robot comienza en la esquina superior izquierda
goal = (4, 4)   # El objetivo está en la esquina inferior derecha

# Definición del algoritmo A-Epsilon
# A-Epsilon es una variante del algoritmo A* que ajusta la influencia de la heurística
def a_epsilon(terrain, start, goal, epsilon=2.0):
    rows, cols = len(terrain), len(terrain[0])  # Obtener las dimensiones del mapa
    open_list = []  # Lista de nodos a explorar (en este caso una cola de prioridad)
    heapq.heappush(open_list, (0, start))  # Insertamos el nodo de inicio con valor de f = 0
    came_from = {}  # Diccionario para rastrear el camino
    g_score = {start: 0}  # Diccionario para almacenar los costos desde el inicio
    f_score = {start: heuristic(start, goal)}  # Diccionario para almacenar los costos estimados hasta el objetivo

    # Mientras haya nodos por explorar
    while open_list:
        # Sacamos el nodo con el menor valor de f
        current_f, current = heapq.heappop(open_list)
        
        # Si llegamos al objetivo, reconstruimos la ruta
        if current == goal:
            return reconstruct_path(came_from, current)

        # Explorar los vecinos del nodo actual
        for neighbor in get_neighbors(current, rows, cols):
            if terrain[neighbor[0]][neighbor[1]] == 1:
                continue  # Si el vecino es un obstáculo (bloqueado), lo ignoramos

            # Calculamos el costo acumulado para llegar al vecino
            tentative_g_score = g_score[current] + 1  # Asumimos que cada paso tiene costo 1

            # Si encontramos un camino más corto al vecino, lo actualizamos
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current  # Guardamos de dónde venimos
                g_score[neighbor] = tentative_g_score  # Actualizamos el costo acumulado
                f_score[neighbor] = tentative_g_score + epsilon * heuristic(neighbor, goal)  # Calculamos f con el parámetro epsilon
                heapq.heappush(open_list, (f_score[neighbor], neighbor))  # Insertamos el vecino en la cola de prioridad

    # Si no se encontró un camino, devolvemos None
    return None

# Función heurística que calcula la distancia Manhattan entre dos puntos
def heuristic(a, b):
    # Distancia Manhattan = |x1 - x2| + |y1 - y2|
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Función para obtener los vecinos de un nodo en el mapa
def get_neighbors(node, rows, cols):
    x, y = node
    neighbors = []
    if x > 0: neighbors.append((x-1, y))  # Arriba
    if x < rows - 1: neighbors.append((x+1, y))  # Abajo
    if y > 0: neighbors.append((x, y-1))  # Izquierda
    if y < cols - 1: neighbors.append((x, y+1))  # Derecha
    return neighbors

# Función para reconstruir el camino desde el nodo final hasta el inicio
def reconstruct_path(came_from, current):
    path = []  # Lista para almacenar el camino
    while current in came_from:
        path.append(current)  # Agregar el nodo al camino
        current = came_from[current]  # Ir al nodo anterior
    path.append(current)  # Agregar el nodo final (el objetivo)
    path.reverse()  # Invertir el camino para que vaya desde el inicio hasta el objetivo
    return path

# Ejecutar el algoritmo A-Epsilon con un valor de epsilon=2.0
path_epsilon = a_epsilon(terrain, start, goal, epsilon=2.0)

# Imprimir la ruta en consola
if path_epsilon:
    print("Ruta encontrada:")
    for step in path_epsilon:
        print(f"Paso: {step}")
else:
    print("No se encontró una ruta.")

# Función para visualizar la ruta y el mapa usando matplotlib
def plot_path(terrain, path, start, goal):
    # Crear una figura y un eje para la visualización
    fig, ax = plt.subplots()
    # Mostrar el mapa usando una escala de grises (0 es blanco, 1 es negro)
    ax.imshow(terrain, cmap='Greys', origin='upper')

    # Dibujar el camino encontrado (celdas del camino en azul)
    for (x, y) in path:
        if terrain[x][y] == 0:  # Solo trazar si es una celda libre
            ax.plot(y, x, 'bo')  # Marca las celdas del camino con un círculo azul

    # Marcar el inicio y el fin en el mapa
    ax.plot(start[1], start[0], 'go', label='Inicio')  # Marca el inicio con un círculo verde
    ax.plot(goal[1], goal[0], 'ro', label='Meta')  # Marca la meta con un círculo rojo

    # Agregar una leyenda y título
    plt.legend()
    plt.title("Ruta de A-Epsilon")
    plt.show()

# Visualizar la ruta encontrada
plot_path(terrain, path_epsilon, start, goal)