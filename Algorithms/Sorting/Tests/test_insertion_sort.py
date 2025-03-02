import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

from Algorithms.Sorting import insertion_sort
from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as sll

def less_than(a, b):
    return a < b

class TestInsertionSort(unittest.TestCase):
    
    def test_empty_array_list(self):
        """Prueba ordenar una array_list vacía."""
        lst = al.new_list()
        lst['type'] = 'array_list'
        sorted_lst = insertion_sort.insertion_sort(lst, less_than)
        self.assertEqual(sorted_lst['size'], 0)
        self.assertEqual(sorted_lst['elements'], [])

    def test_single_element_array_list(self):
        """Prueba ordenar una array_list con un único elemento."""
        lst = al.new_list()
        lst['type'] = 'array_list'
        al.add_last(lst, 42)
        sorted_lst = insertion_sort.insertion_sort(lst, less_than)
        self.assertEqual(sorted_lst['size'], 1)
        self.assertEqual(sorted_lst['elements'], [42])

    def test_multiple_elements_array_list(self):
        """Prueba ordenar una array_list con varios elementos."""
        lst = al.new_list()
        lst['type'] = 'array_list'
        al.add_last(lst, 5)
        al.add_last(lst, 3)
        al.add_last(lst, 8)
        al.add_last(lst, 1)
        sorted_lst = insertion_sort.insertion_sort(lst, less_than)
        self.assertEqual(sorted_lst['size'], 4)
        self.assertEqual(sorted_lst['elements'], [1, 3, 5, 8])

    def test_empty_single_linked_list(self):
        """Prueba ordenar una single_linked_list vacía."""
        lst = sll.new_list()
        lst['type'] = 'single_linked_list'
        sorted_lst = insertion_sort.insertion_sort(lst, less_than)
        self.assertEqual(sorted_lst['size'], 0)
        self.assertIsNone(sorted_lst['first'])
        self.assertIsNone(sorted_lst['last'])

    def test_single_element_single_linked_list(self):
        """Prueba ordenar una single_linked_list con un único elemento."""
        lst = sll.new_list()
        lst['type'] = 'single_linked_list'
        sll.add_last(lst, 99)
        sorted_lst = insertion_sort.insertion_sort(lst, less_than)
        self.assertEqual(sorted_lst['size'], 1)
        self.assertEqual(sll.get_element(sorted_lst, 0), 99)

    def test_multiple_elements_single_linked_list(self):
        """Prueba ordenar una single_linked_list con varios elementos."""
        lst = sll.new_list()
        lst['type'] = 'single_linked_list'
        sll.add_last(lst, 10)
        sll.add_last(lst, 7)
        sll.add_last(lst, 15)
        sll.add_last(lst, 2)
        sorted_lst = insertion_sort.insertion_sort(lst, less_than)
        self.assertEqual(sorted_lst['size'], 4)
        self.assertEqual(sll.get_element(sorted_lst, 0), 2)
        self.assertEqual(sll.get_element(sorted_lst, 1), 7)
        self.assertEqual(sll.get_element(sorted_lst, 2), 10)
        self.assertEqual(sll.get_element(sorted_lst, 3), 15)

    def test_invalid_type(self):
        """Prueba que se lance ValueError si el campo 'type' no es válido."""
        lst = al.new_list()
        lst['type'] = 'invalid_type'
        with self.assertRaises(ValueError):
            insertion_sort.insertion_sort(lst, less_than)

if __name__ == '__main__':
    unittest.main()
