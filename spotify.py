import os
import discord
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pprint import pprint

load_dotenv()

SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

# playlist adionada manulamente para testar o código
#pl_id = 'spotify:playlist:1Qhy7QA5Gfgc1Ugwpk5iXl'

def getSongs(id):
    songList = []
    playlist = 0
    if (id.__contains__('album')):
        playlist = sp.album(id)
        print('album')
        pprint(playlist)
        tracks = playlist['tracks']
        #pprint(tracks['items'])
        for i, item in enumerate(tracks['items']):
            track = item['name']
            song = item['artists'][0]['name'] + " " + track + " audio lyrics"
            #print(song)
            songList.append(song)
        playlistName = playlist['name'] + " by " + playlist['artists'][0]['name']
        return songList, playlistName
    elif (id.__contains__('playlist')):
        playlist = sp.playlist(id)
        #print('playlist')
        print(playlist['name'], 'made by:', playlist['owner']['display_name'])
        playlistName = playlist['name'] + " made by " + playlist['owner']['display_name']
        tracks = playlist['tracks']
        #pprint(tracks)
        for i, item in enumerate(tracks['items']):
            track = item['track']
            #print(track['artists'][0]['name'], track['name'])
            song = track['artists'][0]['name'] + " " + track['name'] + " audio lyrics"
            songList.append(song)
        while tracks['next']:
            tracks = sp.next(tracks)
            for i, item in enumerate(tracks['items']):
                track = item['track']
                #print(track['artists'][0]['name'], track['name'])
                song = track['artists'][0]['name'] + " " + track['name'] + " audio lyrics"
                songList.append(song)
        return songList, playlistName
