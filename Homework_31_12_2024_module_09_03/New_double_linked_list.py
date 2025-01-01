from double_linked_list import LinkedList, Node


class AdvancedLinkedList(LinkedList):

    def print_ll_from_tail(self):

        """ Печать списка в обратном порядке от хвоста к голове """

        current_node = self.tail
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.prev_node
        return "Список выведен с конца"

    def insert_at_index(self, index, data):

        """ Добавление элемента по указанному индексу """

        if index < 0 or (index > 0 and index >= self.len_ll()):
            raise IndexError("Индекс вне допустимого диапазона")

        if index == 0:
            return self.insert_at_head(data)
        elif index == self.len_ll():
            return self.insert_at_tail(data)

        new_node = Node(data)
        current_node = self.head
        for _ in range(index - 1):  # Двигаемся до нужного индекса
            current_node = current_node.next_node

        new_node.next_node = current_node.next_node
        new_node.prev_node = current_node
        current_node.next_node.prev_node = new_node
        current_node.next_node = new_node

        return f"Элемент с данными {data} был вставлен на позицию {index}"

    def remove_node_index(self, index):

        """ Удаление элемента по указанному индексу """

        if index < 0 or index >= self.len_ll():
            raise IndexError("Индекс вне допустимого диапазона")

        if index == 0:
            return self.remove_from_head()
        elif index == self.len_ll() - 1:
            return self.remove_from_tail()

        current_node = self.head
        for _ in range(index):  # Двигаемся до нужного индекса
            current_node = current_node.next_node

        removed_node = current_node
        current_node.prev_node.next_node = current_node.next_node
        current_node.next_node.prev_node = current_node.prev_node

        return f"Удалена нода с данными {removed_node.data} на позиции {index}"

    def remove_node_data(self, data):

        """ Удаление первого узла с указанными данными """

        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                break
            current_node = current_node.next_node

        if current_node is None:
            return f"Ноды с данными '{data}' не найдено."

        if current_node == self.head:
            return self.remove_from_head()
        elif current_node == self.tail:
            return self.remove_from_tail()

        current_node.prev_node.next_node = current_node.next_node
        current_node.next_node.prev_node = current_node.prev_node

        return f"Узел с данными {current_node.data} успешно удалён."

    def len_ll(self):

        """ Возвращает длину связного списка """

        length = 0
        current_node = self.head
        while current_node is not None:
            length += 1
            current_node = current_node.next_node
        return length

    def contains_from_head(self, data):

        """ Проверка наличия данных в списке начиная с головы """

        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                return True
            current_node = current_node.next_node
        return False

    def contains_from_tail(self, data):

        """ Проверка наличия данных в списке начиная с хвоста """

        current_node = self.tail
        while current_node is not None:
            if current_node.data == data:
                return True
            current_node = current_node.prev_node
        return False

    def contains_from(self, data, start_from="head"):

        """ Универсальная проверка наличия данных в списке, можно выбрать начало поиска """

        if start_from == "head":
            return self.contains_from_head(data)
        elif start_from == "tail":
            return self.contains_from_tail(data)
        else:
            raise ValueError("Параметр 'start_from' должен быть 'head' или 'tail'")