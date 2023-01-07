import psycopg2

# Variable to connect to psycopg2 to our postgress chinook database
connection = psycopg2.connect(database="chinook")

# build a cursosr object of the database and strage in a variable, Essentially, anything that we query from the database will become part of this cursor object,
# and to read that data, we should iterate over the cursor using a for-loop, as an example.
cursor = connection.cursor()


# Query 1 - Select all records from the "Artist" Table
# cursor.execute('SELECT * FROM "Artist"')

# Query 2 - select only the "Name" column from the "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - select only "Queen" from the "Artist" table
cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Milton Nascimento"])

# Query 4 - select only by "ArtistId" #51 from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# Query 5 - select only the albums with "ArtistId" #51 on the "Album" table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# Query 6 - select all tracks where the composer is "Queen" from the "Track" table
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])


# fetch the resuts (Multiple).
# Before we start to query the database, we need to set up a way for our data to be retrieved,
# or fetched, from the cursor.
# I'm going to assign this to a variable of 'results' since it'll fetch any result that gets queried.

# Please note, if we need to query multiple records from our database, we should use the
# .fetchall() method.
results = cursor.fetchall()

# fetch the result (single)
# results = cursor.fetchone()

# close the connectio
connection.close()

# print results
for result in results:
    print(result)
