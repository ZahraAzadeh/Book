class Book:
    def __init__(self, title="", author="", year=""):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        self.title = input("Please enter your book title: ")
        self.author = input("Please enter your book author: ")
        self.year = input("Please enter your book year: ")

    def show_info(self):
        print("\n📖 book atributes 📖")
        print(f"title: {self.title}")
        print(f"Autho: {self.author}")
        print(f"Book year: {self.year}")


book1 = Book()
book1.get_info()
book1.show_info()
