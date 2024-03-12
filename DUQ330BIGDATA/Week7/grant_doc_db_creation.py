import sqlite3

#Writing SQL Query
query = '''
CREATE TABLE IF NOT EXISTS npi (
    id INTEGER PRIMARY KEY,
    lastname VARCHAR(100) NOT NULL,
    forename VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

'''

query2 = '''
CREATE TABLE IF NOT EXISTS grants (
    id INTEGER PRIMARY KEY,
    lastname VARCHAR(100) NOT NULL,
    forename VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

'''

conn = sqlite3.connect('data/grant_npi.db')
cursor = conn.cursor()

version_query = 'select sqlite_version()'
cursor.execute(version_query)

record = cursor.fetchall()
print('version is', record)

cursor.close()