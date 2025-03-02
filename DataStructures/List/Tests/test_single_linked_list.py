import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

from DataStructures.List import single_linked_list as sll
import unittest
class TestSingleLinkedList(unittest.TestCase):

    def test_new_list(self):
        """Prueba la creación de una lista vacía."""
        lst = sll.new_list()
        self.assertEqual(lst['size'], 0)
        self.assertIsNone(lst['first'])
        self.assertIsNone(lst['last'])
        self.assertEqual(lst['type'], 'single_linked_list')

    def test_is_empty_true(self):
        """Prueba is_empty cuando la lista está vacía."""
        lst = sll.new_list()
        self.assertTrue(sll.is_empty(lst))

    def test_is_empty_false(self):
        """Prueba is_empty cuando la lista no está vacía."""
        lst = sll.new_list()
        sll.add_last(lst, 10)
        self.assertFalse(sll.is_empty(lst))

    def test_size_empty_list(self):
        """Prueba size en una lista vacía."""
        lst = sll.new_list()
        self.assertEqual(sll.size(lst), 0)

    def test_size_non_empty_list(self):
        """Prueba size en una lista con elementos."""
        lst = sll.new_list()
        sll.add_last(lst, 10)
        sll.add_last(lst, 20)
        self.assertEqual(sll.size(lst), 2)

    def test_add_first_empty(self):
        """Prueba add_first en una lista vacía."""
        lst = sll.new_list()
        sll.add_first(lst, "A")
        self.assertEqual(lst['size'], 1)
        self.assertEqual(lst['first']['info'], "A")
        self.assertEqual(lst['last']['info'], "A")

    def test_add_first_non_empty(self):
        """Prueba add_first en una lista con elementos."""
        lst = sll.new_list()
        sll.add_first(lst, "B")
        sll.add_first(lst, "A")
        self.assertEqual(lst['size'], 2)
        self.assertEqual(lst['first']['info'], "A")
        self.assertEqual(lst['first']['next']['info'], "B")
        self.assertEqual(lst['last']['info'], "B")

    def test_add_last_empty(self):
        """Prueba add_last en una lista vacía."""
        lst = sll.new_list()
        sll.add_last(lst, "A")
        self.assertEqual(lst['size'], 1)
        self.assertEqual(lst['first']['info'], "A")
        self.assertEqual(lst['last']['info'], "A")

    def test_add_last_non_empty(self):
        """Prueba add_last en una lista con elementos."""
        lst = sll.new_list()
        sll.add_last(lst, "A")
        sll.add_last(lst, "B")
        self.assertEqual(lst['size'], 2)
        self.assertEqual(lst['first']['info'], "A")
        self.assertEqual(lst['last']['info'], "B")
        self.assertEqual(lst['first']['next']['info'], "B")

    def test_first_element_ok(self):
        """Prueba first_element en una lista con elementos."""
        lst = sll.new_list()
        sll.add_last(lst, "A")
        sll.add_last(lst, "B")
        self.assertEqual(sll.first_element(lst), "A")

    def test_first_element_empty(self):
        """Prueba first_element en una lista vacía (debe lanzar IndexError)."""
        lst = sll.new_list()
        with self.assertRaises(IndexError):
            sll.first_element(lst)

    def test_last_element_ok(self):
        """Prueba last_element en una lista con elementos."""
        lst = sll.new_list()
        sll.add_last(lst, "A")
        sll.add_last(lst, "B")
        self.assertEqual(sll.last_element(lst), "B")

    def test_last_element_empty(self):
        """Prueba last_element en una lista vacía (debe lanzar IndexError)."""
        lst = sll.new_list()
        with self.assertRaises(IndexError):
            sll.last_element(lst)

    def test_get_element_valid(self):
        """Prueba get_element con posiciones válidas."""
        lst = sll.new_list()
        sll.add_last(lst, "A")
        sll.add_last(lst, "B")
        sll.add_last(lst, "C")
        self.assertEqual(sll.get_element(lst, 0), "A")
        self.assertEqual(sll.get_element(lst, 1), "B")
        self.assertEqual(sll.get_element(lst, 2), "C")

    def test_get_element_invalid_negative(self):
        """Prueba get_element con posición negativa (debe lanzar IndexError)."""
        lst = sll.new_list()
        sll.add_last(lst, "A")
        with self.assertRaises(IndexError):
            sll.get_element(lst, -1)

    def test_get_element_invalid_out_of_range(self):
        """Prueba get_element con posición >= size (debe lanzar IndexError)."""
        lst = sll.new_list()
        sll.add_last(lst, "A")
        with self.assertRaises(IndexError):
            sll.get_element(lst, 1)

    def test_delete_element_valid_first(self):
        """Prueba delete_element eliminando el primer elemento."""
        lst = sll.new_list()
        sll.add_last(lst, "A")
        sll.add_last(lst, "B")
        sll.delete_element(lst, 0)
        self.assertEqual(lst['size'], 1)
        self.assertEqual(lst['first']['info'], "B")
        self.assertEqual(lst['last']['info'], "B")

    def test_delete_element_valid_middle(self):
        """Prueba delete_element eliminando un elemento en medio."""
        lst = sll.new_list()
        sll.add_last(lst, "A")
        sll.add_last(lst, "B")
        sll.add_last(lst, "C")
        sll.delete_element(lst, 1)
        self.assertEqual(lst['size'], 2)
        self.assertEqual(lst['first']['info'], "A")
        self.assertEqual(lst['first']['next']['info'], "C")
        self.assertEqual(lst['last']['info'], "C")

    def test_delete_element_valid_last(self):
        """Prueba delete_element eliminando el último elemento."""
        lst = sll.new_list()
        sll.add_last(lst, "A")
        sll.add_last(lst, "B")
        sll.delete_element(lst, 1)
        self.assertEqual(lst['size'], 1)
        self.assertEqual(lst['first']['info'], "A")
        self.assertEqual(lst['last']['info'], "A")

    def test_delete_element_invalid(self):
        """Prueba delete_element en posición inválida (debe lanzar IndexError)."""
        lst = sll.new_list()
        sll.add_last(lst, "A")
        with self.assertRaises(IndexError):
            sll.delete_element(lst, 1)

    def test_remove_first_ok(self):
        """Prueba remove_first en una lista con elementos."""
        lst = sll.new_list()
        sll.add_last(lst, "A")
        sll.add_last(lst, "B")
        removed = sll.remove_first(lst)
        self.assertEqual(removed, "A")
        self.assertEqual(lst['size'], 1)
        self.assertEqual(lst['first']['info'], "B")
        self.assertEqual(lst['last']['info'], "B")

    def test_remove_first_empty(self):
        """Prueba remove_first en una lista vacía (debe lanzar IndexError)."""
        lst = sll.new_list()
        with self.assertRaises(IndexError):
            sll.remove_first(lst)

    def test_remove_last_ok(self):
        """Prueba remove_last en una lista con varios elementos."""
        lst = sll.new_list()
        sll.add_last(lst, "A")
        sll.add_last(lst, "B")
        sll.add_last(lst, "C")
        removed = sll.remove_last(lst)
        self.assertEqual(removed, "C")
        self.assertEqual(lst['size'], 2)
        self.assertEqual(lst['last']['info'], "B")

    def test_remove_last_single(self):
        """Prueba remove_last en una lista con un solo elemento."""
        lst = sll.new_list()
        sll.add_last(lst, "A")
        removed = sll.remove_last(lst)
        self.assertEqual(removed, "A")
        self.assertEqual(lst['size'], 0)
        self.assertIsNone(lst['first'])
        self.assertIsNone(lst['last'])

    def test_remove_last_empty(self):
        """Prueba remove_last en una lista vacía (debe lanzar IndexError)."""
        lst = sll.new_list()
        with self.assertRaises(IndexError):
            sll.remove_last(lst)

    def test_insert_element_start(self):
        """Prueba insert_element en la posición 0 (equivale a add_first)."""
        lst = sll.new_list()
        sll.insert_element(lst, "A", 0)
        self.assertEqual(lst['size'], 1)
        self.assertEqual(lst['first']['info'], "A")
        self.assertEqual(lst['last']['info'], "A")

    def test_insert_element_end(self):
        """Prueba insert_element en la posición size (equivale a add_last)."""
        lst = sll.new_list()
        sll.insert_element(lst, "A", 0)
        sll.insert_element(lst, "B", 1)
        self.assertEqual(lst['size'], 2)
        self.assertEqual(lst['last']['info'], "B")

    def test_insert_element_middle(self):
        """Prueba insert_element en una posición intermedia."""
        lst = sll.new_list()
        sll.insert_element(lst, "A", 0)
        sll.insert_element(lst, "C", 1)
        sll.insert_element(lst, "B", 1)
        self.assertEqual(lst['size'], 3)
        self.assertEqual(sll.get_element(lst, 0), "A")
        self.assertEqual(sll.get_element(lst, 1), "B")
        self.assertEqual(sll.get_element(lst, 2), "C")

    def test_insert_element_invalid(self):
        """Prueba insert_element con posición inválida."""
        lst = sll.new_list()
        with self.assertRaises(IndexError):
            sll.insert_element(lst, "X", 1)
        with self.assertRaises(IndexError):
            sll.insert_element(lst, "X", -1)

    def test_default_function(self):
        """Prueba la función de comparación por defecto."""
        self.assertEqual(sll.default_function(5, 5), 0)
        self.assertEqual(sll.default_function(10, 5), 1)
        self.assertEqual(sll.default_function(5, 10), -1)

    def test_is_present_found(self):
        """Prueba is_present cuando el elemento sí está presente."""
        lst = sll.new_list()
        sll.add_last(lst, "A")
        sll.add_last(lst, "B")
        sll.add_last(lst, "C")
        pos = sll.is_present(lst, "B", sll.default_function)
        self.assertEqual(pos, 1)

    def test_is_present_not_found(self):
        """Prueba is_present cuando el elemento no está presente."""
        lst = sll.new_list()
        sll.add_last(lst, "A")
        sll.add_last(lst, "B")
        pos = sll.is_present(lst, "C", sll.default_function)
        self.assertEqual(pos, -1)

    def test_change_info_valid(self):
        """Prueba change_info con posición válida."""
        lst = sll.new_list()
        sll.add_last(lst, "A")
        sll.add_last(lst, "B")
        sll.change_info(lst, 1, "B2")
        self.assertEqual(sll.get_element(lst, 1), "B2")

    def test_change_info_invalid(self):
        """Prueba change_info con posición inválida."""
        lst = sll.new_list()
        sll.add_last(lst, "A")
        with self.assertRaises(IndexError):
            sll.change_info(lst, 1, "Invalido")

    def test_exchange_valid(self):
        """Prueba exchange con posiciones válidas."""
        lst = sll.new_list()
        sll.add_last(lst, "A")
        sll.add_last(lst, "B")
        sll.add_last(lst, "C")
        sll.exchange(lst, 0, 2)
        self.assertEqual(sll.get_element(lst, 0), "C")
        self.assertEqual(sll.get_element(lst, 2), "A")

    def test_exchange_same_position(self):
        """Prueba exchange con posiciones iguales (no debe haber cambios)."""
        lst = sll.new_list()
        sll.add_last(lst, "A")
        sll.add_last(lst, "B")
        sll.exchange(lst, 1, 1)
        self.assertEqual(sll.get_element(lst, 0), "A")
        self.assertEqual(sll.get_element(lst, 1), "B")

    def test_exchange_invalid(self):
        """Prueba exchange con alguna posición inválida."""
        lst = sll.new_list()
        sll.add_last(lst, "A")
        with self.assertRaises(IndexError):
            sll.exchange(lst, 0, 1)
            
    def test_sub_list_valid(self):
        """Prueba sub_list con parámetros válidos."""
        lst = sll.new_list()
        sll.add_last(lst, "A")
        sll.add_last(lst, "B")
        sll.add_last(lst, "C")
        sll.add_last(lst, "D")
        sublst = sll.sub_list(lst, 1, 2)
        self.assertEqual(sublst['size'], 2)
        self.assertEqual(sll.get_element(sublst, 0), "B")
        self.assertEqual(sll.get_element(sublst, 1), "C")

    def test_sub_list_invalid_start(self):
        """Prueba sub_list con posición inicial inválida."""
        lst = sll.new_list()
        sll.add_last(lst, "A")
        with self.assertRaises(IndexError):
            sll.sub_list(lst, 1, 1)

    def test_sub_list_invalid_length(self):
        """Prueba sub_list cuando no hay suficientes elementos."""
        lst = sll.new_list()
        sll.add_last(lst, "A")
        sll.add_last(lst, "B")
        with self.assertRaises(IndexError):
            sll.sub_list(lst, 0, 3)

if __name__ == '__main__':
    unittest.main()
