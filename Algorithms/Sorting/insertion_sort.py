def insertion_sort(lst, sort_crit):
    """
    Ordena la lista 'lst' usando el algoritmo Insertion Sort.
    
    Parámetros:
      lst: Lista a ordenar. Debe ser un diccionario con la estructura:
           {'size': int, 'first': ..., 'last': ..., 'type': 'array_list' o 'single_linked_list'}.
      sort_crit: Función de comparación que recibe dos elementos y retorna True
                 si el primer elemento es menor que el segundo.
    
    Retorna:
      La misma lista 'lst', ordenada de forma ascendente según sort_crit.
    
    Ejemplo de uso:
      def less_than(a, b):
          return a < b
      sorted_lst = insertion_sort(my_list, less_than)
    """
    if lst['type'] == 'array_list':
        from DataStructures.List import array_list as lt
    elif lst['type'] == 'single_linked_list':
        from DataStructures.List import single_linked_list as lt
    else:
        raise ValueError("Tipo de lista no soportado. Se esperaba 'array_list' o 'single_linked_list'.")
    n = lt.size(lst)
    for i in range(1, n):
        j = i
        while j > 0 and sort_crit(lt.get_element(lst, j), lt.get_element(lst, j-1)):
            lt.exchange(lst, j, j-1)
            j -= 1
    return lst
