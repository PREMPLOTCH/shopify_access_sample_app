from flask import Blueprint
from app.v1.users import views as sample_subapp_views


v1 = Blueprint('v1', __name__)


# subapp1 urls
sample_subapp_prefix = '/users'

v1.add_url_rule(sample_subapp_prefix + '/getUserName', view_func=sample_subapp_views.GetUserName.as_view('endpoint_1'))

token_prefix = '/token'
v1.add_url_rule(sample_subapp_prefix + '/', view_func=sample_subapp_views.Index.as_view('index'))
v1.add_url_rule(sample_subapp_prefix + '/install', view_func=sample_subapp_views.Install.as_view('install'))
v1.add_url_rule(sample_subapp_prefix + '/api/callback', view_func=sample_subapp_views.OauthCallback.as_view('api_callback'))

