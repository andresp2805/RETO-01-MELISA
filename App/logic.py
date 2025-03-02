import time
import csv
import os
import sys
from datetime import datetime
import tabulate as tb


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as sl
from DataStructures.List import list_node as ln
from DataStructures.List.list_iterator import iterator
from DataStructures.Queue import queue as q
from DataStructures.Stack import stack as s

data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/'

csv.field_size_limit(2147483647)

def get_list_functions(records):
    """
    Dado el objeto 'records' que contiene la lista, retorna un diccionario
    con todas las funciones específicas según el tipo de lista.
    Soporta tanto 'array_list' como 'single_linked_list'.
    """
    list_type = records.get('type', None)
    if list_type == 'array_list':
        return {
            "new_list": al.new_list,
            "is_empty": al.is_empty,
            "size": al.size,
            "add_first": al.add_first,
            "add_last": al.add_last,
            "first_element": al.first_element,
            "last_element": al.last_element,
            "get_element": al.get_element,
            "delete_element": al.delete_element,
            "remove_first": al.remove_first,
            "remove_last": al.remove_last,
            "insert_element": al.insert_element,
            "default_function": al.default_function,
            "is_present": al.is_present,
            "change_info": al.change_info,
            "exchange": al.exchange,
            "sub_list": al.sub_list
        }
    elif list_type == 'single_linked_list':
        return {
            "new_list": sl.new_list,
            "is_empty": sl.is_empty,
            "size": sl.size,
            "add_first": sl.add_first,
            "add_last": sl.add_last,
            "first_element": sl.first_element,
            "last_element": sl.last_element,
            "get_element": sl.get_element,
            "delete_element": sl.delete_element,
            "remove_first": sl.remove_first,
            "remove_last": sl.remove_last,
            "insert_element": sl.insert_element,
            "default_function": sl.default_function,
            "is_present": sl.is_present,
            "change_info": sl.change_info,
            "exchange": sl.exchange,
            "sub_list": sl.sub_list
        }
    else:
        raise TypeError("Tipo de lista no soportado")

# Funciones para medir tiempos de ejecucion
def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return round(elapsed,3)

def new_logic(estructura = "array_list"):
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    #TODO: Llama a las funciónes de creación de las estructuras de datos
    if estructura == "single_linked_list":
        #Inicializar una single_linked_list de registros agrícolas
        agro = {'agricultural_records': sl.new_list()}  
        return agro
    
    if estructura == "array_list":
        #Inicializar una array_list de registros agrícolas
        agro = {'agricultural_records': al.new_list()}  
        return agro
    else:
        raise TypeError("Tipo de lista no soportado")

# Funciones para la carga de datos
def load_data(catalog, filename):
    """
    Carga los datos del reto.
    """
    records = catalog['agricultural_records']
    funcs = get_list_functions(records)
    file_path = data_dir + filename
    with open(file_path, encoding='utf-8') as file:
        input_file = csv.DictReader(file)
        for row in input_file:
            row['year_collection'] = int(row['year_collection'])
            funcs["add_last"](records, row)
    return funcs["size"](records)

def get_min_year(catalog):
    """
    Retorna el menor año de recolección encontrado en la lista de registros.
    """
    lowest = float('inf')
    for i in iterator(catalog['agricultural_records']):
        if i['year_collection'] < lowest:
            lowest = i['year_collection']
    return lowest

def get_max_year(catalog):
    """
    Retorna el mayor año de recolección encontrado en la lista de registros.
    """
    lowest = float('-inf')
    for i in iterator(catalog['agricultural_records']):
        if i['year_collection'] > lowest:
            lowest = i['year_collection']
    return lowest

def get_first_last_info(catalog):
    """
    Retorna una nueva lista (del mismo tipo que la original) que contiene los primeros 5 y 
    los últimos 5 registros con la siguiente información:
      - year_collection: Año de recolección.
      - load_time: Fecha de carga del registro.
      - state_name: Nombre del departamento.
      - source: Fuente/origen (ej. "CENSUS" o "SURVEY").
      - unit_measurement: Unidad de medición (ej. "HEAD", "$", etc.).
      - value: Valor de la medición.
    
    Si la lista original tiene 10 o menos registros, se retornan todos.    
    """
    records = catalog['agricultural_records']
    funcs = get_list_functions(records)
    total = funcs["size"](records)
    new_list_ret = funcs["new_list"]()
    def extract_info(record):
        return {
            'year_collection': record.get('year_collection'),
            'load_time': record.get('load_time'),
            'state_name': record.get('state_name'),
            'source': record.get('source'),
            'unit_measurement': record.get('unit_measurement'),
            'value': record.get('value')
        }
    if total <= 10:
        for i in range(total):
            rec = funcs["get_element"](records, i)
            funcs["add_last"](new_list_ret, extract_info(rec))
    else:
        for i in range(5):
            rec = funcs["get_element"](records, i)
            funcs["add_last"](new_list_ret, extract_info(rec))
        for i in range(total - 5, total):
            rec = funcs["get_element"](records, i)
            funcs["add_last"](new_list_ret, extract_info(rec))
    return new_list_ret

# Funciones de consulta sobre el catálogo
def filtrar_por_año(catalog, anio_inicial, anio_final):
    records = catalog['agricultural_records']
    funcs = get_list_functions(records)
    lista = funcs["new_list"]()
    for registro in iterator(records):
        if anio_inicial <= registro['year_collection'] <= anio_final:
            funcs["add_last"](lista, registro)
    return lista

def filtrar_por_departamento(catalog, departamento):
    records = catalog['agricultural_records']
    funcs = get_list_functions(records)
    lista = funcs["new_list"]()
    for registro in iterator(records):
        if registro['state_name'] == departamento:
            funcs["add_last"](lista, registro)
    return lista
    
def req_1(catalog, anio_interes):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    start = get_time()
    
    records = catalog['agricultural_records']
    funcs = get_list_functions(records)
    records_filtrado = filtrar_por_año(catalog, anio_interes, anio_interes)
    
    most_recent_record = None
    max_load_time = float('-inf') 
    for record in iterator(records_filtrado):
        current_timestamp = datetime.strptime(record['load_time'], "%Y-%m-%d %H:%M:%S").timestamp()
        if current_timestamp > max_load_time:
            max_load_time = current_timestamp
            most_recent_record = record
    
    end = get_time()
    elapsed = delta_time(start, end)
    return elapsed, funcs["size"](records_filtrado), most_recent_record

def req_2(catalog, departamento_interes):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    start = get_time()
    
    records = catalog['agricultural_records']
    funcs = get_list_functions(records)
    records_filtrado = filtrar_por_departamento(catalog, departamento_interes)
    
    most_recent_record = None
    max_load_time = float('-inf') 
    for record in iterator(records_filtrado):
        current_timestamp = datetime.strptime(record['load_time'], "%Y-%m-%d %H:%M:%S").timestamp()
        if current_timestamp > max_load_time:
            max_load_time = current_timestamp
            most_recent_record = record
    
    end = get_time()
    elapsed = delta_time(start, end)
    return elapsed, funcs["size"](records_filtrado), most_recent_record



def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(catalog):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(catalog):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass

