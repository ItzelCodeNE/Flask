import sqlite3,hashlib

#deprecated class

class connectionDb:

    def __init__(self, connection):
        self.connection = connection
        



    def GetTable(self,table):    
        ReturnTable = self.connection.cursor()
        SQL = '''SELECT * FROM {0}'''
        ReturnTable.execute(SQL.format(table))
        Table = ReturnTable.fetchall()
        self.close()
        return Table
    

    def AddUser(self,Username,password):
        InsertUser = self.connection().cursor()
        SQL = '''INSERT INTO Users (Username,Password) VALUES ('{0}','{1}')'''
        InsertUser.execute(SQL.format(Username,password))
        self.connection.commit()
        self.close()
    
    def RemoveUser(self,ID):
        Remove = self.connection.cursor()
        SQL = '''DELETE FROM Users WHERE id = {0}'''
        Remove.execute(SQL.format(ID))
        self.connection.commit()
        self.close()

    def FindUser(self,Username):
        find = self.connection.cursor()
        SQL = '''SELECT * FROM Users'''
        find.execute(SQL)
        UsersTable = find.fetchall()
        for i in range(len(UsersTable)):
            if Username == UsersTable[i][1]:
                return 1
            if i == len(UsersTable)-1:
                return 0
        self.close()
        
            
    def Login(self,Username,password):
        ver = self.connection.cursor()
        SQL = ''' SELECT * FROM Users WHERE Username = '{0}' '''
        ver.execute(SQL.format(Username))
        Table = ver.fetchall()
        self.close()
        
        
        if self.FindUser(Username):
         
            if password == Table[0][2]:
                print('Login granted')
            else:
                print('Wrong password')
        else: print('User not found')
       
    

    



            
           



  



        

