import turtle
import random
from typing import List, Dict, Optional

class VisualizadorMatriz:
    """
    Una clase para generar o cargar una matriz de números y visualizarla
    usando Turtle Graphics.
    """
    
    MAPA_COLORES: Dict[str, str] = {
        '0': '#2c3e50', '1': '#3498db', '2': '#2ecc71', '3': '#e74c3c',
        '4': '#f1c40f', '5': '#9b59b6',  # <-- CORRECCIÓN: Se eliminó un ':' extra aquí
        '6': '#e67e22', '7': '#1abc9c',
        '8': '#d35400', '9': '#bdc3c7'
    }

    def __init__(self, ancho_default: int, alto_default: int, tamaño_pixel: int = 7):
        self.ancho = ancho_default
        self.alto = alto_default
        self.tamaño_pixel = tamaño_pixel
        self.matriz_datos: List[List[str]] = []

        self.ventana = turtle.Screen()
        self.tortuga = turtle.Turtle()
        self._configurar_lienzo()

    def _configurar_lienzo(self):
        self.ventana.title("🎨 Visualizador de Matriz Corregido 🐢")
        self.ventana.tracer(0)
        self.tortuga.speed(0)
        self.tortuga.hideturtle()
        self.tortuga.penup()

    def generar_matriz_en_memoria(self, max_num: int = 9):
        print("🔧 Generando matriz aleatoria en memoria...")
        self.matriz_datos = [
            [str(random.randint(0, max_num)) for _ in range(self.ancho)]
            for _ in range(self.alto)
        ]
        print(f"✅ Matriz de {self.alto}x{self.ancho} generada.")

    def cargar_matriz_desde_archivo(self, nombre_archivo: str):
        print(f"🔍 Buscando archivo '{nombre_archivo}'...")
        try:
            with open(nombre_archivo, 'r') as f:
                matriz_temp = [linea.strip().split() for linea in f if linea.strip()]
            
            if not matriz_temp:
                print("ℹ️ Archivo encontrado pero está vacío.")
                return

            primer_fila_len = len(matriz_temp[0])
            if not all(len(fila) == primer_fila_len for fila in matriz_temp):
                print("❌ Error: Las filas en el archivo no tienen la misma longitud.")
                return

            self.matriz_datos = matriz_temp
            self.alto = len(self.matriz_datos)
            self.ancho = len(self.matriz_datos[0])
            print(f"✅ Matriz de {self.alto}x{self.ancho} cargada desde '{nombre_archivo}'.")

        except FileNotFoundError:
            print(f"ℹ️ Archivo '{nombre_archivo}' no encontrado.")
        except Exception as e:
            print(f"❌ Ocurrió un error inesperado al leer el archivo: {e}")

    def _dibujar_pixel(self, x: float, y: float, color: str):
        self.tortuga.goto(x, y)
        self.tortuga.pendown()
        self.tortuga.color(color)
        self.tortuga.begin_fill()
        for _ in range(4):
            self.tortuga.forward(self.tamaño_pixel)
            self.tortuga.right(90)
        self.tortuga.end_fill()
        self.tortuga.penup()

    def dibujar(self):
        if not self.matriz_datos:
            print("⚠️ No hay datos en la matriz para dibujar. Finalizando.")
            return

        print("🚀 Empezando a dibujar...")
        ancho_ventana = self.ancho * self.tamaño_pixel + 50
        alto_ventana = self.alto * self.tamaño_pixel + 50
        self.ventana.setup(width=ancho_ventana, height=alto_ventana)

        start_x = - (self.ancho * self.tamaño_pixel) / 2
        start_y = (self.alto * self.tamaño_pixel) / 2

        for i, fila in enumerate(self.matriz_datos):
            for j, valor_str in enumerate(fila):
                color = self.MAPA_COLORES.get(valor_str, '#7f8c8d')
                self._dibujar_pixel(start_x + j * self.tamaño_pixel, start_y - i * self.tamaño_pixel, color)
        
        self.ventana.update()
        print("✨ ¡Dibujo completado!")

    def iniciar(self):
        if self.matriz_datos:
            self.ventana.exitonclick()


if __name__ == "__main__":
    ANCHO_DEFAULT = 100
    ALTO_DEFAULT = 100
    TAMAÑO_PIXEL = 7
    
    # ⚠️ Modifica esta línea para usar la ruta completa
    NOMBRE_ARCHIVO_OPCIONAL = r"C:\Users\PC FERRET\Documents\Graficacion\p3\matriz.txt"
    
    visualizador = VisualizadorMatriz(ANCHO_DEFAULT, ALTO_DEFAULT, TAMAÑO_PIXEL)
    visualizador.cargar_matriz_desde_archivo(NOMBRE_ARCHIVO_OPCIONAL)
    
    if not visualizador.matriz_datos:
        print("➡️ No se cargó una matriz válida. Se procederá a generar una aleatoria.")
        visualizador.generar_matriz_en_memoria()

    visualizador.dibujar()
    visualizador.iniciar()