import time
import random

# ---------------------------------------------------------------------------
# Problema A – Insertion sort con métricas
# ---------------------------------------------------------------------------

def insertion_sort_metricas(arr: list) -> tuple:
    arr           = arr.copy()
    n             = len(arr)
    comparaciones = 0
    movimientos   = 0
    inicio        = time.perf_counter()

    for i in range(1, n):
        llave = arr[i]
        j = i - 1

        # El bucle interno
        while j >= 0:
            comparaciones += 1 # Contamos la comparación arr[j] > llave
            if arr[j] > llave:
                arr[j + 1] = arr[j]
                movimientos += 1
                j -= 1
            else:
                # Si falló la condición arr[j] > llave, salimos
                # La comparación ya se contó arriba
                break
        else:
            # Si salimos porque j < 0, contamos esa comparación extra de j >= 0
            # que es la que finalmente rompe el while en el peor caso
            if j < 0:
                comparaciones += 1

        # Colocación final de llave
        arr[j + 1] = llave
        movimientos += 1

    tiempo = time.perf_counter() - inicio
    return (arr, comparaciones, movimientos, tiempo)


# ---------------------------------------------------------------------------
# Problema B – Generación de escenarios
# ---------------------------------------------------------------------------

def generar_arreglo(n: int, escenario: str) -> list:
    if escenario == "mejor":
        return list(range(n))
    elif escenario == "peor":
        return list(range(n, 0, -1))
    elif escenario == "promedio":
        arr = list(range(n))
        random.shuffle(arr)
        return arr
    else:
        raise ValueError("Escenario inválido. Use 'mejor', 'peor' o 'promedio'.")


def medir_escenarios(tamanos: list) -> list:
    resultados = []
    for n in tamanos:
        for escenario in ("mejor", "promedio", "peor"):
            arr = generar_arreglo(n, escenario)
            ordenada, comps, movs, t = insertion_sort_metricas(arr)
            
            resultados.append({
                "tamano": n,
                "escenario": escenario,
                "comparaciones": comps,
                "movimientos": movs,
                "tiempo": t
            })
    return resultados


# ---------------------------------------------------------------------------
# Problema D – Versión híbrida (insertion sort + merge sort)
# ---------------------------------------------------------------------------

def _merge(izq: list, der: list) -> list:
    resultado = []
    i = j = 0
    while i < len(izq) and j < len(der):
        if izq[i] < der[j]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1
    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    return resultado


def _merge_sort_hibrido(arr: list, umbral: int) -> list:
    if len(arr) <= umbral:
        return insertion_sort_metricas(arr)[0]
    
    mid = len(arr) // 2
    izq = _merge_sort_hibrido(arr[:mid], umbral)
    der = _merge_sort_hibrido(arr[mid:], umbral)
    
    return _merge(izq, der)


def insertion_sort_hibrido(arr: list, umbral: int = 32) -> list:
    return _merge_sort_hibrido(arr, umbral)


# ---------------------------------------------------------------------------
if __name__ == "__main__":
    # Prueba estándar de la práctica
    tamanos = [1000, 2000, 4000, 8000]
    print("Midiendo escenarios estándar...\n")
    resultados = medir_escenarios(tamanos)

    print(f"{'Tamaño':>8} {'Escenario':>10} {'Comps':>12} {'Movs':>12} {'Tiempo (s)':>12}")
    print("-" * 65)
    for r in resultados:
        print(f"{r['tamano']:>8} {r['escenario']:>10} {r['comparaciones']:>12} "
              f"{r['movimientos']:>12} {r['tiempo']:>12.4f}")

    # --- PRUEBA EXTRA: PEOR CASO n=16000 ---
    print("\n" + "="*65)
    print("PRUEBA DE ESTRÉS: Peor caso n=16,000")
    print("="*65)
    
    n_extra = 16000
    arr_peor = generar_arreglo(n_extra, "peor")
    _, comps, movs, t = insertion_sort_metricas(arr_peor)
    
    print(f"Resultados para n={n_extra}:")
    print(f"- Comparaciones: {comps}")
    print(f"- Movimientos:   {movs}")
    print(f"- Tiempo total:  {t:.4f} segundos")
    
    # Verificación de la razón de doblamiento
    t_8000 = resultados[-1]['tiempo'] # Último resultado (8000 peor caso)
    razon = t / t_8000
    print(f"- Razón (T_16000 / T_8000): {razon:.2f}")
    print(f"Nota: Si la razón es cercana a 4, se confirma O(n²).")
