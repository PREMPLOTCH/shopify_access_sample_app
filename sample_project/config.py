from app.connections import SqlConnection

class Config:

    VERSIONS_ALLOWED = ['1']


    MYSQL_CONFIG = {
    'host': 'localhost', 
    'user': 'root',    
    'password': 'Root#04', 
    'database': 'customers'   
    }
    MYSQL_CONN = SqlConnection(MYSQL_CONFIG)
    
    APP_API_KEY = '3c4aaa4d17841e0533296913635b9d1a'
    APP_API_SECRET = '11034f4184747a4f30646dff2efbf13d'
    APP_REDIRECT_URL = 'http://127.0.0.1:5000/api/callback'
    APP_AUTH_BASE_URL = 'https://quickstart-ee5cbf78.myshopify.com/admin/oauth/authorize'
    APP_TOKEN_URL = 'https://quickstart-ee5cbf78.myshopify.com/admin/oauth/access_token'

    TABLE_NAME = 'access_tokens'
    COLUMN_NAMES = 'id,token,created_at,updated_at'.split(',')
