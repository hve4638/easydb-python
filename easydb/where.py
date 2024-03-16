class Where:
    def __init__(self):
        pass

    @classmethod
    def eq(cls, column, value):
        return f"{column} = '{value}'"
    
    @classmethod
    def ne(cls, column, value):
        return f"{column} != '{value}'"
    
    @classmethod
    def le(cls, column, value):
        return f"{column} <= '{value}'"
    
    @classmethod
    def ls(cls, column, value):
        return f"{column} < '{value}'"
    
    @classmethod
    def ge(cls, column, value):
        return f"{column} >= '{value}'"
    
    @classmethod
    def gt(cls, column, value):
        return f"{column} > '{value}'"
    
    @classmethod
    def AND(cls, cond1, cond2):
        return f"({cond1} AND {cond2})"
    
    @classmethod
    def OR(cls, cond1, cond2):
        return f"({cond1} OR {cond2})"
    
    @classmethod
    def NOT(cls, cond):
        return f"NOT {cond}"
    
    @classmethod
    def IN(cls, column, values):
        return f"{column} IN ({', '.join(values)})"
        