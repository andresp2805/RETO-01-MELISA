import os

def ejecutar_todos():
    os.system("python3.13 Algorithms/Sorting/Tests/test_selection_sort.py")
    os.system("python3.13 Algorithms/Sorting/Tests/test_insertion_sort.py")
    os.system("python3.13 Algorithms/Sorting/Tests/test_shell_sort.py")
    os.system("python3.13 Algorithms/Sorting/Tests/test_merge_sort.py")
    os.system("python3.13 Algorithms/Sorting/Tests/test_quick_sort.py")
    os.system("python3.13 DataStructures/List/Tests/test_array_list.py")
    os.system("python3.13 DataStructures/List/Tests/test_single_linked_list.py")
    os.system("python3.13 DataStructures/Stack/Tests/test_stack.py")
    os.system("python3.13 DataStructures/Queue/Tests/test_queue.py")
    


def ejecutar_test_listas():
    os.system("python3.13 DataStructures/List/Tests/test_array_list.py")
    os.system("python3.13 DataStructures/List/Tests/test_single_linked_list.py")

def ejecutar_test_stacks():
    os.system("python3.13 DataStructures/Stack/Tests/test_stack.py")

def ejecutar_test_queue():
    os.system("python3.13 DataStructures/Queue/Tests/test_queue.py")

def ejecutar_test_sorting():
    os.system("python3.13 Algorithms/Sorting/Tests/test_selection_sort.py")
    os.system("python3.13 Algorithms/Sorting/Tests/test_insertion_sort.py")
    os.system("python3.13 Algorithms/Sorting/Tests/test_shell_sort.py")
    os.system("python3.13 Algorithms/Sorting/Tests/test_merge_sort.py")
    os.system("python3.13 Algorithms/Sorting/Tests/test_quick_sort.py")
    
def main():
    print("Seleccione el test a ejecutar:")
    print("0 - Todos")
    print("1 - Listas")
    print("2 - Stacks")
    print("3 - Queue")
    print("4 - Sorting")
    
    opcion = input("Ingrese una opción (0/1/2/3/4): ").strip()
    
    if opcion == "0":
        ejecutar_todos()
    elif opcion == "1":
        ejecutar_test_listas()
    elif opcion == "2":
        ejecutar_test_stacks()
    elif opcion == "3":
        ejecutar_test_queue()
    elif opcion == "4":
        ejecutar_test_sorting()
    else:
        print("Opción no válida. Intente de nuevo.")
        main()

if __name__ == '__main__':
    main()
