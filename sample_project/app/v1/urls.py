from flask import Blueprint
from app.v1.users import views as shpoify_access_token_views

v1 = Blueprint('v1', __name__)
shpoify_access_token_prefix = '/token'
v1.add_url_rule(shpoify_access_token_prefix + '/', view_func=shpoify_access_token_views.AppIndex.as_view('index'))
v1.add_url_rule(shpoify_access_token_prefix + '/install', view_func=shpoify_access_token_views.InstallApp.as_view('install'))
v1.add_url_rule(shpoify_access_token_prefix + '/api/callback', view_func=shpoify_access_token_views.AuthorizeApp.as_view('api_callback'))