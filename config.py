ambiente = 'desenvolvimento'

if ambiente == 'desenvolvimento':
    DB_HOST = 'localhost'
    DB_USER = 'root'
    DB_PASSWORD = 'senai'
    DB_NAME = 'emprego'

#COMFIG CHAVE SECRETA (SESSION)
SECRET_KEY = 'emprego'

#ACESSO DO ADMIN
MASTER_EMAIL = 'adm@adm'
MASTER_PASSWORD = 'adm'
