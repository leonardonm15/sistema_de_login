from sql_test import SQL
from menu_lib import Menu
database = SQL.DatabaseOperations()
acesso = False

if __name__ == '__main__':
    while True:
        options = Menu('Logar', 'Nova Conta', 'Sair')
        options.interface()
        x = options.input()
        if x is 0:
            database.set_login(), database.set_hash()
            if database.is_user_real() is False:
                print('--CREDENCIAIS ERRADAS--')
                continue
            else:
                acesso = True
                print('---ACESSO CONCEDIDO--')
                options2 = Menu('Deslogar', 'Trocar senha', 'Mudar login', 'Deletar Conta')
                while acesso:
                    options2.interface()
                    y = options2.input()
                    if y == 0:
                        acesso = False
                    if y == 1:
                        new_hash = str(input('Nova senha: ')).strip()
                        database.set_new_hash(new_hash)
                        print('--NOVA SENHA REGISTRADA--')
                        continue
                    if y == 2:
                        new_login = str(input('Novo login: ')).strip()
                        database.set_new_login(new_login)
                        print('--NOVO LOGIN REGISTRADO--')
                        continue
                    if y == 3:
                        database.delete_acc()
                        break

        if x is 1:
            database.set_login()
            database.set_hash()
            database.new_user()
            print('--NOVO CADASTRO CIRADO--')
            continue
        if x is 2:
            print('--SAINDO--')
            break
