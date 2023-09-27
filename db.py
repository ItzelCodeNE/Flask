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

    def Login(connection,Username,password):
        ver = connection.cursor()
        SQL = ''' SELECT * FROM Users WHERE Username = '{0}' '''
        ver.execute(SQL.format(Username))
        Table = ver.fetchall()
        print(Table)

        if password == Table[0][2]:
            print('Login granted')
        else:
            print('Wrong password')

    def FindUser(connection,Username):
        find = connection.cursor()
        SQL = '''SELECT * FROM Users'''
        find.execute(SQL)
        UsersTable = find.fetchall()
        for i in range(len(UsersTable)):
            if Username == UsersTable[i][1]:
                return 1
            if i == len(UsersTable)-1:
                return 0
           



  



        

