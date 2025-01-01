import unittest
from Homework_31_12_2024_module_09_02.Queue import Queue

class TestQueue(unittest.TestCase):
    def setUp(self):
        self.q = Queue(5)

    def test_is_empty(self):
        self.assertTrue(self.q.is_empty())

        self.q.enqueue('A')
        self.assertFalse(self.q.is_empty())

    def test_is_full(self):
        self.assertFalse(self.q.is_full())

        self.q.enqueue('A')
        self.q.enqueue('B')
        self.q.enqueue('C')
        self.q.enqueue('D')
        self.q.enqueue('E')
        self.assertTrue(self.q.is_full())

if __name__ == '__main__':
    unittest.main()