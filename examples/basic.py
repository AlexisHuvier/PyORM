from pyorm import Table, Database, Column
from pyorm.utils import ValueType

import os

class Person(Table):
    columns = {
        "id": Column("id", type_=ValueType.INT, primary_key=True, auto_increment=True),
        "name": Column("name", type_=ValueType.VARCHAR, not_null=True)
    }
    db = Database("module=sqlite;db="+os.path.dirname(__file__)+"/base.db")

Person.create()
Person.delete_all()
print(Person.get_all())
michel = Person(name="Michel")
print(michel)
michel.save()
for i in Person.get_all():
    print(i)