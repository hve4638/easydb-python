from .dbbuilder import DBBuilder

"""
primarykey는 하나만 지정 가능 (sqlite는 합성키를 지원하나 구현하지 않음)
auto_increment는 interger
"""
class TableBuilder(DBBuilder):
    def setup(self):
        self.schemas = []

    def preexecute(self):
        frag = ", ".join(self.schemas)
        self.query += f"({frag})"

    def __addschema(self, name, datatype, unique, notnull, primarykey, auto_increment):
        schema = f"{name} {datatype}"

        if unique:
            schema += " UNIQUE"
        if notnull:
            schema += " NOT NULL"
        if primarykey:
            schema += " PRIMARY KEY"
            if auto_increment:
                schema += " AUTOINCREMENT"
        self.schemas.append(schema)

    def text(self, name, unique:bool=False, notnull=False, primarykey=False):
        self.__addschema(name, datatype="TEXT", unique=unique, notnull=notnull, primarykey=primarykey, auto_increment=False)
        return self

    def numeric(self, name, unique:bool=False, notnull=False, primarykey=False):
        self.__addschema(name, datatype="NUMERIC", unique=unique, notnull=notnull, primarykey=primarykey, auto_increment=False)
        return self
    
    def integer(self, name, unique:bool=False, notnull=False, primarykey=False, auto_increment=False):
        self.__addschema(name, datatype="INTEGER", unique=unique, notnull=notnull, primarykey=primarykey, auto_increment=auto_increment)
        
        return self

    def real(self, name, unique:bool=False, notnull=False, primarykey=False):
        self.__addschema(name, datatype="REAL", unique=unique, notnull=notnull, primarykey=primarykey, auto_increment=False)
        
        return self

    def blob(self, name, unique:bool=False, notnull=False, primarykey=False):
        self.__addschema(name, datatype="BLOB", unique=unique, notnull=notnull, primarykey=primarykey, auto_increment=False)
        
        return self
