__all__ = "Table"

class Table:
    def __init__(self, db):
        self.db = db
        print([i for i in self.__dir__() if "__" not in i and i != "db"])