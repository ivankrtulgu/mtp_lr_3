class FileManager:
    @staticmethod
    def write(path, content):
        with open(path, "w", encoding="utf-8") as file:
            file.write(content)

    @staticmethod
    def read(path):
        with open(path, "r", encoding="utf-8") as file:
            return file.read()


FileManager.write("test.txt", "Тестовый файл для задания 9")
print(FileManager.read("test.txt"))
