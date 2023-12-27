from app.v1.users.coordinator import ShopifyCoordinator
from flask import request, redirect
import requests
from config import Config
class ShopifyAccessTokenService:

    def __init__(self,params,headers):
        self.params= params
        self.headers = headers
        self.Coordinator = ShopifyCoordinator()

    def app_index(self):
        return 'Hello, welcome to your app!'

    def install_app(self):
        shop = request.args.get('shop')
        auth_url = "{}?client_id={}&redirect_uri={}&grant_options[]=per-user".format(Config.APP_AUTH_BASE_URL, Config.APP_API_PUBLIC_KEY, Config.APP_REDIRECT_URL)
        return redirect(auth_url)

    def authorize_app_after_install(self):
        code = request.args.get('code')
        shop = request.args.get('shop')
        token_url = Config.APP_ACCESS_TOKEN_URL.format(shop=shop)
        data = {
            'client_id': Config.APP_API_PUBLIC_KEY,
            'client_secret': Config.APP_API_SECRET_KEY,
            'code': code
        }
        response = requests.post(token_url, data=data)
        if response.ok:
            access_token = response.json().get('access_token')
            self.Coordinator.add_access_token_to_db(shop, access_token)
            return redirect('https://{}/admin/products'.format(shop))
        else:
            return 'Error getting access token: {}'.format(response.text), 500
