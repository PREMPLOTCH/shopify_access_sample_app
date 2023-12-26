from app import app
from app.v1.users.views import Install,OauthCallback
app.add_url_rule('/install', view_func=Install.as_view('install'))
app.add_url_rule('/api/callback', view_func=OauthCallback.as_view('api_callback'))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
