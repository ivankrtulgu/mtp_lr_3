class Document:
    def info(self):
        pass


class Book(Document):
    def info(self):
        return "Документ: книга"


class Report(Document):
    def info(self):
        return "Документ: отчёт"


class DocumentFactory:
    @staticmethod
    def create(doc_type):
        types = {
            "book": Book,
            "report": Report
        }

        if doc_type not in types:
            print("Неизвестный тип документа")
            return
        
        return types[doc_type]()


first_document = DocumentFactory.create("book")
second_document = DocumentFactory.create("report")
print(first_document.info())
print(second_document.info())
