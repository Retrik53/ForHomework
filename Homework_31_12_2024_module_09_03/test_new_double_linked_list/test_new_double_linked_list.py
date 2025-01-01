import unittest
from Homework_31_12_2024_module_09_03.double_linked_list import LinkedList, Node
from Homework_31_12_2024_module_09_03.New_double_linked_list import AdvancedLinkedList

class TestNode(unittest.TestCase):
    def test_init(self):
        node = Node(10)
        self.assertEqual(node.data, 10)
        self.assertIsNone(node.next_node)
        self.assertIsNone(node.prev_node)

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.llist = LinkedList()

    def test_insert_at_head(self):
        self.llist.insert_at_head(10)
        self.assertEqual(self.llist.head.data, 10)
        self.assertIsNone(self.llist.head.next_node)
        self.assertIsNone(self.llist.head.prev_node)

        self.llist.insert_at_head(20)
        self.assertEqual(self.llist.head.data, 20)
        self.assertEqual(self.llist.head.next_node.data, 10)
        self.assertIsNone(self.llist.head.prev_node)

    def test_insert_at_tail(self):
        self.llist.insert_at_tail(30)
        self.assertEqual(self.llist.tail.data, 30)
        self.assertIsNone(self.llist.tail.next_node)
        self.assertIsNone(self.llist.tail.prev_node)

        self.llist.insert_at_tail(40)
        self.assertEqual(self.llist.tail.data, 40)
        self.assertEqual(self.llist.tail.prev_node.data, 30)
        self.assertIsNone(self.llist.tail.next_node)

    def test_remove_from_head(self):
        self.llist.insert_at_head(50)
        self.llist.insert_at_head(60)
        result = self.llist.remove_from_head()
        self.assertIn('Были удалены данные', result)
        self.assertEqual(self.llist.head.data, 50)

    def test_remove_from_tail(self):
        self.llist.insert_at_tail(70)
        self.llist.insert_at_tail(80)
        result = self.llist.remove_from_tail()
        self.assertIn('Были удалены данные', result)
        self.assertEqual(self.llist.tail.data, 70)

class TestAdvancedLinkedList(unittest.TestCase):
    def setUp(self):
        self.adv_llist = AdvancedLinkedList()

    def test_print_ll_from_tail(self):
        self.adv_llist.insert_at_tail(100)
        self.adv_llist.insert_at_tail(200)
        result = self.adv_llist.print_ll_from_tail()
        self.assertIn('Список выведен с конца', result)

    def test_insert_at_index(self):
        self.adv_llist.insert_at_index(0, 300)
        self.assertEqual(self.adv_llist.head.data, 300)
        with self.assertRaises(IndexError):
            self.adv_llist.insert_at_index(-1, 400)

    def test_remove_node_index(self):
        self.adv_llist.insert_at_tail(500)
        self.adv_llist.insert_at_tail(600)
        result = self.adv_llist.remove_node_index(0)
        self.assertIn('Были удалены данные 500 из головы списка.\nТеперь голова списка 600', result)
        self.assertEqual(self.adv_llist.head.data, 600)

    def test_remove_node_data(self):
        self.adv_llist.insert_at_tail(700)
        self.adv_llist.insert_at_tail(800)
        result = self.adv_llist.remove_node_data(700)
        self.assertIn('Были удалены данные 700 из головы списка.\nТеперь голова списка 800', result)
        self.assertEqual(self.adv_llist.head.data, 800)

    def test_len_ll(self):
        self.adv_llist.insert_at_tail(900)
        self.adv_llist.insert_at_tail(1000)
        self.assertEqual(self.adv_llist.len_ll(), 2)

    def test_contains_from_head(self):
        self.adv_llist.insert_at_tail(1100)
        self.adv_llist.insert_at_tail(1200)
        self.assertTrue(self.adv_llist.contains_from_head(1100))
        self.assertFalse(self.adv_llist.contains_from_head(1300))

    def test_contains_from_tail(self):
        self.adv_llist.insert_at_tail(1400)
        self.adv_llist.insert_at_tail(1500)
        self.assertTrue(self.adv_llist.contains_from_tail(1500))
        self.assertFalse(self.adv_llist.contains_from_tail(1600))

    def test_contains_from(self):
        self.adv_llist.insert_at_tail(1700)
        self.adv_llist.insert_at_tail(1800)
        self.assertTrue(self.adv_llist.contains_from(1700, "head"))
        self.assertTrue(self.adv_llist.contains_from(1800, "tail"))
        with self.assertRaises(ValueError):
            self.adv_llist.contains_from(1900, "middle")

if __name__ == '__main__':
    unittest.main()