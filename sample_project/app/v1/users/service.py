from app.v1.users import coordinator
from app.v1.users.coordinator import DatabaseCoordinator
from flask import request, redirect
import requests
from config import Config
class SubApp1Service:

    def __init__(self, params, headers):
        self.params = params
        self.headers = headers
        self.Coordinator = DatabaseCoordinator()

    def get_static_api_response(self):
        return self.params, 'success'

    def index(self):
        return 'Hello, welcome to your app!'

    def install(self):
        shop = request.args.get('shop')
        auth_url = "{}?client_id={}&redirect_uri={}&grant_options[]=per-user".format(Config.APP_AUTH_BASE_URL, Config.APP_API_KEY, Config.APP_REDIRECT_URL)
        return redirect(auth_url)

    def oauth_callback(self):
        code = request.args.get('code')
        shop = request.args.get('shop')
        token_url = Config.APP_TOKEN_URL.format(shop=shop)
        data = {
            'client_id': Config.APP_API_KEY,
            'client_secret': Config.APP_API_SECRET,
            'code': code
        }
        print('Authorization Code:{}'.format(code))
        response = requests.post(token_url, data=data)
        if response.ok:
            access_token = response.json().get('access_token')
            print('access token: {}'.format(access_token))
            self.store_access_token_in_db(shop, access_token)
            return redirect('https://{}/admin/products'.format(shop))
        else:
            return 'Error getting access token: {}'.format(response.text), 500 
    def store_access_token_in_db(self, shop, data):
        return self.Coordinator.add_token_db(shop, data)