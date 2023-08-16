import time

def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)  # ordenar a metade esquerda
        merge_sort(R)  # ordenar a metade direita

        i = j = k = 0

        # Mescla as metades ordenadas
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Copia os elementos restantes, se tiver
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

if __name__ == "__main__":
    n_values_insert_sort_faster = []

    # Loop para testar valores de 'n' de 0 a 10
    for n in range(0, 100):
        arr = list(range(n, 0, -1))  # Cria uma lista invertida de 0 a 'n' para o pior caso do Insert Sort
        start_time = time.time()
        insert_sort(arr)  # Chama o Insert Sort para ordenar a lista
        insert_sort_time = time.time() - start_time

        arr = list(range(n, 0, -1))  # Reinicia a lista invertida para o Merge Sort
        start_time = time.time()
        merge_sort(arr)  # Chama o Merge Sort para ordenar a lista
        merge_sort_time = time.time() - start_time

        # Compara os tempos de execução dos algoritmos e adiciona 'n' à lista se o Insert Sort for mais rápido
        if insert_sort_time < merge_sort_time:
            n_values_insert_sort_faster.append(n)

    print("Valores em que Insert Sort é mais rápido que o Merge Sort:")
    print(n_values_insert_sort_faster)
