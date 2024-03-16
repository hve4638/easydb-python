class QueryResult:
    def __init__(self, cursor, onprocess=None):
        self.cursor = cursor
        if onprocess:
            self.onprocess = onprocess
        else:
            self.onprocess = lambda x : x

    def one(self):
        return self.onprocess(self.cursor.fetchone())
    
    def all(self):
        result = []
        for item in self.cursor.fetchall():
            result.append(self.onprocess(item))
        return result
    
    def many(self, n:int):
        result = []
        for item in self.cursor.fetchmany(n):
            result.append(self.onprocess(item))
        return result