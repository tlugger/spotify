from nio.block.base import Block
from nio.properties import VersionProperty, StringProperty
from nio.block.mixins import EnrichSignals
import spotipy
import spotipy.util as util


class Spotify(Block, EnrichSignals):

    version = VersionProperty('0.1.0')
    client_id = StringProperty(title='Client ID', default='[[CLIENT_ID]]')
    client_secret = StringProperty(title='Client Secret', default='[[CLIENT_SECRET]]')
    scope = StringProperty(title='Scope', default=None)
    redirect_uri = StringProperty(title='Redirect URI', default='http://localhost:8888/callback')
    username = StringProperty(title='Username', default='')

    def process_signals(self, signals):
        out_sigs = []
        for signal in signals:
            token = {"token": util.prompt_for_user_token(self.username(), self.scope(), self.client_id(), self.client_secret(), self.redirect_uri()) }
            out_sigs.append(self.get_output_signal(token, signal))
        self.notify_signals(out_sigs)
