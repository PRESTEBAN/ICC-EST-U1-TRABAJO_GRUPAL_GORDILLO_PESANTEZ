
import random

from benchmarking import Benchmarking
from sortmethods import SortMethods
import matplotlib.pyplot as plt

class App:
    def __init__(self):
        self.tamanos = [5000, 10000, 30000,50000,100000]
        self.max_tamano = max(self.tamanos)
        self.arreglo_base = self.build_arreglo(self.max_tamano)
        self.algoritmos = {
            "Burbuja": SortMethods().sortByBubble,
            "Burbuja Mejorada": SortMethods().sortByBubble_enhanced,
            "Selección": SortMethods().sort_seleccion,
            "Insercion": SortMethods().sortByInsertion,
            "Shell": SortMethods().sortByShell,
        }
        self.resultados = []

    def build_arreglo(self, tamano: int):
        array = []
        for i in range(tamano):
            numero = random.randint(0, 99999)
            array.append(numero)
        return array

    def main(self):
        for tam in self.tamanos:
            arreglo = self.arreglo_base[:tam]
            for nombre, funcion in self.algoritmos.items():
                arreglo_a_usar = arreglo.copy()
                tiempo = Benchmarking.medir_tiempo(funcion, arreglo_a_usar)
                self.resultados.append((tam, nombre, tiempo))

        for tam, nombre, tiempo in self.resultados:
            print(f"Tamano: {tam}, Algoritmo: {nombre}, Tiempo: {tiempo:.6f} segundos")
            
    def graficar_resultados(self):
    
        resultados_por_algoritmo = {}

        for tam, nombre, tiempo in self.resultados:
            if nombre not in resultados_por_algoritmo:
                resultados_por_algoritmo[nombre] = {"tamanos": [], "tiempos": []}
            resultados_por_algoritmo[nombre]["tamanos"].append(tam)
            resultados_por_algoritmo[nombre]["tiempos"].append(tiempo)

        for nombre, datos in resultados_por_algoritmo.items():
            plt.plot(datos["tamanos"], datos["tiempos"], label=nombre)

        plt.title("Comparación de algoritmos de ordenamiento")
        plt.xlabel("Tamaño del arreglo")
        plt.ylabel("Tiempo de ejecución (s)")
        plt.legend()
        plt.grid(True)
        plt.show()
            

if __name__ == "__main__":
    app = App()
    app.main()