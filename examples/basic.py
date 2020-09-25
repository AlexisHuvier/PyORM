from pyorm import Table, Database, Column
from pyorm.utils import ValueType

class Person(Table):
    id = Column(type_=ValueType.INT, primary_key=True, unique=True, auto_increment=True, not_null=True)
    name = Column(type_=ValueType.VARCHAR, not_null=True)
    db = Database("module=sqlite;db=base.db")

michel = Person(id=1, name="Michel")
print(michel.id)
print(michel.name)
print(michel)
michel.id = 4
print(michel.id)
print(michel)