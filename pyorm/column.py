from pyorm.utils import ValueType

__all__ = ["Column"]

class Column:
    def __init__(self, type_=ValueType.INT, primary_key=False, not_null = False, unique = False, auto_increment = False, default = None):
        self.type_ = type_
        self.primary_key = primary_key
        self.not_null = not_null
        self.default = default
        self.unique = unique
        self.auto_increment = auto_increment