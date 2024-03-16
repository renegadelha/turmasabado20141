import psycopg2

def conectar_local_bd():
    con = psycopg2.connect(
        host = 'localhost',
        database = 'ferascomp',
        user = 'postgres',
        password = '12345'
    )
    return con

def conectar_cloud_db():
    con = psycopg2.connect(
        host = 'dpg-cnqu148l5elc73avqjlg-a.oregon-postgres.render.com',
        database = 'ferascompcloud',
        user = 'ferascompcloud_user',
        password = '6ErVy4FPtb9T9w5gjcpJN73gbdsbN2KI'
    )
    return con

def conectar_bd():
    return conectar_cloud_db()

def verificar_login(login, senha):
    con = conectar_bd()

    cursor = con.cursor()
    cursor.execute(f"select count(*) from usuarios where email = '{login}' and senha = '{senha}'")
    if cursor.fetchall()[0][0] == 1:
        return True
    else:
        return False

