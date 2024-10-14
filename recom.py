import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = '159ebc178c6c47edacedca15239cfd9b'
client_secret = 'aa615c28f70b4c488f5b3365f70a2c32'

def recom_song(emotion_inp):
    auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(auth_manager=auth_manager)

    results = sp.search(q=emotion_inp, type='track')
    tracks = []
    for item in results['tracks']['items']:
        track = item['external_urls']['spotify']
        tracks.append(track)
    return tracks

