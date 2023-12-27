from flask.views import MethodView
from app.decorators import validate_request
from app.v1.users.service import ShopifyAccessTokenService
from flask import request

class AppIndex(MethodView):
    @validate_request
    def get(self, params, headers, *args, **kwargs):
        response = ShopifyAccessTokenService(params, headers).app_index()
        return response

class InstallApp(MethodView):  
    @validate_request
    def get(self, params, headers, *args, **kwargs):
        response = ShopifyAccessTokenService(params, headers).install_app()
        return response    

class AuthorizeApp(MethodView):
    @validate_request
    def get(self, params, headers, *args, **kwargs):
        code = request.args.get('code')
        shop = request.args.get('shop')
        response = ShopifyAccessTokenService(params, headers).authorize_app_after_install()
        return response
