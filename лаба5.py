class Book:
    def __init__(self, title, author, year):
        """Инициализация атрибутов книги."""
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        """Возвращает информацию о книге в заданном формате."""
        return f"Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}"

my_book = Book("1984", "Джордж Оруэлл", 1949)
print(my_book.get_info())

class Circle:
    def __init__(self, radius):
        """Инициализация радиуса круга."""
        self.radius = radius

    def get_radius(self):
        """Возвращает значение радиуса."""
        return self.radius

    def set_radius(self, new_radius):
        """Изменяет радиус круга на новый."""
        self.radius = new_radius

my_circle = Circle(5)
print(f"Текущий радиус: {my_circle.get_radius()}")
my_circle.set_radius(10)
print(f"Новый радиус: {my_circle.get_radius()}")
