import sqlite3

#Connecting to database
conn = sqlite3.connect('data/grant_npi.db')
cursor = conn.cursor()

query = '''
INSERT INTO npi_grants_bridge (npi_id, grants_id)
SELECT npi.id AS npi_id, grants.id AS grants_id
FROM npi, grants;

'''

#Executing Queries
cursor.execute(query)

#Selecting Version
version_query = 'select sqlite_version()'
cursor.execute(version_query)
record = cursor.fetchall()
print('version is', record)

cursor.close()