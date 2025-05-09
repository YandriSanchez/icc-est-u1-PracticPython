import time
import matplotlib.pyplot as plt
import random


 
# Algoritmos de ordenamiento
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

# Medir tiempos de ejecución
sizes = [100, 500, 1000, 5000]
bubble_times = []
insertion_times = []

for size in sizes:
    arr = [random.randint(0, 10000) for _ in range(size)]
    
    start = time.time()
    bubble_sort(arr.copy())
    bubble_times.append(time.time() - start)
    
    start = time.time()
    insertion_sort(arr.copy())
    insertion_times.append(time.time() - start)

# Graficar resultados
plt.plot(sizes, bubble_times, label="Bubble Sort", marker="o")
plt.plot(sizes, insertion_times, label="Insertion Sort", marker="s")
plt.xlabel("Tamaño de entrada")
plt.ylabel("Tiempo de ejecución (s)")
plt.title("Comparación de Algoritmos de Ordenamiento")
plt.legend()
plt.show()