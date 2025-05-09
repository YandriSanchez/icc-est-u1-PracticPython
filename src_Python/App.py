from Benchmarking import Benchmarking
from SorthMethods import SorthMethods
import matplotlib.pyplot as plt
import random

class App:
    
    def __init__(self):
        self.sizes = [5000, 10000, 30000, 50000, 100000]
        self.base_array = [random.randint(1, 1000000) for _ in range(max(self.sizes))]
        self.primeros_10 = self.base_array[:10]  # Mantener los primeros 10 números fijos
        self.metodosOrden = SorthMethods()
        self.methods = {
            "Burbuja": self.metodosOrden.sortByBubble,
            "Burbuja Mejorado": self.metodosOrden.sortByBubbleOptimized,
            "Selección": self.metodosOrden.sortBySelection,
            "Inserción": self.metodosOrden.sortByInsertion,
            "Shell": self.metodosOrden.sortByShell
        }
        self.resultados = []
    def ejecutar_pruebas(self):
        #"Ejecuta los algoritmos de ordenamiento y mide los tiempos de ejecución."
        for tam in self.sizes:
            arreglo_base = self.primeros_10 + self.base_array[10:tam]

            for nombre, metodo in self.methods.items():
                tiempo = Benchmarking.medir_tiempo(metodo, arreglo_base)
                self.resultados.append((tam, nombre, tiempo))
                print(f"Tamaño: {tam}, Método: {nombre}, Tiempo: {tiempo:.6f} segundos")
    def ejecutar_pruebas(self):
        #"Imprime los arreglos generados antes de ordenarlos."
        for tam in self.sizes:
            arreglo_base = self.primeros_10 + self.base_array[10:tam]

            print(f"\nTamaño: {tam}, Arreglo generado:")
            print(arreglo_base) 
                
if __name__ == "__main__":
    app = App()
    app.ejecutar_pruebas()