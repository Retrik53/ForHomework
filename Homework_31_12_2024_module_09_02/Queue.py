class Queue:

    """Класс для представления очереди символов."""

    def __init__(self, max_size):

        """Инициализация объекта очереди."""

        self.max_size = max_size
        self.queue = [None] * max_size
        self.front = 0
        self.rear = -1
        self.size = 0

    def is_empty(self):

        """Проверка, является ли очередь пустой."""

        return self.size == 0

    def is_full(self):

        """Проверка, является ли очередь полной."""

        return self.size == self.max_size

    def enqueue(self, item):

        """Добавление элемента в конец очереди."""

        if self.is_full():
            raise ValueError("Очередь переполнена.")
        else:
            self.rear = (self.rear + 1) % self.max_size
            self.queue[self.rear] = item
            self.size += 1

    def dequeue(self):

        """Удаление элемента из начала очереди."""

        if self.is_empty():
            raise IndexError("Очередь пуста.")
        else:
            item = self.queue[self.front]
            self.front = (self.front + 1) % self.max_size
            self.size -= 1
            return item

    def show(self):

        """Отображение всех элементов очереди на экране."""

        print("Элементы очереди:")
        for i in range(self.size):
            index = (self.front + i) % self.max_size
            print(f"{i + 1}. {self.queue[index]}")

def main():
    max_size = int(input("Введите максимальный размер очереди: "))
    q = Queue(max_size)

    while True:
        print("\nМеню операций:")
        print("1. Проверить очередь на пустоту")
        print("2. Проверить очередь на заполненность")
        print("3. Добавить элемент в очередь")
        print("4. Удалить элемент из очереди")
        print("5. Показать все элементы очереди")
        print("6. Выход")

        choice = input("Выберите операцию (1-6): ")

        if choice == '1':
            if q.is_empty():
                print("Очередь пуста.")
            else:
                print("Очередь не пуста.")
        elif choice == '2':
            if q.is_full():
                print("Очередь полна.")
            else:
                print("Очередь не полна.")
        elif choice == '3':
            item = input("Введите символ для добавления в очередь: ")
            try:
                q.enqueue(item)
                print(f"Элемент '{item}' успешно добавлен в очередь.")
            except ValueError as e:
                print(e)
        elif choice == '4':
            try:
                item = q.dequeue()
                print(f"Элемент '{item}' удален из очереди.")
            except IndexError as e:
                print(e)
        elif choice == '5':
            q.show()
        elif choice == '6':
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()