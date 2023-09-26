import sqlite3,hashlib



class connectionDb:

    
    connection = sqlite3.connect('IRSv2.db')

    def GetTable(connection,table):    
        ReturnTable = connection.cursor()
        SQL = '''SELECT * FROM {0}'''
        ReturnTable.execute(SQL.format(table))
        Table = ReturnTable.fetchall()
        return Table
    
    def AddUser(connection,Username,password):
        InsertUser = connection.cursor()
        SQL = '''INSERT INTO Users (Username,Password) VALUES ('{0}','{1}')'''
        InsertUser.execute(SQL.format(Username,password))
        connection.commit()
    
    def RemoveUser(connection,ID):
        Remove = connection.cursor()
        SQL = '''DELETE FROM Users WHERE id = {0}'''
        Remove.execute(SQL.format(ID))
        connection.commit()

  



        

