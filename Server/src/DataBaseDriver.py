# סרבר הראשון
import sqlite3
from sqlite3 import Error
import multiprocessing
import threading

dbDir=r'..//db//database1.db'

class DataBase:
    def __init__(self):
        self.con = self.create_connection(dbDir)
        self.cursor = self.define_cursor()
        self.create_table()
        self.lock = threading.Lock()


    # נעילת המנעול
    def lockAcquire(self):
        self.lock.acquire()


    # שיחרור המנעול
    def lockRelease(self):
        self.lock.release()

    """ create a database connection to the SQLite database
            specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """

    def create_connection(self, db_file):
        connection = None
        try:
            connection = sqlite3.connect(db_file,check_same_thread=False)
            return connection
        except Error as e:
            print(e)

        return connection

    """ create a cursor
        param : connection
        return: cursor
        """

    def define_cursor(self):
        return self.con.cursor()

    """ create a table
        param : 
        return: 1 success , 0 error
        """

    def create_table(self):
        sql = """create table if not exists 
         data(user_id integer primary key, name text not null, per text not null);"""
        try:
            self.cursor.execute(sql)
            return 1
        except Error as e:
            print(e)
            return 0

    """ close connection
        param : 
        return: 1 success , 0 error
        """

    def close_connection(self):
        try:
            self.con.close()
            return 1
        except Error as e:
            print(e)
            return 0

    """ save data base
        param : 
        return: 1 success , 0 error
        """

    def save(self):
        try:
            self.con.commit()
            return 1
        except Error as e:
            print(e)
            return 0

    """ insert values into the data base
        param : id, name, per
        return: 1 success , 0 error
        """

    def insert_values(self, id, name, per):
        try:
            self.lockAcquire()
            self.cursor.execute("INSERT INTO data VALUES (?,?,?)", (id, name, per))
            self.save()
            self.lockRelease()
            return 1
        except Error as e:
            print(e)
            self.lockRelease()
            return 0

    """ update values in the data base
        param :  id, name, per
        return: 1 success , 0 error
        """

    def update(self, id, name, per):
        try:
            self.cursor.execute("UPDATE data SET name=?  WHERE user_id=?", (name, id))
            self.cursor.execute("UPDATE data SET per=?  WHERE user_id=?", (per, id))
            # cursor.execute('Update data set name=? per=? where user_id=?', (name, per, id))
            self.save()
            return 1
        except Error as e:
            print(e)
            return 0

    """ delete values from the data base
        param : cursor, id, name, per
        return: 1 success , 0 error
        """

    def delete(self, id):
        sql = 'DELETE FROM data WHERE user_id=?'
        try:
            self.lockAcquire()
            self.cursor.execute(sql, (id,))
            self.save()
            self.lockRelease()
            return 1
        except Error as e:
            print(e)
            self.lockRelease()
            return 0

    """ get all users  from the data base
            param : 
            return: results , 0 error
            """
    def getAll(self):
        sql="SELECT * FROM data"
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            return results
        except Error as e:
            return 0

    """ get one  user  from the data base
               param : id
               return: 1 success , 0 error
               """
    def getById(self,id ):
        sql="SELECT * FROM data WHERE user_id=?"
        try:
            self.cursor.execute(sql, (id,))
            results=self.cursor.fetchall()
            return results
        except Error as e:
            return 0

    def getPerById(self):
        data=self.getById
        per=data["per"]
        return per
'''
def main():
    db = DataBase()
    

    # add to sql
    db.insert_values(1556341, 'yigal1', ' r')
    db.insert_values(1556342, 'yigal2', ' r')
    db.insert_values(1556343, 'yigal3', ' r')
    db.insert_values(1556344, 'yigal4', ' r')

    print(db.getById(556342))
    #print(db.getAll())


    x = db.update( 556341, 'pretty1 ', 'rw')
    print('update:')
    print(x)

    y = db.delete( 556341)
    print('delete:')
    print(y)

    db.insert_values( 556341, 'yigal', ' r')
    db.save()
    # get results
    print(db.getAll())
    #cursor.execute("SELECT * FROM data")

    db.close_connection()


if __name__ == "__main__":
    main()

'''