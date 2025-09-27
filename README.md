
Descripción General
proporciona una herramienta para generar, cargar y visualizar matrices bidimensionales de datos numéricos utilizando la librería Turtle Graphics de Python. Cada valor en la matriz se representa como un "pixel" coloreado según un mapa de colores predefinido.

Clase VisualizadorMatriz
Propósito
La clase gestiona todo el ciclo de vida del proceso de visualización: configuración del lienzo de dibujo, manejo de la matriz de datos, lógica de carga de archivos, generación de datos aleatorios y el proceso de dibujo celda por celda.

Atributos de Clase
Atributo	Tipo	Descripción
MAPA_COLORES	Dict[str, str]	Diccionario que mapea los valores de la matriz (como strings de '0' a '9') a sus respectivos códigos de color hexadecimal. Cualquier valor fuera de este rango se dibuja en gris.

Exportar a Hojas de cálculo
Constructor (__init__)

__init__(self, ancho_default: int, alto_default: int, tamaño_pixel: int = 7)
Parámetros:

ancho_default (int): Número de columnas de la matriz si se genera de forma aleatoria.

alto_default (int): Número de filas de la matriz si se genera de forma aleatoria.

tamaño_pixel (int, opcional): Tamaño (en píxeles) de cada celda cuadrada en la visualización. Por defecto es 7.

Inicialización: Configura los objetos turtle.Screen y turtle.Turtle (lienzo y tortuga) y establece sus propiedades de dibujo rápido (velocidad 0, tracer(0)).

Métodos Públicos
1. generar_matriz_en_memoria

generar_matriz_en_memoria(self, max_num: int = 9)
Descripción: Llena el atributo self.matriz_datos con una matriz aleatoria utilizando las dimensiones (self.alto, self.ancho) definidas en el constructor.

Parámetros:

max_num (int, opcional): El número entero máximo (incluido) que puede aparecer en la matriz. Por defecto es 9.

2. cargar_matriz_desde_archivo

cargar_matriz_desde_archivo(self, nombre_archivo: str)
Descripción: Intenta leer y parsear una matriz desde un archivo de texto.

Espera que los valores estén separados por espacios en blanco en el archivo.

Manejo de Errores: Incluye bloques try...except para capturar FileNotFoundError y errores de formato (como filas de distinta longitud).

Si la carga es exitosa, actualiza dinámicamente self.ancho y self.alto con las dimensiones del archivo.

Parámetros:

nombre_archivo (str): La ruta completa o relativa al archivo de texto (.txt) a cargar.

3. dibujar

dibujar(self)
Descripción: Ejecuta el proceso de visualización.

Calcula las dimensiones necesarias de la ventana para centrar la matriz.

Itera sobre cada celda (i, j) en self.matriz_datos.

Asigna el color basado en MAPA_COLORES y llama a _dibujar_pixel para pintar el cuadrado en la posición correcta.

Actualiza la ventana de Turtle (self.ventana.update()) solo una vez al final para asegurar un dibujo rápido.

4. iniciar

iniciar(self)
Descripción: Mantiene abierta la ventana de Turtle Graphics. El programa continuará en ejecución hasta que el usuario haga clic en la ventana de dibujo.

Bloque de Ejecución Principal (if __name__ == "__main__":)
Esta sección define las constantes por defecto y la secuencia de comandos para probar el visualizador:

Se inicializan las constantes de dimensión y el tamaño del píxel.

Se crea una instancia de VisualizadorMatriz.

Se intenta cargar el archivo.

Si la matriz está vacía (la carga falló o el archivo no existe), se llama a generar_matriz_en_memoria.

Se llama a dibujar() para mostrar los resultados.

Se llama a iniciar() para esperar la interacción del usuario.
