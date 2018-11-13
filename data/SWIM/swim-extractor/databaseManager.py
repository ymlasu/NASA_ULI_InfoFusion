import sqlite3
class DatabaseManager(object):
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.conn.execute('pragma foreign_keys = on')
        self.conn.commit()
        self.cur = self.conn.cursor()

    def query(self, arg):
        self.cur.execute(arg)
        self.conn.commit()
        return self.cur

    def insert_line(self, table, cols, vals):
       sql_command='INSERT INTO {} ('.format(table)
       sql_command = [sql_command+col 

    def close(self):
        self.conn.close()

    def create_table(self,table,cols,opts = None):
        sql_command = 'CREATE TABLE {} ('.format(table)
        sql_command = [sql_command+col+',' for col in cols[:-1]]
        sql_command = sql_command+'{})'.format(col[-1])
        
        if rewrite:
            self.delete_table(table)
            self.query(sql_command)

    def delete_table(self,table):
        self.query('DROP TABLE IF EXISTS {}'.format(table))

