import sqlite3, sys
from .queryresult import QueryResult

class DBBuilder:
    def __init__(self, cursor:sqlite3.Cursor, query:str, params:list=[], *, preprocess:callable=None, verbose=False):
        self.cursor = cursor
        self.query = query
        self.params = params
        self.verbose = verbose
        self.onpreprocess = preprocess
        self.setup()

    '''
    overload 전용
    '''
    def setup(self):
        pass

    '''
    overload 전용
    '''
    def preexecute(self):
        pass

    def raw(self, query):
        self.query += query + " "

    def execute(self):
        self.preexecute()
        if self.verbose:
            sys.stdout.write(f"+ {self.query}")
            if self.params:
                sys.stdout.write(f" % {self.params}")
            sys.stdout.write('\n')
        self.cursor.execute(self.query, self.params)

        return QueryResult(self.cursor, onprocess=self.onpreprocess)
