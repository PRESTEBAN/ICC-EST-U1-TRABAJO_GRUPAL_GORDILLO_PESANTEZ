class SortMethods:
    def sortByBubble(self, arreglo):
        arreglo = arreglo.copy()
        n = len(arreglo)
        for i in range(n):
            for j in range(i+1, n):
                  if arreglo[i] > arreglo[j]:
                    arreglo[i],arreglo[j] = arreglo[j],arreglo[i]
        return arreglo
    
    def sortByBubble_enhanced(self, arreglo):
        arreglo = arreglo.copy()
        n = len(arreglo)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1): 
                if arreglo[j] > arreglo[j + 1]:
                    arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]
                    swapped = True
            if not swapped:
                break  
        return arreglo
    
    def sort_seleccion(self, arreglo):
        arreglo = arreglo.copy()
        n = len(arreglo)
        for i in range(n):
            indice_minimo = i
            for j in range(i+1,n):
                 if arreglo[j] < arreglo[indice_minimo]:
                    indice_minimo = j
            arreglo[i], arreglo[indice_minimo] = arreglo[indice_minimo], arreglo[i]
        return arreglo

    def sortByInsertion(self, arreglo):
        arreglo = arreglo.copy()
        n = len(arreglo)
        for i in range(1, n):
            clave = arreglo[i]
            j = i - 1
            while j >= 0 and arreglo[j] > clave:
                arreglo[j + 1] = arreglo[j]
                j -= 1
            arreglo[j + 1] = clave
        return arreglo
    
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


