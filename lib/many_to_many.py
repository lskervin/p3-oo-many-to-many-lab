class Author:
    def __init__(self, name):
        self.name = name

    def contracts(self):
        contract_list = []
        for contract in Contract.all:
            if contract.author == self:
                contract_list.append(contract)
        return contract_list

    def books(self):
        book_list = []
        for contract in Contract.all:
            if contract.author == self:
                book_list.append(contract.book)
        return book_list

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        total = 0
        for contract in Contract.all:
            if contract.author == self:
                total += contract.royalties
        return total

class Book:
    def __init__(self, title):
        self.title = title

    def contracts(self):
        contract_list = []
        for contract in Contract.all:
            if contract.book == self:
                contract_list.append(contract)
        return contract_list

    def authors(self):
        author_list = []
        for contract in Contract.all:
            if contract.book == self:
                author_list.append(contract.author)
        return author_list
    
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        if isinstance(new_title, str):
            self._title = new_title
        return self._title


class Contract:
    all = []
    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]


    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if isinstance(new_author, Author):
            self._author = new_author
        return self._author

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, new_book):
        if isinstance(new_book, Book):
            self._book = new_book
        return self._book

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, new_date):
        if isinstance(new_date, str):
            self._date = new_date
        return self._date

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, new_royalties):
        if isinstance(new_royalties, int):
            self._royalties = new_royalties
        return self._royalties