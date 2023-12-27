from config import Config
from app.app_config import register_versions, app
from app.v1.users.views import InstallApp,AuthorizeApp

app.add_url_rule('/install', view_func=InstallApp.as_view('install'))
app.add_url_rule('/api/callback', view_func=AuthorizeApp.as_view('api_callback'))

register_versions(Config.VERSIONS_ALLOWED)
