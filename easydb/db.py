import os, sys
import sqlite3
from .querybuilder import QueryBuilder
from .tablebuilder import TableBuilder

class EasyDB:
    def __init__(self, filename=':memory:', verbose=False):
        self.filename = filename
        self.conn = sqlite3.connect(self.filename)
        self.verbose = verbose
        self.closed = False

    def __enter__(self):
        return self
    
    def __exit__(self, type, value, trackback):
        self.conn.commit()
        self.conn.close()
        return self

    def close(self):
        if not self.closed:
            self.closed = True
            self.conn.close()

    def commit(self):
        self.conn.commit()

    def cursor(self):
        return self.conn.cursor()
    
    def query(self, query, params=[]):
        return QueryBuilder(self.conn, query, params)

    def fields(self, table:str):
        cur = self.cursor()
        cur.execute(f'PRAGMA table_info({table})')
        fields = cur.fetchall()
        return [field[1] for field in fields]
    
    def create_table(self, table:str)->TableBuilder:
        return TableBuilder(self.cursor(), f"CREATE TABLE {table}", verbose=self.verbose)
    
    def drop_table(self, table:str)->QueryBuilder:
        return QueryBuilder(self.cursor(), f"DROP TABLE IF EXISTS {table}", verbose=self.verbose)

    def exists_table(self, table_name):
        cur = self.conn.cursor()
        query = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'"
        cur.execute(query)
        result = self.cur.fetchone()
        return result is not None
    
    def select_count(self, table:str)->QueryBuilder:
        return QueryBuilder(
            self.cursor(), 
            f"SELECT count(*) FROM {table}",
            preprocess=lambda x : x[0],
            verbose=self.verbose
        )
    
    def select_all(self, table:str)->QueryBuilder:
        return QueryBuilder(self.cursor(), f"SELECT * FROM {table}")

    def select(self, table:str, fields:list[str])->QueryBuilder:
        def preprocess(items):
            result = {}
            for i, item in enumerate(items):
                result[fields[i]] = item
            return result
        columnf = ", ".join(fields)
        params = []
        
        return QueryBuilder(
            self.cursor(), 
            f"SELECT {columnf} FROM {table}",
            preprocess=preprocess, 
            verbose=self.verbose
        )
    
    def update(self, table:str, data:dict)->QueryBuilder:
        setf = ", ".join(f"{key}=?" for key in data.keys())
        values = list(data.values())
        return QueryBuilder(self.cursor(), f"UPDATE {table} SET {setf}", values, verbose=self.verbose)

    def insert(self, table:str, data:dict)->QueryBuilder:
        keys, values = list(data.keys()), list(data.values())
        keyf = ", ".join(keys)
        valuef = ", ".join(["?" for _ in keys])
        
        query = f"INSERT INTO {table} ({keyf}) VALUES ({valuef})"
        params = values
        return QueryBuilder(self.cursor(), query, params, verbose=self.verbose)

