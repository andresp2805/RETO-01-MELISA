def quick_sort(lst, sort_crit):
    """
    Ordena la lista 'lst' usando el algoritmo Quick Sort.
    
    Parámetros:
      lst: Lista a ordenar. Debe ser un diccionario con la estructura
           {'size': int, 'first': ..., 'last': ..., 'type': 'array_list' o 'single_linked_list'}.
      sort_crit: Función de comparación que recibe dos elementos y retorna True
                 si el primer elemento es menor que el segundo.
                 
    Retorna:
      La misma lista 'lst', ordenada de forma ascendente según sort_crit.
      
    Ejemplo de uso:
      def less_than(a, b):
          return a < b
      sorted_lst = quick_sort(lst, less_than)
    """
    if lst['type'] == 'array_list':
        from DataStructures.List import array_list as lt
    elif lst['type'] == 'single_linked_list':
        from DataStructures.List import single_linked_list as lt
    else:
        raise ValueError("Tipo de lista no soportado. Se esperaba 'array_list' o 'single_linked_list'.")
    def partition(lo, hi):
        """
        Reorganiza los elementos entre los índices lo y hi usando el elemento en hi como pivot.
        Devuelve la posición final del pivot.
        """
        follower = lo
        pivot = lt.get_element(lst, hi)
        for leader in range(lo, hi):
            if sort_crit(lt.get_element(lst, leader), pivot):
                lt.exchange(lst, follower, leader)
                follower += 1
        lt.exchange(lst, follower, hi)
        return follower
    def quicksort(lo, hi):
        if lo < hi:
            pivot_index = partition(lo, hi)
            quicksort(lo, pivot_index - 1)
            quicksort(pivot_index + 1, hi)
    n = lt.size(lst)
    if n > 0:
        quicksort(0, n - 1)
    return lst
