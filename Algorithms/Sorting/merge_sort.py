def merge_sort(lst, sort_crit):
    """
    Ordena la lista 'lst' usando el algoritmo Merge Sort.

    Parámetros:
      lst: Lista a ordenar. Debe ser un diccionario con la estructura
           {'size': int, 'first': ..., 'last': ..., 'type': 'array_list' o 'single_linked_list'}.
      sort_crit: Función de comparación que recibe dos elementos y retorna True
                 si el primer elemento es menor que el segundo (criterio de ordenación ascendente).

    Retorna:
      La misma lista 'lst', ordenada de forma ascendente según sort_crit.

    Ejemplo de uso:
      def less_than(a, b):
          return a < b
      sorted_lst = merge_sort(my_list, less_than)
    """
    if lst['type'] == 'array_list':
        from DataStructures.List import array_list as lt
    elif lst['type'] == 'single_linked_list':
        from DataStructures.List import single_linked_list as lt
    else:
        raise ValueError("Tipo de lista no soportado. Se esperaba 'array_list' o 'single_linked_list'.")
    n = lt.size(lst)
    if n > 1:
        mid = n // 2
        left_list = lt.sub_list(lst, 0, mid)
        right_list = lt.sub_list(lst, mid, n - mid)
        merge_sort(left_list, sort_crit)
        merge_sort(right_list, sort_crit)
        i = j = k = 0
        left_size = lt.size(left_list)
        right_size = lt.size(right_list)
        while i < left_size and j < right_size:
            if sort_crit(lt.get_element(right_list, j), lt.get_element(left_list, i)):
                lt.change_info(lst, k, lt.get_element(right_list, j))
                j += 1
            else:
                lt.change_info(lst, k, lt.get_element(left_list, i))
                i += 1
            k += 1
        while i < left_size:
            lt.change_info(lst, k, lt.get_element(left_list, i))
            i += 1
            k += 1
        while j < right_size:
            lt.change_info(lst, k, lt.get_element(right_list, j))
            j += 1
            k += 1
    return lst
