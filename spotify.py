import os
import discord
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv()

SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

songList = []

# playlist adionada manulamente para testar o código
#pl_id = 'spotify:playlist:1Qhy7QA5Gfgc1Ugwpk5iXl'

def getSongs(id):
    playlist = sp.playlist(id)
    print(playlist['name'], 'made by:', playlist['owner']['display_name'])
    tracks = playlist['tracks']
    for i, item in enumerate(tracks['items']):
        track = item['track']
        #print(track['artists'][0]['name'], track['name'])
        song = track['artists'][0]['name'] + " " + track['name']
        songList.append(song)
    while tracks['next']:
        tracks = sp.next(tracks)
        for i, item in enumerate(tracks['items']):
            track = item['track']
            #print(track['artists'][0]['name'], track['name'])
            song = track['artists'][0]['name'] + " " + track['name']
            songList.append(song)
    return songList
                
"""    code from an example online

playlists = sp.user_playlists(username)
for playlist in playlists['items']:
    if playlist['owner']['id'] == username:
        print()
        print(playlist['name'])
        print('  total tracks', playlist['tracks']['total'])
        results = sp.user_playlist(username, playlist['id'], fields="tracks,next")
        tracks = results['tracks']
        show_tracks(tracks)
        while tracks['next']:
            tracks = sp.next(tracks)
            show_tracks(tracks)
            
"""