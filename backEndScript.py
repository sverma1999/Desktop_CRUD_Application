import psycopg2


class Database:
    """
    This class gets all data from database and send it back to front end class.
    """
    def __init__(self, db):
        self.conn = psycopg2.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS employeesList (id INT PRIMARY KEY, employeeName text, company text, position text, salary money)")
        self.cur.execute("CREATE SEQUENCE IF NOT EXISTS employeesList_sequence START 1 INCREMENT 1")
        self.conn.commit()

    def insert(self, employeeName, company, position, salary):
        self.cur.execute("INSERT INTO employeesList VALUES(nextval('employeesList_sequence'), %s,%s,%s,%s)", (employeeName, company, position, salary))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM employeesList")
        rows = self.cur.fetchall()
        return rows

    def search(self, employeeName="", company="", position="", salary=""):
        self.cur.execute("SELECT * FROM employeesList WHERE employeeName= %s OR company=%s OR  position=%s OR salary=%s", (employeeName, company, position, salary))
        rows = self.cur.fetchall()
        return rows


    def delete(self, id):
        self.cur.execute("DELETE FROM employeesList WHERE id= %s", (id,))
        self.conn.commit()


    def update(self, id, employeeName, company, position, salary):
        self.cur.execute("UPDATE employeesList SET employeeName= %s, company=%s,  position=%s, salary=%s WHERE id=%s", (employeeName, company, position, salary, id))
        self.conn.commit()

    def  __del__(self):
        self.conn.close()


#connect()
#insert("Shubham Verma", "Vestcor", "Developer",2300)
#insert("Yuvang Verma", "Vestcor", "Developer",2500)
#insert("Jack Boe", "Vestcor", "CEO",4000)
#insert("Hanson Waite", "Vestcor", "Investment Manager",2000)
#update(1, "Shubham Verma", "IBM", "Developer", 4000)
#delete(4)
#print(search(employeeName="Shubham Verma"))