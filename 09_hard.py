from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def info(self):
        pass

class Book(Document):
    def info(self):
        return "Документ: книга"

class Report(Document):
    def info(self):
        return "Документ: отчёт"

class Article(Document):
    def info(self):
        return "Документ: статья"

book = Book()
print(book.info())

report = Report()
print(report.info())

article = Article()
print(article.info())