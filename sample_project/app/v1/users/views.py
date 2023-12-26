from flask.views import MethodView
from app.decorators import validate_request
from app.common_utils import render_success_response
from app.v1.users.service import SubApp1Service
from flask import request


class GetUserName(MethodView):

    @validate_request
    def get(self, params, headers, *args, **kwargs):
        response, message = SubApp1Service(params, headers).get_static_api_response()
        return render_success_response(response, message)

class Index(MethodView):

    @validate_request
    def get(self, params, headers, *args, **kwargs):
        response = SubApp1Service(params, headers).index()
        return response

class Install(MethodView):
    
    @validate_request
    def get(self, params, headers, *args, **kwargs):
        response = SubApp1Service(params, headers).install()
        return response
    

class OauthCallback(MethodView):

    @validate_request
    def get(self, params, headers, *args, **kwargs):
        code = request.args.get('code')
        shop = request.args.get('shop')
        response = SubApp1Service(params, headers).oauth_callback()
        return response