Spotify
=======
A nio block for creating an authorization token for the Spotify Web API

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

Commands
--------
None

