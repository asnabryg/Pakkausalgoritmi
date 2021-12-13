import unittest
from min_heap import MinHeap


class TestBitConversion(unittest.TestCase):

    def setUp(self):
        self.heap = MinHeap()

    def test_init(self):
        self.assertNotEqual(self.heap, None)
        self.assertEqual(self.heap.list, [0])
        self.assertEqual(self.heap.size, 0)

    def test_heap_maintain_structure(self):
        self.heap.push(5)
        self.heap.push(2)
        self.heap.push(8)
        self.heap.push(12)
        self.heap.push(11)
        self.assertEqual(self.heap.list, [0, 2, 5, 8, 12, 11])
        self.assertEqual(self.heap.size, 5)

    def test_pop(self):
        self.heap.push(5)
        self.heap.push(2)
        self.heap.push(8)
        self.heap.push(12)
        self.heap.push(11)
        self.assertEqual(self.heap.pop(), 2)
        for _ in range(4):
            self.heap.pop()
        self.assertEqual(self.heap.pop(), None)
