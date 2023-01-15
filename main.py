import json
import requests
from secrets1 import spotify_user_id, my_playlist_id
from pprint import pp
from datetime import date
from refresh import Refresh

class SaveSongs:
    def __init__(self):
        self.user_id = spotify_user_id
        self.spotify_token = ""
        self.discover_weekly_id = my_playlist_id
        self.tracks = ""
        self.new_playlist_id = ""

    
    def find_songs(self):

        # Loop through playlist tracks, add them to list
        print("Finding songs.....")

        url = f"https://api.spotify.com/v1/playlists/{my_playlist_id}/tracks"
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {self.spotify_token}"}
        response = requests.get(url, headers=headers)
        response_json = response.json()
        # pp(response)

        for i in response_json["items"]:
            self.tracks += (i["track"]["uri"] + ",")
        self.tracks = self.tracks[:-1]

        self.add_to_playlist()


    def create_new_playlist(self):
        print("Creating new play list.....")
        today=date.today()
        formateddate= today.strftime("%d/%m/%Y")
        url=f"https://api.spotify.com/v1/users/{spotify_user_id}/playlists"
        data=json.dumps({"name": formateddate + " Bollywood weekly ","description":"my weekly playlist rescued from the desruction using python script","public":True})
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {self.spotify_token}"}
        response=requests.post(url,data=data,headers=headers)

        response_json=response.json()
        # pp(response_json)
        return response_json[ 'id']

    
    def add_to_playlist(self):
        # add all songs to new playlist
        self.new_playlist_id = self.create_new_playlist()
        print("Adding songs...")

        url = f"https://api.spotify.com/v1/playlists/{self.new_playlist_id}/tracks?uris={self.tracks}" 
        headers={"Content-Type": "application/json",
                 "Authorization": "Bearer {}".format(self.spotify_token)}

        response = requests.post(url, headers=headers)

        pp(response.json)

    
    
    def call_refresh(self):

        print("Refreshing token")
        rc = Refresh()
        self.spotify_token = rc.refresh()
        self.find_songs()


playlist = SaveSongs()
playlist.call_refresh()







