import sqlite3, datetime
#table name for SQLite_Python.db is SqliteDb_images

def converToBinary(filename):
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def insertBLOB(id, name, date, image):
    try:
        sqliteConnection = sqlite3.connect('SQLite_Python.db')
        cursor = sqliteConnection.cursor()

        insert_query = """ INSERT INTO SqliteDb_images
                            (id, name, input_date, image) VALUES (?, ?, ?, ?)"""
        
        img = converToBinary(image)
        
        data_tuple = (id,name,date,image)
        cursor.execute(insert_query, data_tuple)
        sqliteConnection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Error while creating a sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
        print("sqlite connection is closed")


if __name__=='__main__':
    x = datetime.datetime.now()
    insertBLOB(1, "cat :3", x.strftime("%x"), "cat.jpg")