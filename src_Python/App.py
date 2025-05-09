#Relaciona las técnicas de ordenamiento.
#Desarrolla módulos que emplean técnicas de ordenamiento.
import time
import random

# Algoritmos de ordenamiento
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):                           
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def insertion_sort(arr):
    for i in range(1, len(arr)):   
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Generar lista aleatoria
size = 100  # Puedes cambiar el tamaño de la lista
arr = [random.randint(0, 10000) for _ in range(size)]

# Medir tiempo de Bubble Sort
start = time.time()
bubble_sort(arr.copy())
bubble_time = time.time() - start

# Medir tiempo de Insertion Sort
start = time.time()
insertion_sort(arr.copy())
insertion_time = time.time() - start

# Imprimir resultados
print(f"Tamaño de entrada: {size}")
print(f"Tiempo Bubble Sort: {bubble_time:.6f} segundos")
print(f"Tiempo Insertion Sort: {insertion_time:.6f} segundos")