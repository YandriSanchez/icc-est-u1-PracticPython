class SorthMethods:
    #"Método de ordenamiento Burbuja"
    def sortByBubble(self,arreglo):
        arreglo = arreglo.copy()
        n = len(arreglo)
        for i in range(n - 1):  
            for j in range(n - i - 1):  
                if arreglo[j] > arreglo[j + 1]:
                    arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j] 
        return arreglo
    #"Método de ordenamiento Burbuja Mejorado"
    def sortByBubbleOptimized(self, arreglo):
        arreglo = arreglo.copy()
        n = len(arreglo)
        for i in range(n - 1):
            swapped = False
            for j in range(n - i - 1):
                if arreglo[j] > arreglo[j + 1]:
                    arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]
                    cambio = True
            if not cambio:
                break  
        return arreglo
    #"Método de ordenamiento de Seleccion"
    def sortBySelection(self,arreglo):
        arreglo = arreglo.copy()
        n = len(arreglo)
        for i in range(n-1):
            minIndex = i
            for j in range(i+1,n):
                if arreglo[j] < arreglo[minIndex]:
                    minIndex = j
            arreglo[minIndex], arreglo[i] = arreglo[i], arreglo[minIndex]
        return arreglo
    #"Método de ordenamiento de Insercion"
    def sortByInsertion(self, arreglo):
        arreglo = arreglo.copy()
        n = len(arreglo)
        for i in range(1, n):
            key = arreglo[i]
            j = i - 1
            while j >= 0 and arreglo[j] > key:
                arreglo[j + 1] = arreglo[j]
                j -= 1
            arreglo[j + 1] = key
        return arreglo
    #"Método de ordenamiento Shell"
    def sortByShell(self, arreglo):
        arreglo = arreglo.copy()
        n = len(arreglo)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = arreglo[i]
                j = i
                while j >= gap and arreglo[j - gap] > temp:
                    arreglo[j] = arreglo[j - gap]
                    j -= gap
                arreglo[j] = temp
            gap //= 2
        return arreglo

        