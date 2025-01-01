import unittest
from Homework_31_12_2024_module_09_02.LinkedListClass import LinkedList, Node

class TestNode(unittest.TestCase):

    def test_init(self):
        node = Node(10)
        self.assertEqual(node.data, 10)
        self.assertIsNone(node.next_node)

        node2 = Node("test", node)
        self.assertEqual(node2.data, "test")
        self.assertEqual(node2.next_node, node)


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.llist = LinkedList()

    def test_insert_at_head(self):
        result = self.llist.insert_at_head(5)
        self.assertEqual(result, "Узел с данными 5 добавлен в начало списка")
        self.assertEqual(self.llist.head.data, 5)
        self.assertIsNone(self.llist.head.next_node)

        result = self.llist.insert_at_head(7)
        self.assertEqual(result, "Узел с данными 7 добавлен в начало списка")
        self.assertEqual(self.llist.head.data, 7)
        self.assertEqual(self.llist.head.next_node.data, 5)

    def test_insert_at_end(self):
        self.llist.insert_at_end(3)
        self.assertEqual(self.llist.head.data, 3)
        self.assertIsNone(self.llist.head.next_node)

        self.llist.insert_at_end(4)
        self.assertEqual(self.llist.head.next_node.data, 4)

    def test_remove_node_position(self):
        self.llist.insert_at_head(1)
        self.llist.insert_at_head(2)
        self.llist.insert_at_head(3)

        result = self.llist.remove_node_position(2)
        self.assertEqual(result, "Удален узел с данными 2 позиции 2")
        self.assertEqual(self.llist.head.data, 3)
        self.assertEqual(self.llist.head.next_node.data, 1)

        result = self.llist.remove_node_position(1)
        self.assertEqual(result, "Удален узел с данными 3 позиции 1")
        self.assertEqual(self.llist.head.data, 1)

        result = self.llist.remove_node_position(100)
        self.assertEqual(result, "Ничего не удалено")

    def test_insert_at_position(self):
        self.llist.insert_at_position(1, 1)
        self.assertEqual(self.llist.head.data, 1)

        self.llist.insert_at_position(2, 2)
        self.assertEqual(self.llist.head.next_node.data, 2)

        self.llist.insert_at_position(0, 1)
        self.assertEqual(self.llist.head.data, 0)
        self.assertEqual(self.llist.head.next_node.data, 1)

    def test_print_ll(self):
        self.llist.insert_at_head(6)
        self.llist.insert_at_head(8)
        result = self.llist.print_ll()
        self.assertEqual(result, "Данные списка выведены")

    def test_get(self):
        self.llist.insert_at_head(9)
        found, node = self.llist.get(9)
        self.assertTrue(found)
        self.assertEqual(node.data, 9)

        found, node = self.llist.get(10)
        self.assertFalse(found)
        self.assertIsNone(node)

    def test_change_data(self):
        self.llist.insert_at_head(11)
        self.llist.insert_at_head(12)
        result = self.llist.change_data(11, 13)
        self.assertEqual(result, "Заменены данные в узле № 2")
        self.assertEqual(self.llist.head.next_node.data, 13)