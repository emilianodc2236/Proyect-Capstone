# Capstone: BattleShip (Juego de Estrategia Naval en Consola)

Desarrollado de forma individual como un proyecto de programación estructurada, Capstone es una implementación interactiva en formato CLI (interfaz de línea de comandos) del juego Battleship (Batalla Naval). El programa permite al usuario enfrentarse a la CPU.

### Características principales

* Tableros dinámicos y paramétricos: El usuario define las dimensiones del tablero del juego a través de la consola de comandos.
* Algoritmo de validación de colisiones: El código implementa de lógica matemática para comprobar la disponibilidad de coordenadas tanto para el usuario como para la generación aleatoria de la CPU, evitando la superposición de embarcaciones y desbordamientos del tablero (out of bounds).
* IA enemiga automatizada: La CPU cuenta con un motor de posicionamiento pseudoaleatorio basado en la biblioteca random, capaz de reintentar colocaciones de forma iterativa hasta encontrar configuraciones válidas.
* Interfaz visual dinámica (UI): Renderizado en consola optimizado mediante la biblioteca colorama, diferenciando los tableros por paletas de colores (Cian para el usuario, Rojo para el enemigo) y marcando impactos (O) o agua (X) en tiempo real.
* Persistencia de datos básica: Lectura e integración de archivos planos externos (manual.txt) para la carga de instrucciones de usuario.

### Tecnologías y módulos utilizados

* Python 3.x: Lenguaje base de desarrollo.
* Colorama: Gestión de estilos y colores en el flujo de salida estándar (consola).
* Copy (deepcopy): Utilizado para la clonación profunda de los estados de los tableros, aislando las fases de inicialización, posicionamiento y juego.
* Random: Base para la toma de decisiones algorítmicas de la CPU (coordenadas, orientaciones y vectores de dirección).

### Arquitectura del código

El desarrollo lleva una programación estructurada:

* construirTablero(numF, numC): Genera la matriz inicial y formatea las cabeceras numéricas de filas y columnas.
* barcosChocan(tablero, fila, columna): Evalúa el estado de una celda específica antes de realizar modificaciones.
* colocarBarcos() / barcosCpu(): Administran los vectores de dirección (arriba, abajo, izquierda, derecha) para el despliegue de barcos de tamaño variable (2 a 4 celdas).
* disparosBarcos() / disparoBarcosCpu(): Controlan el ciclo de daño, modificando el estado de los tableros en función de los impactos.
* verificarGanador(tablero): Escanea recursivamente los elementos remanentes de la matriz para dictaminar el fin de la partida.

### Cómo ejecutar el proyecto

1. Asegúrate de tener instalado Python y la dependencia colorama (instalable mediante `pip install colorama`).
2. Descarga el código fuente de este repositorio.
3. Asegúrate de incluir el archivo llamado manual.txt en la misma carpeta raíz.
4. Ejecuta el script principal desde tu terminal: `python battleship.py`

Autor: Emiliano Delgado Carreño – Estudiante de Ingeniería Mecatrónica.
