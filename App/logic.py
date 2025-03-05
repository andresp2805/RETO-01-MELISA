import time
import csv
import os
import sys
from datetime import datetime
import tabulate as tb


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as sl
from DataStructures.List.list_iterator import iterator


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
    records_return = get_first_last_info(records)
    return funcs["size"](records), records_return

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

def get_first_last_info(records, requerimiento = "carga_datos"):
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
    funcs = get_list_functions(records)
    total = funcs["size"](records)
    new_list_ret = funcs["new_list"]()
    def extract_info(record):
        if requerimiento == "carga_datos":
            return {
                'year_collection': record['year_collection'],
                'load_time': record['load_time'],
                'state_name': record['state_name'],
                'source': record['source'],
                'unit_measurement': record['unit_measurement'],
                'value': record['value']
            }
        elif requerimiento == "req_3":
            dt = datetime.strptime(record['load_time'], "%Y-%m-%d %H:%M:%S")
            return {
                'source': record['source'],
                'year_collection': record['year_collection'],
                'load_time': dt.strftime("%Y-%m-%d"),
                'freq_collection': record['freq_collection'],
                'commodity': record['commodity'],
                'unit_measurement': record['unit_measurement']
            }
        elif requerimiento == "req_4":
            dt = datetime.strptime(record['load_time'], "%Y-%m-%d %H:%M:%S")
            return {
                'source': record['source'],
                'year_collection': record['year_collection'],
                'load_time': dt.strftime("%Y-%m-%d"),
                'freq_collection': record['freq_collection'],
                'state_name': record['state_name'],
                'unit_measurement': record['unit_measurement']
            }
        elif requerimiento == "req_5":
            dt = datetime.strptime(record['load_time'], "%Y-%m-%d %H:%M:%S")
            return {
                'source': record['source'],
                'year_collection': record['year_collection'],
                'load_time': dt.strftime("%Y-%m-%d"),
                'freq_collection': record['freq_collection'],
                'state_name': record['state_name'],
                'unit_measurement': record['unit_measurement'],
                'commodity': record['commodity'],
            }
        elif requerimiento == "req_6":
            dt = datetime.strptime(record['load_time'], "%Y-%m-%d %H:%M:%S")
            return {
                'source': record['source'],
                'year_collection': record['year_collection'],
                'load_time': dt.strftime("%Y-%m-%d"),
                'freq_collection': record['freq_collection'],
                'state_name': record['state_name'],
                'unit_measurement': record['unit_measurement']
            }
        else:
            return {
                'source': record['source'],
                'commodity': record['commodity'],
                'statical_category': record['statical_category'],
                'source': record['source'],
                'unit_measurement': record['unit_measurement'],
                'state_name': record['state_name'],
                'location': record['location'],
                'year_collection': record['year_collection'],
                'freq_collection': record['freq_collection'],
                'reference_period': record['reference_period'],
                'load_time': record['load_time'],
                'value': record['value'],
            }
            
    if total <= 20:
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
def filtrar_por_año(records, anio_inicial, anio_final):
    funcs = get_list_functions(records)
    lista = funcs["new_list"]()
    for registro in iterator(records):
        if anio_inicial <= registro['year_collection'] <= anio_final:
            funcs["add_last"](lista, registro)
    return lista

def filtrar_por_fecha(records, fecha_inicial, fecha_final):
    funcs = get_list_functions(records)
    lista = funcs["new_list"]()
    fecha_i = datetime.strptime(fecha_inicial + " 00:00:00", "%Y-%m-%d %H:%M:%S")
    fecha_f = datetime.strptime(fecha_final + " 23:59:59", "%Y-%m-%d %H:%M:%S")
    for registro in iterator(records):
        fecha_r = datetime.strptime(registro['load_time'], "%Y-%m-%d %H:%M:%S")
        if fecha_i <= fecha_r <= fecha_f:
            funcs["add_last"](lista, registro)
    return lista

def filtrar_por_departamento(records, departamento):
    funcs = get_list_functions(records)
    lista = funcs["new_list"]()
    for registro in iterator(records):
        if registro['state_name'] == departamento:
            funcs["add_last"](lista, registro)
    return lista

def filtrar_por_producto(records, producto):
    funcs = get_list_functions(records)
    lista = funcs["new_list"]()
    for registro in iterator(records):
        if registro['commodity'] == producto:
            funcs["add_last"](lista, registro)
    return lista

def filtrar_por_categoria_estadistica(records, categoria):
    funcs = get_list_functions(records)
    lista = funcs["new_list"]()
    for registro in iterator(records):
        if registro['statical_category'] == categoria:
            funcs["add_last"](lista, registro)
    return lista

def filtrar_por_unidad_de_medida(records):
    funcs = get_list_functions(records)
    lista = funcs["new_list"]()
    for registro in iterator(records):
        if "$" in registro['unit_measurement']:
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
    records_filtrado = filtrar_por_año(records, anio_interes, anio_interes) 
    most_recent_record = None
    max_load_time = float('-inf') 
    for record in iterator(records_filtrado):
        current_timestamp = datetime.strptime(record['load_time'], "%Y-%m-%d %H:%M:%S").timestamp()
        if current_timestamp > max_load_time:
            max_load_time = current_timestamp
            most_recent_record = record    
    if most_recent_record is not None:
        dt = datetime.strptime(most_recent_record['load_time'], "%Y-%m-%d %H:%M:%S")
        record_formateado = {
            'year_collection': str(most_recent_record['year_collection']),
            'load_time': dt.strftime("%Y-%m-%d"),
            'source': most_recent_record['source'],
            'freq_collection': most_recent_record['freq_collection'],
            'state_name': most_recent_record['state_name'],
            'commodity': most_recent_record['commodity'],
            'unit_measurement': most_recent_record['unit_measurement'],
            'value': most_recent_record['value']
        }
    else:
        record_formateado = {
            'year_collection': None,
            'load_time': None,
            'source': None,
            'freq_collection': None,
            'state_name': None,
            'commodity': None,
            'unit_measurement': None,
            'value': None
        }
    end = get_time()
    elapsed = delta_time(start, end)
    return elapsed, funcs["size"](records_filtrado), record_formateado

def req_2(catalog, departamento_interes):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    start = get_time()
    records = catalog['agricultural_records']
    funcs = get_list_functions(records)
    records_filtrado = filtrar_por_departamento(records, departamento_interes)
    most_recent_record = None
    max_load_time = float('-inf') 
    for record in iterator(records_filtrado):
        current_timestamp = datetime.strptime(record['load_time'], "%Y-%m-%d %H:%M:%S").timestamp()
        if current_timestamp > max_load_time:
            max_load_time = current_timestamp
            most_recent_record = record
    if most_recent_record is not None:
        dt = datetime.strptime(most_recent_record['load_time'], "%Y-%m-%d %H:%M:%S")
        record_formateado = {
            'year_collection': str(most_recent_record['year_collection']),
            'load_time': dt.strftime("%Y-%m-%d"),
            'source': most_recent_record['source'],
            'freq_collection': most_recent_record['freq_collection'],
            'state_name': most_recent_record['state_name'],
            'commodity': most_recent_record['commodity'],
            'unit_measurement': most_recent_record['unit_measurement'],
            'value': most_recent_record['value']
        }
    else:
        record_formateado = {
            'year_collection': None,
            'load_time': None,
            'source': None,
            'freq_collection': None,
            'state_name': None,
            'commodity': None,
            'unit_measurement': None,
            'value': None
        }
    end = get_time()
    elapsed = delta_time(start, end)
    return elapsed, funcs["size"](records_filtrado), record_formateado

def req_3(catalog, departamento_interes, anio_inicio, anio_fin):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    start = get_time()
    records = catalog['agricultural_records']
    funcs = get_list_functions(records)
    records_filtrado = filtrar_por_departamento(records, departamento_interes)
    records_filtrado = filtrar_por_año(records_filtrado, anio_inicio, anio_fin)
    num_surveys = 0
    num_census = 0
    for record in iterator(records_filtrado):
        if record['source'] == 'SURVEY':
            num_surveys += 1
        elif record['source'] == 'CENSUS':
            num_census += 1
    records_return = get_first_last_info(records_filtrado, "req_3")
    end = get_time()
    elapsed = delta_time(start, end)
    return elapsed, funcs["size"](records_filtrado), num_surveys, num_census, records_return

def req_4(catalog, tipo_producto, anio_inicio, anio_fin):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    start = get_time()
    records = catalog['agricultural_records']
    funcs = get_list_functions(records)
    records_filtrado = filtrar_por_producto(records, tipo_producto)
    records_filtrado = filtrar_por_año(records_filtrado, anio_inicio, anio_fin)
    num_surveys = 0
    num_census = 0
    for record in iterator(records_filtrado):
        if record['source'] == 'SURVEY':
            num_surveys += 1
        elif record['source'] == 'CENSUS':
            num_census += 1
    records_return = get_first_last_info(records_filtrado, "req_4")
    end = get_time()
    elapsed = delta_time(start, end)
    return elapsed, funcs["size"](records_filtrado), num_surveys, num_census, records_return

def req_5(catalog, categoria_estadistica, anio_inicio, anio_fin):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    start = get_time()
    records = catalog['agricultural_records']
    funcs = get_list_functions(records)
    records_filtrado = filtrar_por_categoria_estadistica(records, categoria_estadistica)
    records_filtrado = filtrar_por_año(records_filtrado, anio_inicio, anio_fin)
    num_surveys = 0
    num_census = 0
    for record in iterator(records_filtrado):
        if record['source'] == 'SURVEY':
            num_surveys += 1
        elif record['source'] == 'CENSUS':
            num_census += 1
    records_return = get_first_last_info(records_filtrado, "req_5")
    end = get_time()
    elapsed = delta_time(start, end)
    return elapsed, funcs["size"](records_filtrado), num_surveys, num_census, records_return

def req_6(catalog, departamento_interes, fecha_inicio, fecha_fin):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    start = get_time()
    records = catalog['agricultural_records']
    funcs = get_list_functions(records)
    records_filtrado = filtrar_por_departamento(records, departamento_interes)
    records_filtrado = filtrar_por_fecha(records_filtrado, fecha_inicio, fecha_fin)
    num_surveys = 0
    num_census = 0
    for record in iterator(records_filtrado):
        if record['source'] == 'SURVEY':
            num_surveys += 1
        elif record['source'] == 'CENSUS':
            num_census += 1
    records_return = get_first_last_info(records_filtrado, "req_6")
    end = get_time()
    elapsed = delta_time(start, end)
    return elapsed, funcs["size"](records_filtrado), num_surveys, num_census, records_return

def req_7(catalog, departamento_interes, anio_inicio, anio_fin):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    start = get_time()
    records = catalog['agricultural_records']
    funcs = get_list_functions(records)
    records_filtrado = filtrar_por_año(records, anio_inicio, anio_fin)
    records_filtrado = filtrar_por_departamento(records_filtrado, departamento_interes)
    records_filtrado = filtrar_por_unidad_de_medida(records_filtrado)
    
    grupos = {}  # clave: año, valor: diccionario con acumulados
    for registro in iterator(records_filtrado):
        anio = registro['year_collection']
        if anio not in grupos:
            grupos[anio] = {
                "income": 0.0,
                "count": 0,
                "invalid": 0,
                "survey": 0,
                "census": 0
            }
        valor_str = registro['value']
        try:
            valor_numerico = float(valor_str.replace(",", "").strip())
            grupos[anio]["income"] += valor_numerico
        except Exception:
            grupos[anio]["invalid"] += 1
        grupos[anio]["count"] += 1
        if registro['source'] == "SURVEY":
            grupos[anio]["survey"] += 1
        elif registro['source'] == "CENSUS":
            grupos[anio]["census"] += 1
    
    if not grupos:
        resultado_max = {
            "year_collection": None,
            "period_type": None,
            "income": None,
            "count": None,
            "invalid": None,
            "survey": None,
            "census": None
        }
        resultado_min = resultado_max.copy()
    else:
        anio_max = max(grupos, key=lambda a: grupos[a]["income"])
        anio_min = min(grupos, key=lambda a: grupos[a]["income"])
        resultado_max = {
                "year_collection": str(anio_max),
                "period_type": "MAYOR",
                "income": grupos[anio_max]["income"],
                "count": grupos[anio_max]["count"],
                "invalid": grupos[anio_max]["invalid"],
                "survey": grupos[anio_max]["survey"],
                "census": grupos[anio_max]["census"]
        }
        resultado_min = {
            "year_collection": str(anio_min),
            "period_type": "MENOR",
            "income": grupos[anio_min]["income"],
            "count": grupos[anio_min]["count"],
            "invalid": grupos[anio_min]["invalid"],
            "survey": grupos[anio_min]["survey"],
            "census": grupos[anio_min]["census"]
        }
    end = get_time()
    elapsed = delta_time(start, end)
    return elapsed, funcs["size"](records_filtrado), resultado_max, resultado_min

def req_8(catalog):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass

