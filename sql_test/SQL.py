import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Lr1amor2',
    database='users'
)

cursor = db.cursor()


class DatabaseOperations:
    def __init__(self, login=None, hash=None, new_login=None, new_hash=None):
        self.login = login
        self.hash = hash
        self.new_hash = new_hash
        self.new_login = new_login

    def new_user(self):
        sql = 'INSERT INTO registers (login, hash) VALUES (%s, %s)'
        val = (f'{self.login}', f'{self.hash}')
        cursor.execute(sql, val)
        db.commit()
        print('--USUARIO RREGISTRADO--')

    def set_new_login(self, new_login):
        adr = (f'{new_login}', f'{self.login}', f'{self.hash}')
        sql = 'UPDATE registers SET login = %s WHERE login = %s AND hash = %s'
        cursor.execute(sql, adr)
        db.commit()
        self.login = new_login
        self.new_login = None

    def set_new_hash(self, new_hash):
        val = (f'{new_hash}', f'{self.login}', f'{self.hash}')
        sql = 'UPDATE registers SET hash = %s WHERE login = %s AND hash = %s' #  invalid sql syntax
        cursor.execute(sql, val)
        db.commit()
        self.hash = new_hash
        self.new_hash = None

    def set_login(self):
        self.login = str(input('Login: ')).strip()

    def set_hash(self):
        self.hash = str(input('Senha: ')).strip()

    def is_user_real(self):
        sql = 'SELECT * FROM registers WHERE login = %s AND hash = %s'
        adr = (f'{self.login}', f'{self.hash}')
        cursor.execute(sql, adr)
        result = cursor.fetchone()
        if result is None:
            return False
        else:
            print(f'--BEM VINDO(A) {self.login.upper()}--')

    def delete_acc(self):
        adr = (f'{self.login}', f'{self.hash}')
        sql = 'DELETE FROM registers WHERE login = %s and hash = %s'
        cursor.execute(sql, adr)
        db.commit()
        print('--CONTA DELETADA--')