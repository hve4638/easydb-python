#!/usr/bin/env python3
from easydb import *

if __name__ == "__main__":
    db = EasyDB()
    
    tablebuilder = db.create_table('chart')\
        .text('title')\
        .text('message', unique=True, notnull=True)\
        .execute()
    
    db.insert('chart',
        { 'title': 'DB Example', 'message': 'hello world!' }
    ).execute()

    count = db.select_count('chart').execute().one()
    print(f'count: {count}')

    result = db.select('chart', ['title', 'message']).execute()
    print(result.one())