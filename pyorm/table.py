__all__ = "Table"

from pyorm.column import Column

class Table:
    db = None

    def __init__(self, **args):
        self.values = {}
        self.columns = {}
        for i in [i for i in self.__dir__() if '__' not in i and i not in ["db", "values"]]:
            if isinstance(self.__getattribute__(i), Column):
                self.columns[i] = self.__getattribute__(i)
        for k, v in args.items():
            if k in self.columns.keys():
                self.values[k] = v
            else:
                raise ValueError("Unknown Column : "+k)
        print(self.values)
        print(self.columns)

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