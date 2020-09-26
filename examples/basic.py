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
Person(name="Lyos").save()
Person(name="Hugo").save()
print(Person.get_one("name = 'Hugo'"))
for i in Person.get_all("name = 'Lyos'"):
    print(i)