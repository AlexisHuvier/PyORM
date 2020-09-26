from pyorm.utils import ValueType

__all__ = ["Column"]

class Column:
    def __init__(self, name, type_=ValueType.INT, primary_key=False, not_null = False, unique = False, auto_increment = False, default = None):
        self.name = name
        self.type_ = type_
        self.primary_key = primary_key
        self.not_null = not_null
        self.unique = unique
        self.auto_increment = auto_increment
        self.default = default
    
    def get_sql_description(self):
        parts = [self.name, self.type_]
        if self.primary_key:
            parts.append("PRIMARY KEY")
        if self.auto_increment:
            parts.append("AUTOINCREMENT")
        if self.not_null:
            parts.append("NOT NULL")
        if self.unique:
            parts.append("UNIQUE")
        if self.default is not None:
            parts.append("DEFAULT "+str(self.default))
        
        return " ".join(parts)
    
    def __str__(self):
        return self.name+"(type = {}, primary_key = {}, not_null = {}, unique = {}, auto_increment = {}, default = {})".format(
            self.type_, self.primary_key, self.not_null, self.unique, self.auto_increment, self.default
        )