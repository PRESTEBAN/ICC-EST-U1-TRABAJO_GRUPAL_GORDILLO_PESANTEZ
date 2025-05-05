import time

class Benchmarking:
    def medir_tiempo(func, array):
        inicio = time.time()
        func(array)
        fin = time.time()
        return fin - inicio
    
    