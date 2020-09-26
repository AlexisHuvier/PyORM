__all__ = "Table"

from pyorm.column import Column
from pyorm.utils import ValueType

class Table:
    columns = {}
    db = None

    def __init__(self, **args):
        self.values = {}
        for k in self.columns.keys():
            if k in args.keys():
                self.values[k] = args[k]
            else:
                self.values[k] = None

    def save(self):
        values = {}
        for k, v in self.values.items():
            if v is not None:
                if self.columns[k].type_ == ValueType.VARCHAR:
                    v = "'"+v+"'"
                values[k] = v
            elif not self.columns[k].auto_increment and self.columns[k].not_null:
                raise ValueError("Except value for column : "+k)
        self.db.pdo.execute("INSERT INTO "+self.__class__.__name__.lower()+"("+", ".join(values.keys())+") VALUES ("+", ".join(values.values())+");")

    @classmethod
    def create(cls):
        cls.db.pdo.execute("CREATE TABLE IF NOT EXISTS "+cls.__name__.lower()+"(\n"+ ",\n".join([i.get_sql_description() for i in cls.columns.values()])+"\n);")

    @classmethod
    def drop(cls):
        cls.db.pdo.execute("DROP TABLE "+cls.__name__.lower()+";")
    
    @classmethod
    def delete_all(cls):
        cls.db.pdo.execute("DELETE FROM "+cls.__name__.lower()+";")

    @classmethod
    def get_all(cls):
        cls.db.pdo.execute("SELECT * FROM "+cls.__name__.lower())
        results = cls.db.pdo.fetchall()
        final_results = []
        for result in results:
            final_results.append(eval(cls.__result_to_class(result)))
        return final_results

    @classmethod
    def __result_to_class(cls, result):
        args = {}
        for i, v in enumerate(cls.columns.keys()):
            if cls.columns[v].type_ == ValueType.VARCHAR:
                args[v] = "'"+result[i]+"'" 
            else:
                args[v] = result[i]
        return "cls("+", ".join([k + " = " + str(v) for k, v in args.items()])+")"

    def __str__(self):
        return self.__class__.__name__ + str(self.values)
    
    def __getattribute__ (self, name):
        if name == "values":
            return super().__getattribute__(name)
        if name in self.values.keys():
            return self.values[name]
        return super().__getattribute__(name)

    def __setattr__(self, name, value):
        if name == "values":
            super().__setattr__(name, value)
        if name in self.values.keys():
            self.values[name] = value
        super().__setattr__(name, value)