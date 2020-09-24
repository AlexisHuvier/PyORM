from pyorm import Table, Database

class Person(Table):
    id = 3
    name = 4
    deptno = 5

db = Database("module=sqlite;db=base.db")