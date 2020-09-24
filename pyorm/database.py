from pyorm.pdo import PDO

__all__ = "Database"

class Database:
    def __init__(self, connection_string):
        self.pdo = PDO(connection_string)
