from dis import pretty_flags


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return \
            (f"کتاب [{self.title}] "
             f" نویسنده [{self.author}] "
             f" سال [{self.year}]")
book1 = Book("شازده کوچولو", "آنتوان دو سنت اگزوپری", 1943)
print(book1.get_info())



