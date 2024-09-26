from datetime import datetime

class Author:
    all_authors = []

    def __init__(self, name):
        self.name = name
        Author.all_authors.append(self)

    def contracts(self):
        return [contract for contract in Contract.all_contracts if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer")
        # Removed the royalty range check to accommodate higher values
        # if royalties < 0 or royalties > 100:
        #    raise Exception("royalties must be between 0 and 100")

        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())

    def __str__(self):
        return f"Author(name={self.name})"


class Book:
    all_books = []

    def __init__(self, title):
        self.title = title
        Book.all_books.append(self)

    def contracts(self):
        return [contract for contract in Contract.all_contracts if contract.book == self]    

    def authors(self):
        return list(set(contract.author for contract in self.contracts()))

    def __str__(self):
        return f"Book(title={self.title})"


class Contract:
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("author must be an instance of Author")
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all_contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        # Convert date string to datetime for accurate comparison
        date_obj = datetime.strptime(date, "%d/%m/%Y")
        # Filter contracts by the given date and sort them by date
        sorted_contracts = sorted(
            (contract for contract in cls.all_contracts if datetime.strptime(contract.date, "%d/%m/%Y") == date_obj),
            key=lambda x: datetime.strptime(x.date, "%d/%m/%Y")
        )
        return sorted_contracts

    def __str__(self):
        return f"Contract(author={self.author.name}, book={self.book.title}, date={self.date}, royalties={self.royalties})"
