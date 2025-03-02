import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

from DataStructures.List import array_list
import unittest

class TestArrayList(unittest.TestCase):
    def test_new_list(self):
        """Prueba la creación de una lista vacía."""
        lst = array_list.new_list()
        self.assertEqual(lst['size'], 0, "El tamaño de la lista recién creada debe ser 0.")
        self.assertEqual(lst['elements'], [], "Los elementos de la lista recién creada deben ser [].")

    def test_is_empty_true(self):
        """Prueba is_empty cuando la lista está vacía."""
        lst = array_list.new_list()
        self.assertTrue(array_list.is_empty(lst), "is_empty debería retornar True para una lista vacía.")

    def test_is_empty_false(self):
        """Prueba is_empty cuando la lista no está vacía."""
        lst = array_list.new_list()
        array_list.add_last(lst, 10)
        self.assertFalse(array_list.is_empty(lst), "is_empty debería retornar False para una lista con elementos.")

    def test_size_empty_list(self):
        """Prueba size en una lista vacía."""
        lst = array_list.new_list()
        self.assertEqual(array_list.size(lst), 0, "El tamaño de una lista vacía debería ser 0.")

    def test_size_non_empty_list(self):
        """Prueba size en una lista con elementos."""
        lst = array_list.new_list()
        array_list.add_last(lst, 10)
        array_list.add_last(lst, 20)
        self.assertEqual(array_list.size(lst), 2, "El tamaño de la lista debería ser 2.")

    def test_add_first_single(self):
        """Prueba add_first con un único elemento."""
        lst = array_list.new_list()
        array_list.add_first(lst, 5)
        self.assertEqual(lst['size'], 1, "El tamaño de la lista debería ser 1 después de agregar un elemento al inicio.")
        self.assertEqual(lst['elements'], [5], "El primer elemento debería ser 5.")

    def test_add_first_multiple(self):
        """Prueba add_first con múltiples elementos."""
        lst = array_list.new_list()
        array_list.add_first(lst, 5)
        array_list.add_first(lst, 10)
        self.assertEqual(lst['size'], 2, "El tamaño de la lista debería ser 2.")
        self.assertEqual(lst['elements'], [10, 5], "Los elementos deberían haberse agregado al inicio en orden inverso.")

    def test_add_last_single(self):
        """Prueba add_last con un único elemento."""
        lst = array_list.new_list()
        array_list.add_last(lst, 5)
        self.assertEqual(lst['size'], 1)
        self.assertEqual(lst['elements'], [5])

    def test_add_last_multiple(self):
        """Prueba add_last con múltiples elementos."""
        lst = array_list.new_list()
        array_list.add_last(lst, 5)
        array_list.add_last(lst, 10)
        self.assertEqual(lst['size'], 2)
        self.assertEqual(lst['elements'], [5, 10])

    def test_first_element_ok(self):
        """Prueba first_element en una lista con elementos."""
        lst = array_list.new_list()
        array_list.add_last(lst, 5)
        array_list.add_last(lst, 10)
        self.assertEqual(array_list.first_element(lst), 5, "El primer elemento debería ser 5.")

    def test_first_element_empty(self):
        """Prueba first_element en una lista vacía (debe lanzar IndexError)."""
        lst = array_list.new_list()
        with self.assertRaises(IndexError):
            array_list.first_element(lst)

    def test_last_element_ok(self):
        """Prueba last_element en una lista con elementos."""
        lst = array_list.new_list()
        array_list.add_last(lst, 5)
        array_list.add_last(lst, 10)
        self.assertEqual(array_list.last_element(lst), 10, "El último elemento debería ser 10.")

    def test_last_element_empty(self):
        """Prueba last_element en una lista vacía (debe lanzar IndexError)."""
        lst = array_list.new_list()
        with self.assertRaises(IndexError):
            array_list.last_element(lst)

    def test_get_element_valid(self):
        """Prueba get_element con posiciones válidas."""
        lst = array_list.new_list()
        array_list.add_last(lst, 'a')
        array_list.add_last(lst, 'b')
        self.assertEqual(array_list.get_element(lst, 0), 'a')
        self.assertEqual(array_list.get_element(lst, 1), 'b')

    def test_get_element_invalid_negative(self):
        """Prueba get_element con posición negativa (debe lanzar IndexError)."""
        lst = array_list.new_list()
        array_list.add_last(lst, 'a')
        with self.assertRaises(IndexError):
            array_list.get_element(lst, -1)

    def test_get_element_invalid_out_of_range(self):
        """Prueba get_element con posición mayor o igual al size (debe lanzar IndexError)."""
        lst = array_list.new_list()
        array_list.add_last(lst, 'a')
        with self.assertRaises(IndexError):
            array_list.get_element(lst, 1)

    def test_delete_element_valid(self):
        """Prueba delete_element en posición válida."""
        lst = array_list.new_list()
        array_list.add_last(lst, 'a')
        array_list.add_last(lst, 'b')
        array_list.delete_element(lst, 0)
        self.assertEqual(lst['size'], 1)
        self.assertEqual(lst['elements'], ['b'])

    def test_delete_element_invalid(self):
        """Prueba delete_element en posición inválida (debe lanzar IndexError)."""
        lst = array_list.new_list()
        array_list.add_last(lst, 'a')
        with self.assertRaises(IndexError):
            array_list.delete_element(lst, 1)

    def test_remove_first_ok(self):
        """Prueba remove_first en una lista con elementos."""
        lst = array_list.new_list()
        array_list.add_last(lst, 10)
        array_list.add_last(lst, 20)
        removed = array_list.remove_first(lst)
        self.assertEqual(removed, 10, "El elemento eliminado debe ser el primero.")
        self.assertEqual(lst['size'], 1)
        self.assertEqual(lst['elements'], [20])

    def test_remove_first_empty(self):
        """Prueba remove_first en una lista vacía (debe lanzar IndexError)."""
        lst = array_list.new_list()
        with self.assertRaises(IndexError):
            array_list.remove_first(lst)

    def test_remove_last_ok(self):
        """Prueba remove_last en una lista con elementos."""
        lst = array_list.new_list()
        array_list.add_last(lst, 10)
        array_list.add_last(lst, 20)
        removed = array_list.remove_last(lst)
        self.assertEqual(removed, 20, "El elemento eliminado debe ser el último.")
        self.assertEqual(lst['size'], 1)
        self.assertEqual(lst['elements'], [10])

    def test_remove_last_empty(self):
        """Prueba remove_last en una lista vacía (debe lanzar IndexError)."""
        lst = array_list.new_list()
        with self.assertRaises(IndexError):
            array_list.remove_last(lst)

    def test_insert_element_valid_positions(self):
        """Prueba insert_element en posiciones válidas (0, size)."""
        lst = array_list.new_list()
        array_list.insert_element(lst, 'a', 0)
        self.assertEqual(lst['elements'], ['a'])
        self.assertEqual(lst['size'], 1)

        array_list.insert_element(lst, 'b', 1)
        self.assertEqual(lst['elements'], ['a', 'b'])
        self.assertEqual(lst['size'], 2)

        array_list.insert_element(lst, 'c', 1)
        self.assertEqual(lst['elements'], ['a', 'c', 'b'])
        self.assertEqual(lst['size'], 3)

    def test_insert_element_invalid_positions(self):
        """Prueba insert_element con posiciones inválidas (negativa o > size)."""
        lst = array_list.new_list()
        with self.assertRaises(IndexError):
            array_list.insert_element(lst, 'x', 1)
        with self.assertRaises(IndexError):
            array_list.insert_element(lst, 'x', -1)

    def test_default_function(self):
        """Prueba la función de comparación por defecto."""
        self.assertEqual(array_list.default_function(5, 5), 0)
        self.assertEqual(array_list.default_function(10, 5), 1)
        self.assertEqual(array_list.default_function(5, 10), -1)

    def test_is_present_found(self):
        """Prueba is_present cuando el elemento sí está presente."""
        lst = array_list.new_list()
        array_list.add_last(lst, 1)
        array_list.add_last(lst, 2)
        array_list.add_last(lst, 3)
        pos = array_list.is_present(lst, 2, array_list.default_function)
        self.assertEqual(pos, 1, "El elemento 2 está en la posición 1.")

    def test_is_present_not_found(self):
        """Prueba is_present cuando el elemento no está presente."""
        lst = array_list.new_list()
        array_list.add_last(lst, 1)
        array_list.add_last(lst, 2)
        pos = array_list.is_present(lst, 3, array_list.default_function)
        self.assertEqual(pos, -1)

    def test_change_info_valid(self):
        """Prueba change_info con posición válida."""
        lst = array_list.new_list()
        array_list.add_last(lst, 'a')
        array_list.add_last(lst, 'b')
        array_list.change_info(lst, 1, 'z')
        self.assertEqual(lst['elements'], ['a', 'z'])

    def test_change_info_invalid(self):
        """Prueba change_info con posición inválida (debe lanzar IndexError)."""
        lst = array_list.new_list()
        array_list.add_last(lst, 'a')
        with self.assertRaises(IndexError):
            array_list.change_info(lst, 1, 'z')

    def test_exchange_valid(self):
        """Prueba exchange con posiciones válidas."""
        lst = array_list.new_list()
        array_list.add_last(lst, 'a')
        array_list.add_last(lst, 'b')
        array_list.exchange(lst, 0, 1)
        self.assertEqual(lst['elements'], ['b', 'a'])

    def test_exchange_invalid(self):
        """Prueba exchange con alguna posición inválida (debe lanzar IndexError)."""
        lst = array_list.new_list()
        array_list.add_last(lst, 'a')
        with self.assertRaises(IndexError):
            array_list.exchange(lst, 0, 1)
            
    def test_sub_list_valid(self):
        """Prueba sub_list con parámetros válidos."""
        lst = array_list.new_list()
        array_list.add_last(lst, 1)  
        array_list.add_last(lst, 2)  
        array_list.add_last(lst, 3)  
        sublst = array_list.sub_list(lst, 1, 2)
        self.assertEqual(sublst['size'], 2)
        self.assertEqual(sublst['elements'], [2, 3])

    def test_sub_list_invalid_start(self):
        """Prueba sub_list con posición inicial inválida (debe lanzar IndexError)."""
        lst = array_list.new_list()
        array_list.add_last(lst, 1)
        with self.assertRaises(IndexError):
            array_list.sub_list(lst, 1, 1)

    def test_sub_list_invalid_length(self):
        """Prueba sub_list cuando no hay suficientes elementos (debe lanzar IndexError)."""
        lst = array_list.new_list()
        array_list.add_last(lst, 1)
        array_list.add_last(lst, 2)
        with self.assertRaises(IndexError):
            array_list.sub_list(lst, 0, 3)

if __name__ == '__main__':
    unittest.main()
