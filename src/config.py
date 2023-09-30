class Config:
    SECRET_KEY = 'B!1w8NAt1T^%kvhUI*S^'
    WTF_CSRF_CHECK_DEFAULT = False


class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost' #loaclhost
    MYSQL_USER = 'root'#root
    MYSQL_PASSWORD =''
    MYSQL_DB = 'flask_login'


config = {
    'development': DevelopmentConfig
}