import time

class Benchmarking:
    #"Clase que mide los tiempos de ejecución de los algoritmos de ordenamiento."
   
    @staticmethod
    def medir_tiempo(metodo, arreglo):
        #"Mide el tiempo de ejecución sin usar lambda."
        arreglo_copia = arreglo.copy()
        inicio = time.perf_counter()
        metodo(arreglo_copia)  # Llamada directa al método
        fin = time.perf_counter()
        return (fin - inicio)
