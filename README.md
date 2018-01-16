Spotify
=======
A nio block for creating an authorization token for the Spotify Web API

Note: Configure the helper script `spotify.py` before using this block to create the initial token request. This script will have you visit the redirect uri once in a web browser and enter the url that you are redirected to in your terminal. 

Properties
----------
- **client_id**: API Client ID
- **client_secret**: API Client Secret
- **enrich**: If checked (true), the attributes of the incoming signal will be excluded from the outgoing signal. If unchecked (false), the attributes of the incoming signal will be included in the outgoing signal.
- **redirect_uri**: Oauth2 Redirect URI
- **scope**: Scopes that token will have access to
- **username**: Spotify Username

Inputs
------
- **default**: Any list of signals

Outputs
-------
- **default**: A signal appended to each incoming signal containing a `token` attribute

Dependencies
------------
spotipy

Commands
--------
None
