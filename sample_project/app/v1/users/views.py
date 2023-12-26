from flask.views import MethodView
from app.decorators import validate_request
from app.common_utils import render_success_response
from app.v1.users.service import SubApp1Service


class GetUserName(MethodView):

    @validate_request
    def get(self, params, headers, *args, **kwargs):
        response, message = SubApp1Service(params, headers).get_static_api_response()
        return render_success_response(response, message)

class Index(MethodView):

    @validate_request
    def get(self, params, headers, *args, **kwargs):
        response, message = SubApp1Service(params, headers).index()
        return render_success_response({}, 'Home view')

class Install(MethodView):

    @validate_request
    def get(self, params, headers, *args, **kwargs):
        response, message = SubApp1Service(params, headers).install()
        return render_success_response({}, 'Login view')

class OauthCallback(MethodView):

    @validate_request
    def get(self, params, headers, *args, **kwargs):
        response, message = SubApp1Service(params, headers).oauth_callback()
        return render_success_response({}, 'Logout view')