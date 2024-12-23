import unittest
from Homework_23_12_2024.Stack import Stack

class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_push_pop(self):
        self.stack.push(10)
        self.assertEqual(self.stack.pop(), 10)

        self.stack.push(20)
        self.stack.push(30)
        self.assertEqual(self.stack.pop(), 30)
        self.assertEqual(self.stack.pop(), 20)

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())

        self.stack.push(100)
        self.assertFalse(self.stack.is_empty())

    def test_is_full(self):
        self.assertFalse(self.stack.is_full())
        for i in range(5):
            self.stack.push(i)

        self.assertTrue(self.stack.is_full())

    def test_clear_stack(self):
        self.stack.push(40)
        self.stack.push(50)

        self.stack.clear_stack()

        self.assertTrue(self.stack.is_empty())

    def test_get_data(self):
        self.stack.push(60)
        self.stack.push(70)
        self.stack.push(80)

        self.assertEqual(self.stack.get_data(0), 80)
        self.assertEqual(self.stack.get_data(1), 70)
        self.assertEqual(self.stack.get_data(2), 60)

        self.assertEqual(self.stack.get_data(3), 'Out of range')

    def test_counter_int(self):
        self.stack.push('abc')
        self.stack.push(90)
        self.stack.push(3.14)
        self.stack.push(100)

        self.assertEqual(self.stack.counter_int(), 2)

if __name__ == '__main__':
    unittest.main()