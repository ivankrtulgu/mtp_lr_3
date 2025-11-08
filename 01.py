class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"«{self.title}» — {self.author}"


first_book = Book("Преступление и наказание", "Ф. Достоевский")
second_book = Book("Властелин Колец. Том 1. Братство кольца.", "Дж. Р. Р. Толкин")
print(first_book)
print(second_book)
