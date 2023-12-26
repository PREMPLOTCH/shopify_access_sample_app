from config import Config

class DatabaseCoordinator(object):
    def __init__(self):
        self.mysql_conn = Config.MYSQL_CONN

    def add_token_db(self, shop, access_token):
        insert_query = "INSERT INTO access_tokens(shop_domain, access_token) VALUES (%s, %s)"
        return self.mysql_conn.write_db(insert_query, (shop, access_token))