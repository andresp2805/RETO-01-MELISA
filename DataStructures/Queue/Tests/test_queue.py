import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

from DataStructures.Queue import queue as q

class TestQueue(unittest.TestCase):

    def setUp(self):
        """Se ejecuta antes de cada test: crea una cola vacía."""
        self.queue = q.new_queue()

    def test_new_queue_empty(self):
        """Verifica que una cola recién creada esté vacía."""
        self.assertEqual(q.size(self.queue), 0)
        self.assertTrue(q.is_empty(self.queue))
        self.assertIsNone(self.queue.get('first'))
        self.assertIsNone(self.queue.get('last'))

    def test_enqueue_single_element(self):
        """Verifica enqueue en una cola vacía."""
        q.enqueue(self.queue, "A")
        self.assertEqual(q.size(self.queue), 1)
        self.assertFalse(q.is_empty(self.queue))
        self.assertEqual(self.queue['first']['info'], "A")
        self.assertEqual(self.queue['last']['info'], "A")

    def test_enqueue_multiple_elements(self):
        """Verifica enqueue en una cola con varios elementos."""
        q.enqueue(self.queue, "A")
        q.enqueue(self.queue, "B")
        self.assertEqual(q.size(self.queue), 2)
        self.assertEqual(self.queue['first']['info'], "A")
        self.assertEqual(self.queue['last']['info'], "B")

    def test_dequeue_single_element(self):
        """Verifica dequeue cuando la cola tiene un solo elemento."""
        q.enqueue(self.queue, "A")
        removed = q.dequeue(self.queue)
        self.assertEqual(removed, "A")
        self.assertTrue(q.is_empty(self.queue))
        self.assertEqual(q.size(self.queue), 0)
        self.assertIsNone(self.queue['first'])
        self.assertIsNone(self.queue['last'])

    def test_dequeue_multiple_elements(self):
        """Verifica dequeue cuando la cola tiene varios elementos."""
        q.enqueue(self.queue, "A")
        q.enqueue(self.queue, "B")
        q.enqueue(self.queue, "C")
        removed = q.dequeue(self.queue)
        self.assertEqual(removed, "A")
        self.assertEqual(q.size(self.queue), 2)
        self.assertEqual(self.queue['first']['info'], "B")
        self.assertEqual(self.queue['last']['info'], "C")

    def test_dequeue_empty(self):
        """Verifica que dequeue en una cola vacía lance excepción."""
        with self.assertRaises(IndexError):
            q.dequeue(self.queue)

    def test_peek(self):
        """Verifica que peek retorne el primer elemento sin removerlo."""
        q.enqueue(self.queue, "A")
        q.enqueue(self.queue, "B")
        first_elem = q.peek(self.queue)
        self.assertEqual(first_elem, "A")
        self.assertEqual(q.size(self.queue), 2)
        self.assertEqual(self.queue['first']['info'], "A")
        self.assertEqual(self.queue['last']['info'], "B")

    def test_peek_empty(self):
        """Verifica que peek en una cola vacía lance excepción."""
        with self.assertRaises(IndexError):
            q.peek(self.queue)

    def test_is_empty(self):
        """Verifica is_empty en cola vacía y no vacía."""
        self.assertTrue(q.is_empty(self.queue))
        q.enqueue(self.queue, "X")
        self.assertFalse(q.is_empty(self.queue))

    def test_size(self):
        """Verifica que size retorne la cantidad correcta de elementos."""
        self.assertEqual(q.size(self.queue), 0)
        q.enqueue(self.queue, "A")
        self.assertEqual(q.size(self.queue), 1)
        q.enqueue(self.queue, "B")
        self.assertEqual(q.size(self.queue), 2)
        q.dequeue(self.queue)
        self.assertEqual(q.size(self.queue), 1)

if __name__ == '__main__':
    unittest.main()
