import time
import random
n=8000 #Se cambian los valores por 1000, 2000,4000 y 8000 según el caso
def insertion_sort_metricas(arr_in: list[int]):
    """Regresa (arreglo_ordenado, comparaciones, movimientos, tiempo_segundos)."""
    # 1. Creamos una copia para no alterar la lista original
    arr = arr_in.copy()
    
    # 2. Inicializamos contadores DENTRO de la función
    comparaciones = 0
    movimientos = 0
    
    inicio = time.perf_counter()
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0:
            comparaciones += 1  
            if arr[j] > key:
                arr[j + 1] = arr[j]
                movimientos += 1
                j -= 1
            else:
                break
        arr[j + 1] = key
        movimientos += 1
    fin = time.perf_counter()
    tiempo = fin - inicio
    
    
    return arr, comparaciones, movimientos, tiempo
promedio = [random.randint(0, n) for _ in range(n)]
peor = list(range(n, 0, -1))
mejor=list(range(n))
ordenada, comps, movs, t = insertion_sort_metricas(peor)#Se coloca mejor,promedio o peor según el caso

print(f"Lista Ordenada: {ordenada}")
print(f"Comparaciones: {comps}")
print(f"Movimientos: {movs}")
print(f"Tiempo: {t:.6f} segundos")
