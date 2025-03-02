import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

from DataStructures.List import array_list
from DataStructures.List import single_linked_list
from DataStructures.List.list_iterator import iterator
import unittest

class TestIteratorArrayList(unittest.TestCase):
    def test_iterator_empty_array_list(self):
        """Prueba que iterar sobre una array_list vacía retorne una lista vacía."""
        lst = array_list.new_list()
        result = list(iterator(lst))
        self.assertEqual(result, [], "La iteración sobre una array_list vacía debe retornar []")

    def test_iterator_array_list(self):
        """Prueba la iteración sobre una array_list con varios elementos."""
        lst = array_list.new_list()
        array_list.add_last(lst, 1)
        array_list.add_last(lst, 2)
        array_list.add_last(lst, 3)
        result = list(iterator(lst))
        self.assertEqual(result, [1, 2, 3], "La iteración debe retornar los elementos en el mismo orden en que están almacenados.")

class TestIteratorSingleLinkedList(unittest.TestCase):
    def test_iterator_empty_single_linked_list(self):
        """Prueba que iterar sobre una single_linked_list vacía retorne una lista vacía."""
        lst = single_linked_list.new_list()
        result = list(iterator(lst))
        self.assertEqual(result, [], "La iteración sobre una single_linked_list vacía debe retornar []")

    def test_iterator_single_linked_list(self):
        """Prueba la iteración sobre una single_linked_list con varios elementos."""
        lst = single_linked_list.new_list()
        single_linked_list.add_last(lst, 'a')
        single_linked_list.add_last(lst, 'b')
        single_linked_list.add_last(lst, 'c')
        result = list(iterator(lst))
        self.assertEqual(result, ['a', 'b', 'c'], "La iteración debe retornar los elementos en el orden en que se agregaron.")

class TestIteratorTypeError(unittest.TestCase):
    def test_iterator_tipo_no_soportado(self):
        """Prueba que la función iterator lance un TypeError si el diccionario no tiene el campo 'type' esperado."""
        invalid_list = {'size': 0, 'elements': []}
        with self.assertRaises(TypeError):
            list(iterator(invalid_list))

if __name__ == '__main__':
    unittest.main()
