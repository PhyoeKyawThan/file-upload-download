from sqlalchemy import create_engine, Table, MetaData, Column, Integer, String

class CreateDB():
    def __init__(self) -> None:
        self.engine = create_engine("mysql://root:Domak9090@127.0.0.1:3306/file")
        metadata = MetaData()
        self.table_name = "fileData"
        self.table = Table(self.table_name, metadata, 
                      Column('id', Integer, primary_key=True),
                      Column('fileName', String(20), nullable=False), 
                      Column('filePath', String(225), nullable=False))
        metadata.create_all(self.engine)

class DB(CreateDB):
    def insert(self, data: list):
        self.conn      = self.engine.connect()
        self.conn.execute(self.table.insert(), data)
        self.conn.commit()
        self.conn.close()
    
    def delete(self, id: int):
        self.conn      = self.engine.connect()
        self.conn.execute(self.table.delete().where(self.table.c.id == id))
        self.conn.commit()
        self.conn.close()

    def show(self):
        self.conn      = self.engine.connect()
        return self.conn.execute(self.table.select())
    
        
if __name__=='__main__':
    db = DB()
    db.insert([{'fileName': 'python', 'filePath': '/dir/test/test.pdf'}])
    