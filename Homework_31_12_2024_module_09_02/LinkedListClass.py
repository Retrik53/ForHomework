class Node:

    """ Класс узла односвязного списка."""

    def __init__(self, data, next_node=None):

        """Инициализация нового узла."""

        self.data = data
        self.next_node = next_node


class LinkedList:

    """ Класс односвязного списка."""

    def __init__(self):
        """ Инициализация пустого односвязного списка. """
        self.head = None

    def insert_at_head(self, data):

        """ Вставка нового узла в начало списка."""

        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node
        return f"Узел с данными {new_node.data} добавлен в начало списка"

    def insert_at_end(self, data):

        """ Вставка нового узла в конец списка."""

        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next_node:
            current_node = current_node.next_node
        current_node.next_node = new_node
        return f"Узел с данными {new_node.data} добавлен в конец списка"

    def remove_node_position(self, rm_position):

        """ Удаляет узел по указанной позиции."""

        if rm_position == 1:
            removed_node = self.head
            self.head = self.head.next_node
            return f"Удален узел с данными {removed_node.data} позиции {rm_position}"
        current_node = self.head
        current_node_position = 1
        while current_node is not None and current_node_position < rm_position - 1:
            current_node = current_node.next_node
            current_node_position += 1
        if current_node is None or current_node.next_node is None:
            return "Ничего не удалено"
        removed_node = current_node.next_node
        current_node.next_node = current_node.next_node.next_node  # removed_node.next_node
        return f"Удален узел с данными {removed_node.data} позиции {rm_position}"

    def insert_at_position(self, data, node_position):

        """ Вставляет новый узел в указанную позицию."""

        new_node = Node(data)
        if node_position == 1:
            self.insert_at_head(data)
            return f"Узел с данными {new_node.data} добавлен на позицию {node_position}"
        current_node = self.head
        current_node_position = 1
        while current_node is not None and current_node_position < node_position - 1:
            current_node = current_node.next_node
            current_node_position += 1
        if current_node is None:
            return None
        new_node.next_node = current_node.next_node
        current_node.next_node = new_node
        return f"Узел с данными {new_node.data} добавлен на позицию {node_position}"

    def print_ll(self):

        """ Выводит все узлы списка."""

        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next_node
        return "Данные списка выведены"

    def get(self, data):

        """ Проверяет наличие данных в списке и возвращает соответствующий узел."""

        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True, current_node
            current_node = current_node.next_node
        return False, None

    def change_data(self, node_data, change_data):

        """ Изменяет данные в узле, если такой узел существует."""

        current_node = self.head
        current_node_position = 1
        while current_node:
            if current_node.data == node_data:
                current_node.data = change_data
                return f"Заменены данные в узле № {current_node_position}"
            current_node = current_node.next_node
            current_node_position += 1
        return "Данные не обнаружены"