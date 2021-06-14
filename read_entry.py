import sqlite3

def writeTofile(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(decode(data))
    print("Stored blob data into: ", filename, "\n")

def readBlobData(id):
    try:
        sqliteConnection = sqlite3.connect('SQLite_Python.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_fetch_blob_query = """SELECT * from SqliteDb_images WHERE id = ?"""
        cursor.execute(sql_fetch_blob_query, (id,))
        record = cursor.fetchall()
        for row in record:
            print("id = ", row[0], "name = ", row[1])
            name = row[1]
            photo = row[3]

            print("Storing image on disk \n")
            photoPath = "C:\\Users\\reyes\\Desktop\\python\\imageAPI\\storage\\" + name + ".jpg"
            writeTofile(photo, photoPath)

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read blob data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")

readBlobData(1)
