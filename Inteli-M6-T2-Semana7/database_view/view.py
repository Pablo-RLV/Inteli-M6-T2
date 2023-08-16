import sqlite3

def writeTofile(data, filename):
    with open(filename, 'wb') as file:
        file.write(data)

def readBlobData(imgId):
    try:
        sqliteConnection = sqlite3.connect('/data.db')
        cursor = sqliteConnection.cursor()
        sql_fetch_blob_query = """SELECT * from imagens where id = ?"""
        cursor.execute(sql_fetch_blob_query, (imgId,))
        record = cursor.fetchall()
        for row in record:
            print("Id = ", row[0], "Name = ", row[1])
            name = row[1]
            photo = row[2]
            photoPath = "/database_view/" + name
            writeTofile(photo, photoPath)
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to read blob data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()

readBlobData(1)
readBlobData(2)
readBlobData(3)
readBlobData(4)