import json
import pickle


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        print(f"Title: {self.title}, Author: {self.author}, Year: {self.year}")

    def update_author(self, new_author):
        self.author = new_author

    class BookEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, Book):
                return {
                    'title': obj.title,
                    'author': obj.author,
                    'year': obj.year
                }
            return super().default(obj)

    def to_json(self):
        return json.dumps(self, cls=Book.BookEncoder)

    @staticmethod
    def from_json(json_str):
        data = json.loads(json_str)
        book = Book(data['title'], data['author'], data['year'])
        return book

    def to_pickle(self):
        return pickle.dumps(self)

    @staticmethod
    def from_pickle(pickled_data):
        return pickle.loads(pickled_data)

book = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)

book.info()

book.update_author("Francis Scott Key Fitzgerald")
book.info()

json_book = book.to_json()
print(json_book)

new_book = Book.from_json(json_book)
new_book.info()

pickled_book = book.to_pickle()

unpickled_book = Book.from_pickle(pickled_book)
unpickled_book.info()