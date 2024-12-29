# Navegación de un Robot en un Terreno Dinámico usando A-Epsilon

## Descripción del Proyecto
Este repositorio contiene la implementación del algoritmo **A-Epsilon**, una variante del algoritmo A*, que guía a un robot para encontrar una ruta en un mapa con obstáculos. El objetivo es encontrar el camino más corto desde una posición inicial hasta un objetivo, ajustando la influencia de la heurística a través de un parámetro ϵ (*epsilon*).

### Características Principales
- Navegación eficiente en un terreno dinámico representado como una matriz 5x5.
- Uso del algoritmo A-Epsilon con ponderación ajustable para la heurística.
- Visualización del mapa y la ruta encontrada utilizando Matplotlib.

## Estructura del Proyecto

### Archivos
- **`a_epsilon_robot_navigation.py`**: Script principal que incluye la implementación del algoritmo y la visualización.
- **`Franklin Camacho - Navegación de un Robot en un Terreno Dinámico.pdf`**: Documento explicativo con detalles del problema, algoritmo y resultados.

### Algoritmo A-Epsilon
- **Costo acumulado (g(n))**: Distancia recorrida desde el inicio hasta un nodo.
- **Heurística (h(n))**: Distancia Manhattan entre el nodo actual y el objetivo.
- **Función de evaluación**:  
  \[
  f(n) = g(n) + \epsilon \cdot h(n)
  \]  
  El parámetro ϵ permite equilibrar la exploración y la explotación.

## Resultados
- **Mapa inicial**: El robot navega en un terreno representado como una matriz donde:
  - `0` indica celdas transitables.
  - `1` indica celdas bloqueadas.
- **Ruta encontrada**: El algoritmo encuentra el camino óptimo desde `(0, 0)` hasta `(4, 4)` evitando obstáculos.
- **Visualización**: La ruta se destaca en el mapa con puntos azules, y se marcan el inicio (verde) y el objetivo (rojo).

## Requisitos

### Dependencias
- `heapq`: Para manejar la cola de prioridad.
- `matplotlib`: Para la visualización gráfica.

### Instalación
1. Clona el repositorio:
   ```bash
   git clone https://github.com/usuario/robot-navigation-a-epsilon.git
   ```
2. Instala las dependencias:
   ```bash
   pip install matplotlib
   ```

## Ejecución
1. Ejecuta el script principal:
   ```bash
   python a_epsilon_robot_navigation.py
   ```
2. Observa los resultados en la terminal y la visualización gráfica del mapa.

## Visualización
- **Celdas negras**: Obstáculos.
- **Celdas blancas**: Transitables.
- **Ruta**: Destacada en azul.
- **Inicio y Meta**: Marcados con colores verde y rojo, respectivamente.

## Contribución
Si deseas contribuir:
1. Haz un fork del repositorio.
2. Crea una rama para tu función:
   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```
3. Realiza un pull request con tus cambios.
=