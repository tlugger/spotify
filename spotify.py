import spotipy.util as util

scope = '[[ YOUR_SCOPE]]'
username = '[[ YOUR_USERNAME ]]'
client_id = '[[ YOUR_CLIENT_ID ]]'
client_secret = '[[ YOUR_CLIENT_SECRET ]]'
redirect_uri = 'http://localhost:8888/callback'

token = util.prompt_for_user_token(username,
                                   scope,
                                   client_id,
                                   client_secret,
                                   redirect_uri)

if token:
    print("Success")
else:
    print("Failed")
