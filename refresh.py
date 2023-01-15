
import requests
from pprint import pp
from secrets import refresh_token, base_64


class Refresh:                                     # To generate refresh token 
    def __init__(self):
        self.refresh_token=refresh_token            #set the refresh token which we recived from authorization 
        self.base_64=base_64                        #base_64=(client_id:secret_id) converted to base_64 
        # self.base_64=""
        # self.client_id=client_id
        # self.client_secret=client_secret
        # self.headers={}
        # self.data={}

    def refresh(self):
        url="https://accounts.spotify.com/api/token"                 #Spotify API endpont to get token
        # auth_string=client_id+":"+client_secret
        # auth_bytes=auth_string.encode("utf-8")                     #convert str to byte code
        # base_64=str(base64.b64encode(auth_bytes),"utf-8")      #convert to base64
        headers={ "Authorization": "Basic " + base_64} 
        data= {"grant_type": "refresh_token","refresh_token":refresh_token}
        response=requests.post(url,headers=headers,data=data)
        response_json=response.json()
        return response_json['access_token']



# b=Refresh()
# b.refresh()
