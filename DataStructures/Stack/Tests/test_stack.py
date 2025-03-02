import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

from DataStructures.Stack import stack as st

class TestStack(unittest.TestCase):
    
    def setUp(self):
        """Se ejecuta antes de cada test: crea una pila vacía."""
        self.stack = st.new_stack()

    def test_new_stack_empty(self):
        """Verifica que una pila recién creada esté vacía."""
        self.assertEqual(st.size(self.stack), 0)
        self.assertTrue(st.is_empty(self.stack))
        self.assertEqual(self.stack['elements'], [])

    def test_push_single_element(self):
        """Verifica push en una pila vacía."""
        st.push(self.stack, {'name': 'John', 'age': 25})
        self.assertEqual(st.size(self.stack), 1)
        self.assertFalse(st.is_empty(self.stack))
        self.assertEqual(self.stack['elements'][-1], {'name': 'John', 'age': 25})

    def test_push_multiple_elements(self):
        """Verifica push en una pila con varios elementos."""
        st.push(self.stack, {'name': 'John', 'age': 25})
        st.push(self.stack, {'name': 'Jane', 'age': 30})
        self.assertEqual(st.size(self.stack), 2)
        self.assertEqual(self.stack['elements'][0], {'name': 'John', 'age': 25})
        self.assertEqual(self.stack['elements'][-1], {'name': 'Jane', 'age': 30})

    def test_top(self):
        """Verifica que top retorne el elemento en el tope sin desapilarlo."""
        st.push(self.stack, {'name': 'John', 'age': 25})
        st.push(self.stack, {'name': 'Jane', 'age': 30})
        top_elem = st.top(self.stack)
        self.assertEqual(top_elem, {'name': 'Jane', 'age': 30})
        self.assertEqual(st.size(self.stack), 2)

    def test_pop(self):
        """Verifica que pop retire el elemento del tope y actualice la pila."""
        st.push(self.stack, {'name': 'John', 'age': 25})
        st.push(self.stack, {'name': 'Jane', 'age': 30})
        removed = st.pop(self.stack)
        self.assertEqual(removed, {'name': 'Jane', 'age': 30})
        self.assertEqual(st.size(self.stack), 1)
        self.assertEqual(st.top(self.stack), {'name': 'John', 'age': 25})

    def test_pop_empty(self):
        """Verifica que pop en una pila vacía lance una excepción."""
        with self.assertRaises(IndexError) as context:
            st.pop(self.stack)
        self.assertEqual(str(context.exception), "list index out of range")

    def test_is_empty(self):
        """Verifica la función is_empty en pila vacía y no vacía."""
        self.assertTrue(st.is_empty(self.stack))
        st.push(self.stack, 100)
        self.assertFalse(st.is_empty(self.stack))

    def test_size(self):
        """Verifica que size retorne la cantidad correcta de elementos."""
        self.assertEqual(st.size(self.stack), 0)
        st.push(self.stack, "A")
        self.assertEqual(st.size(self.stack), 1)
        st.push(self.stack, "B")
        self.assertEqual(st.size(self.stack), 2)
        st.pop(self.stack)
        self.assertEqual(st.size(self.stack), 1)

if __name__ == '__main__':
    unittest.main()
