class Node:

    """Класс узла связного списка."""

    def __init__(self, data, next_node=None):

        """Инициализация узла."""

        self.data = data
        self.next_node = next_node


class Stack:

    """Реализация стека на основе связного списка."""

    def __init__(self, stack_size=5, top=None):

        """Инициализация стека."""

        self.stack_size = stack_size
        self.top = top

    def push(self, data):

        """Добавление элемента в стек."""

        if self.size_stack() < self.stack_size:
            new_node = Node(data)
            new_node.next_node = self.top
            self.top = new_node
        else:
            print("Стек переполнен")
            return "Стек переполнен"

    def pop(self):

        """Извлечение последнего элемента из стека."""

        if self.top:
            remove_last = self.top
            self.top = self.top.next_node
            return remove_last.data
        else:
            return "Стек пуст"

    def is_empty(self):

        """Проверка, пуст ли стек полностью."""

        if self.top:
            return False
        else:
            return True

    def is_full(self):

        """Проверка, заполнен ли стек до максимума."""

        if self.stack_size == self.size_stack():
            return True
        else:
            return False

    def clear_stack(self):

        """Очистка всего содержимого стека."""

        while self.top:
            self.pop()

    def get_data(self, index):

        """Получение данных по индексу в стеке."""

        counter = 0
        stack_item = self.top
        while stack_item:
            if counter == index:
                return stack_item.data
            stack_item = stack_item.next_node
            counter += 1
        return f"Out of range"

    def size_stack(self):

        """Подсчет количества элементов в стеке."""

        counter = 0
        stack_item = self.top
        while stack_item:
            counter += 1
            stack_item = stack_item.next_node
        return counter

    def counter_int(self):

        """Подсчет количества целых чисел в стеке."""

        counter = 0
        stack_item = self.top
        while stack_item:
            if isinstance(stack_item.data, int):
                counter += 1
            stack_item = stack_item.next_node
        return counter