import sys
import os
import tabulate as tb

default_limit=1000
sys.setrecursionlimit(default_limit*10)

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from DataStructures.List.list_iterator import iterator

from App import logic

def new_logic(estructura):
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función de la lógica donde se crean las estructuras de datos
    return logic.new_logic(estructura)

def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8 (Bono)")
    print("0- Salir")
    
def definir_estructura():
    print("Cargando información de los archivos ....\n")
    print("Escoja la estructura para cargar los datos")
    print("1- Array List")
    print("2- Single Linked List")
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs) == 1:
        return "array_list"
    elif int(inputs) == 2:
        return "single_linked_list"
    else:
        print("Opción errónea, vuelva a elegir.\n")
        definir_estructura()
        
def seleccionar_archivo():
    print("Cargando información de los archivos ....\n")
    print("Escoja el archivo a cargar")
    print("1- agricultural-20.csv")
    print("2- agricultural-40.csv")
    print("3- agricultural-60.csv")
    print("4- agricultural-80.csv")
    print("5- agricultural-100.csv")
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs) == 1:
        return "/agricultural-20.csv"
    elif int(inputs) == 2:
        return "/agricultural-40.csv"
    elif int(inputs) == 3:
        return "/agricultural-60.csv"
    elif int(inputs) == 4:
        return "/agricultural-80.csv"
    elif int(inputs) == 5:
        return "/agricultural-100.csv"
    else:
        print("Opción errónea, vuelva a elegir.\n")
        seleccionar_archivo()

def load_data(control, archivo):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    size_control, records_recortado = logic.load_data(control, archivo)
    menor_año = logic.get_min_year(control)
    mayor_año = logic.get_max_year(control)
    print()
    print("INICIANDO LA CARGA DE DATOS")
    print("========================================================================================================")
    print("SE CARGARON LOS DATOS CORRECTAMENTE")
    print("Cantidad de registros cargados: ", size_control)
    print("Año más antiguo de recolección de registros: ", menor_año)
    print("Año más reciente de recolección de registros: ", mayor_año)
    print(tb.tabulate(iterator(records_recortado), headers= 'keys' , tablefmt= "fancy_grid"))
    print()

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    anio = int(input("Ingrese el año a buscar: "))
    time, size, record_formateado = logic.req_1(control, anio)
    print()
    print("========================================================================================================")
    print("Tiempo de ejecución en ms: ", time)
    print(f"Cantidad de registros encontrados en el año {anio}: ", size)
    print("ULTIMO REGISTRO RECOPILADO")
    print(tb.tabulate([record_formateado], headers= 'keys' , tablefmt= "fancy_grid"))
    print()

def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    departamento = input("Ingrese el departamento a buscar: ")
    time, size, record_formateado = logic.req_2(control, departamento)
    print()
    print("========================================================================================================")
    print("Tiempo de ejecución en ms: ", time)
    print(f"Cantidad de registros encontrados en el departamento {departamento}: ", size)
    print("ULTIMO REGISTRO RECOPILADO")
    print(tb.tabulate([record_formateado], headers= 'keys' , tablefmt= "fancy_grid"))
    print()

def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    departamento = input("Ingrese el departamento a buscar: ")
    anio_i = int(input("Ingrese el año inicial del periodo a consultar: "))
    anio_f = int(input("Ingrese el año final del periodo a consultar: "))
    time, size, num_surveys, num_census, records_return = logic.req_3(control, departamento, anio_i, anio_f)
    print()
    print("========================================================================================================")
    print("Tiempo de ejecución en ms: ", time)
    print(f"Cantidad de registros encontrados en el departamento {departamento} entre los años {anio_i} y {anio_f}: ", size)
    print(f"Cantidad de registros de tipo 'SURVEY' encontrados en el departamento {departamento} entre los años {anio_i} y {anio_f}: ", num_surveys)
    print(f"Cantidad de registros de tipo 'CENSUS' encontrados en el departamento {departamento} entre los años {anio_i} y {anio_f}: ", num_census)
    print("RESUMEN DE REGISTROS ENCONTRADOS")
    print(tb.tabulate(iterator(records_return), headers= 'keys' , tablefmt= "fancy_grid"))
    print()

def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    producto = input("Ingrese el producto a buscar: ")
    anio_i = int(input("Ingrese el año inicial del periodo a consultar: "))
    anio_f = int(input("Ingrese el año final del periodo a consultar: "))
    time, size, num_surveys, num_census, records_return = logic.req_4(control, producto, anio_i, anio_f)
    print()
    print("========================================================================================================")
    print("Tiempo de ejecución en ms: ", time)
    print(f"Cantidad de registros encontrados en el producto {producto} entre los años {anio_i} y {anio_f}: ", size)
    print(f"Cantidad de registros de tipo 'SURVEY' encontrados en el producto {producto} entre los años {anio_i} y {anio_f}: ", num_surveys)
    print(f"Cantidad de registros de tipo 'CENSUS' encontrados en el producto {producto} entre los años {anio_i} y {anio_f}: ", num_census)
    print("RESUMEN DE REGISTROS ENCONTRADOS")
    print(tb.tabulate(iterator(records_return), headers= 'keys' , tablefmt= "fancy_grid"))
    print()


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    categoria_estadística = input("Ingrese la categoría estadística a buscar: ")
    anio_i = int(input("Ingrese el año inicial del periodo a consultar: "))
    anio_f = int(input("Ingrese el año final del periodo a consultar: "))
    time, size, num_surveys, num_census, records_return = logic.req_5(control, categoria_estadística, anio_i, anio_f)
    print()
    print("========================================================================================================")
    print("Tiempo de ejecución en ms: ", time)
    print(f"Cantidad de registros encontrados en la categoria_estadística {categoria_estadística} entre los años {anio_i} y {anio_f}: ", size)
    print(f"Cantidad de registros de tipo 'SURVEY' encontrados en la categoria_estadística {categoria_estadística} entre los años {anio_i} y {anio_f}: ", num_surveys)
    print(f"Cantidad de registros de tipo 'CENSUS' encontrados en la categoria_estadística {categoria_estadística} entre los años {anio_i} y {anio_f}: ", num_census)
    print("RESUMEN DE REGISTROS ENCONTRADOS")
    print(tb.tabulate(iterator(records_return), headers= 'keys' , tablefmt= "fancy_grid"))
    print()


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    departamento = input("Ingrese el departamento a buscar: ")
    fecha_i = input('Ingrese la fecha inicial del periodo a consultar (con formato "%Y-%m-%d"): ')
    fecha_f = input('Ingrese la fecha final del periodo a consultar (con formato "%Y-%m-%d"): ')
    time, size, num_surveys, num_census, records_return = logic.req_6(control, departamento, fecha_i, fecha_f)
    print()
    print("========================================================================================================")
    print("Tiempo de ejecución en ms: ", time)
    print(f"Cantidad de registros encontrados en el departamento {departamento} entre las fechas {fecha_i} y {fecha_f}: ", size)
    print(f"Cantidad de registros de tipo 'SURVEY' encontrados en el departamento {departamento} entre las fechas {fecha_i} y {fecha_f}: ", num_surveys)
    print(f"Cantidad de registros de tipo 'CENSUS' encontrados en el departamento {departamento} entre las fechas {fecha_i} y {fecha_f}: ", num_census)
    print("RESUMEN DE REGISTROS ENCONTRADOS")
    print(tb.tabulate(iterator(records_return), headers= 'keys' , tablefmt= "fancy_grid"))
    print()


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    departamento = input("Ingrese el departamento a buscar: ")
    anio_i = int(input("Ingrese el año inicial del periodo a consultar: "))
    anio_f = int(input("Ingrese el año final del periodo a consultar: "))
    time, size, max_records, min_records = logic.req_7(control, departamento, anio_i, anio_f)
    print()
    print("========================================================================================================")
    print("Tiempo de ejecución en ms: ", time)
    print(f"Cantidad de registros encontrados en el departamento {departamento} entre los años {anio_i} y {anio_f}: ", size)
    print("AÑO CON MAYOR CANTIDAD DE INGRESOS")
    print(tb.tabulate([max_records], headers= 'keys' , tablefmt= "fancy_grid"))
    print()
    print("AÑO CON MENOR CANTIDAD DE INGRESOS")
    print(tb.tabulate([min_records], headers= 'keys' , tablefmt= "fancy_grid"))
    print()



def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            estructura = definir_estructura()
            archivo = seleccionar_archivo()
            control = new_logic(estructura)
            load_data(control, archivo)
        elif int(inputs) == 2:
            print("INICIANDO EL REQUERIMIENTO 1")
            print("========================================================================================================")
            print_req_1(control)

        elif int(inputs) == 3:
            print("INICIANDO EL REQUERIMIENTO 2")
            print("========================================================================================================")
            print_req_2(control)

        elif int(inputs) == 4:
            print("INICIANDO EL REQUERIMIENTO 3")
            print("========================================================================================================")
            print_req_3(control)

        elif int(inputs) == 5:
            print("INICIANDO EL REQUERIMIENTO 4")
            print("========================================================================================================")
            print_req_4(control)

        elif int(inputs) == 6:
            print("INICIANDO EL REQUERIMIENTO 5")
            print("========================================================================================================")
            print_req_5(control)

        elif int(inputs) == 7:
            print("INICIANDO EL REQUERIMIENTO 6")
            print("========================================================================================================")
            print_req_6(control)

        elif int(inputs) == 8:
            print("INICIANDO EL REQUERIMIENTO 7")
            print("========================================================================================================")
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
