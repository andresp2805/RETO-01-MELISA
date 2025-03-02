def new_list():
    """
    Crea una lista de tipo array_list vacía.
    Returns:
        dict: Un diccionario con dos llaves:
              - 'size': 0
              - 'elements': []
    """
    return {
        'size': 0,
        'elements': [],
        'type': 'array_list'
    }
    
def is_empty(my_list):
    """
    Verifica si la lista está vacía.
    Parameters:
        my_list (dict): Estructura array_list con llaves 'size' y 'elements'.
                        Ejemplo:
                        {
                            'size': 0,
                            'elements': []
                        }
    Returns:
        bool: True si la lista está vacía, False en caso contrario.
    """
    return my_list['size'] == 0

def size(my_list):
    """
    Retorna el tamaño de la lista.
    Parameters:
        my_list (dict): Estructura array_list con llaves 'size' y 'elements'.
                        Ejemplo:
                        {
                            'size': 0,
                            'elements': []
                        }
    Returns:
        int: Tamaño de la lista (número de elementos).
    """
    return my_list['size']

def add_first(my_list, element):
    """
    Agrega un elemento al inicio de la lista (array_list) y 
    actualiza el tamaño de la lista en 1.
    Parameters:
        my_list (dict): Estructura array_list con llaves 'size' y 'elements'.
                        Ejemplo:
                        {
                            'size': 0,
                            'elements': []
                        }
        element (any): Elemento a agregar al inicio de la lista.
    Returns:
        dict: La lista (array_list) con el elemento agregado al inicio.
    """
    my_list['elements'].insert(0, element)
    my_list['size'] += 1
    return my_list

def add_last(my_list, element):
    """
    Agrega un elemento al final de la lista (array_list) y 
    actualiza el tamaño de la lista en 1.
    Parameters:
        my_list (dict): Estructura array_list con llaves 'size' y 'elements'.
                        Ejemplo:
                        {
                            'size': 0,
                            'elements': []
                        }
        element (any): Elemento a agregar al final de la lista.
    Returns:
        dict: La lista (array_list) con el elemento agregado al final.
    """
    my_list['elements'].append(element)
    my_list['size'] += 1
    return my_list

def first_element(my_list):
    """
    Retorna el primer elemento de una lista no vacía.
    Si la lista está vacía, lanza un IndexError: "list index out of range".
    Parameters:
        my_list (dict): Estructura array_list con llaves 'size' y 'elements'.
                        Ejemplo:
                        {
                            'size': 0,
                            'elements': []
                        }
    
    Returns:
        any: El primer elemento de la lista.
    
    Raises:
        IndexError: Si la lista está vacía.
    """
    if my_list['size'] == 0:
        raise IndexError("list index out of range")
    return my_list['elements'][0]

def last_element(my_list):
    """
    Retorna el último elemento de una lista no vacía.
    Si la lista está vacía, lanza un IndexError: "list index out of range".
    Parameters:
        my_list (dict): Estructura array_list con llaves 'size' y 'elements'.
                        Ejemplo:
                        {
                            'size': 0,
                            'elements': []
                        }
    Returns:
        any: El último elemento de la lista.
    Raises:
        IndexError: Si la lista está vacía.
    """
    if my_list['size'] == 0:
        raise IndexError("list index out of range")
    return my_list['elements'][-1]

def get_element(my_list, pos):
    """
    Retorna el elemento en la posición dada.
    La posición 'pos' debe ser >= 0 y < size(my_list).
    Parameters:
        my_list (dict): Estructura array_list con llaves 'size' y 'elements'.
                        Ejemplo:
                        {
                            'size': 0,
                            'elements': []
                        }
        pos (int): Posición del elemento a retornar.
    Returns:
        any: El elemento en la posición 'pos'.
    Raises:
        IndexError: Si la posición es inválida (pos < 0 o pos >= my_list['size']).
    """
    if pos < 0 or pos >= my_list['size']:
        raise IndexError("list index out of range")
    return my_list['elements'][pos]

def delete_element(my_list, pos):
    """
    Elimina el elemento en la posición 'pos' de la lista (array_list).
    La posición 'pos' debe ser >= 0 y < my_list['size'].
    Parameters:
        my_list (dict): Estructura array_list con llaves 'size' y 'elements'.
                        Ejemplo:
                        {
                            'size': 0,
                            'elements': []
                        }
        pos (int): Posición del elemento a eliminar.

    Returns:
        dict: La lista (array_list) actualizada.
    Raises:
        IndexError: Si la posición es inválida (pos < 0 o pos >= my_list['size']).
    """
    if pos < 0 or pos >= my_list['size']:
        raise IndexError("list index out of range")
    my_list['elements'].pop(pos)
    my_list['size'] -= 1    
    return my_list

def remove_first(my_list):
    """
    Elimina el primer elemento de la lista (array_list) y disminuye
    el tamaño de la lista en 1. Retorna el elemento eliminado.
    Si la lista está vacía, lanza un IndexError: "list index out of range".
    Parameters:
        my_list (dict): Estructura array_list con llaves 'size' y 'elements'.
                        Ejemplo:
                        {
                            'size': 0,
                            'elements': []
                        }
    Returns:
        any: El elemento que se ha eliminado de la lista.
    Raises:
        IndexError: Si la lista está vacía.
    """
    if my_list['size'] == 0:
        raise IndexError("list index out of range")
    element = my_list['elements'].pop(0)
    my_list['size'] -= 1
    return element

def remove_last(my_list):
    """
    Elimina el último elemento de la lista (array_list) y disminuye
    el tamaño de la lista en 1. Retorna el elemento eliminado.
    Si la lista está vacía, lanza un IndexError: "list index out of range".
    Parameters:
        my_list (dict): Estructura array_list con llaves 'size' y 'elements'.
                        Ejemplo:
                        {
                            'size': 0,
                            'elements': []
                        }
    Returns:
        any: El elemento que se ha eliminado de la lista.
    Raises:
        IndexError: Si la lista está vacía.
    """
    if my_list['size'] == 0:
        raise IndexError("list index out of range")    
    element = my_list['elements'].pop()
    my_list['size'] -= 1
    return element

def insert_element(my_list, element, pos):
    """
    Inserta un elemento en la posición 'pos' de la lista (array_list).
    Aumenta el tamaño de la lista en 1.
    Si la posición es inválida (pos < 0 o pos > my_list['size']), 
    lanza un IndexError: "list index out of range".
    Parameters:
        my_list (dict): Estructura array_list con llaves 'size' y 'elements'.
                        Ejemplo:
                        {
                            'size': 0,
                            'elements': []
                        }
        element (any): Elemento a insertar en la lista.
        pos (int): Posición en la cual se insertará el elemento.
    Returns:
        dict: La lista (array_list) actualizada.
    Raises:
        IndexError: Si la posición es inválida.
    """
    if pos < 0 or pos > my_list['size']:
        raise IndexError("list index out of range")
    my_list['elements'].insert(pos, element)
    my_list['size'] += 1
    return my_list

def default_function(element_1, element_2):
    """
    Función de comparación por defecto.
    
    Retorna:
      0 si element_1 == element_2
      1 si element_1 > element_2
     -1 si element_1 < element_2
    Parameters:
        element_1 (any): Primer elemento a comparar.
        element_2 (any): Segundo elemento a comparar.

    Returns:
        int: El resultado de la comparación (1, 0, -1).
    """
    if element_1 > element_2:
        return 1
    elif element_1 < element_2:
        return -1
    else:
        return 0

def is_present(my_list, element, cmp_function):
    """
    Verifica si un elemento está presente en la lista.
    Para comparar los elementos, se utiliza la función de comparación cmp_function. 
    Si el elemento está presente, retorna su posición, en caso contrario retorna -1.
    Parameters:
        my_list (dict): Estructura array_list con llaves 'size' y 'elements'.
                        Ejemplo:
                        {
                            'size': 0,
                            'elements': []
                        }
        element (any): Elemento a buscar en la lista.
        cmp_function (function): Función de comparación que recibe dos elementos y
                                 retorna:
                                    - 0 si son iguales
                                    - 1 si el primero es mayor
                                    - -1 si el primero es menor
    Returns:
        int: Posición del elemento si está presente, -1 en caso contrario.
    """
    for i in range(my_list['size']):
        if cmp_function(my_list['elements'][i], element) == 0:
            return i
    return -1

def change_info(my_list, pos, new_info):
    """
    Cambia la información de un elemento en la posición 'pos' por 'new_info'.
    Si la posición es inválida, lanza un IndexError: "list index out of range".
    Parameters:
        my_list (dict): Estructura array_list con llaves 'size' y 'elements'.
                        Ejemplo:
                        {
                            'size': 0,
                            'elements': []
                        }
        pos (int): Posición del elemento a modificar.
        new_info (any): Nueva información para reemplazar el elemento en 'pos'.   
    Returns:
        dict: La lista (array_list) actualizada.  
    Raises:
        IndexError: Si la posición es inválida (pos < 0 o pos >= my_list['size']).
    """
    if pos < 0 or pos >= my_list['size']:
        raise IndexError("list index out of range")
    my_list['elements'][pos] = new_info
    return my_list

def exchange(my_list, pos_1, pos_2):
    """
    Intercambia la información de dos elementos en las posiciones pos_1 y pos_2.
    Si alguna de las posiciones es inválida (pos_1 < 0, pos_2 < 0,
    pos_1 >= my_list['size'] o pos_2 >= my_list['size']), lanza un IndexError:
    "list index out of range".
    Parameters:
        my_list (dict): Estructura array_list con llaves 'size' y 'elements'.
                        Ejemplo:
                        {
                            'size': 0,
                            'elements': []
                        }
        pos_1 (int): Posición del primer elemento a intercambiar.
        pos_2 (int): Posición del segundo elemento a intercambiar.
    Returns:
        dict: La lista (array_list) con la información de los elementos intercambiada.
    Raises:
        IndexError: Si pos_1 o pos_2 es inválido.
    """
    if (pos_1 < 0 or pos_1 >= my_list['size']) or (pos_2 < 0 or pos_2 >= my_list['size']):
        raise IndexError("list index out of range")
    temp = my_list['elements'][pos_1]
    my_list['elements'][pos_1] = my_list['elements'][pos_2]
    my_list['elements'][pos_2] = temp
    return my_list

def sub_list(my_list, pos_i, num_elements):
    """
    Retorna una sublista de la lista original que inicia en la posición pos_i 
    y contiene num_elements elementos.
    Si pos_i < 0 o pos_i >= my_list['size'], lanza IndexError: "list index out of range".
    Si pos_i + num_elements > my_list['size'], también lanza IndexError, 
    pues no hay suficientes elementos para formar la sublista solicitada.
    Parameters:
        my_list (dict): Estructura array_list con llaves 'size' y 'elements'.
                        Ejemplo:
                        {
                            'size': 4,
                            'elements': [1, 2, 3, 4]
                        }
        pos_i (int): Posición inicial de la sublista.
        num_elements (int): Número de elementos a tomar desde pos_i.
    Returns:
        dict: Un nuevo array_list con la sublista solicitada.
    Raises:
        IndexError: Si la posición inicial es inválida o 
                    si pos_i + num_elements excede el tamaño de la lista.
    """
    if pos_i < 0 or pos_i >= my_list['size']:
        raise IndexError("list index out of range")
    if pos_i + num_elements > my_list['size']:
        raise IndexError("list index out of range")
    sub_elements = my_list['elements'][pos_i : pos_i + num_elements]
    new_list = {
        'size': num_elements,
        'elements': sub_elements,
        'type': 'array_list'
    }
    return new_list
