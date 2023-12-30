import requests
import json
import math

API_TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjRhZjIxOTNiLTNjNDQtNDEyZi1iZjI5LTVlZDk4M2QyNDY5MSIsImlhdCI6MTcwMjU3ODExOCwic3ViIjoiZGV2ZWxvcGVyLzhlMmY2NzNkLTExNTEtNGVlZi0wM2Q0LWJhMzhkNDZlYzIxMCIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiMTI4LjE5NS45Ny4xMjUiLCIxNjkuMjM0LjM4LjQzIl0sInR5cGUiOiJjbGllbnQifV19.Zj8SWo7M3DbfD9EbUPj-NVHPCHJ66O8SthOFMMYSSrFuaGEpFfQsZRyGY-qGMObpFtXN-WTcwTjV-Rbklm-BXQ'

class PlayerInfo:
    def __init__(self, player_id) -> None:
        self.url = f'https://api.brawlstars.com/v1/players/%23{player_id}'
        self.player_info = None

    def run_query(self):
        headers = {
            'Authorization': f'Bearer {API_TOKEN}'
        }
        response = requests.get(self.url, headers=headers)
        if response.status_code == 200:
            self.player_info = json.loads(response.text)
        elif response.status_code == 403:
            self.player_info = None
    
    def username(self):
        if not self.player_info:
            self.run_query()
        try:
            return self.player_info['name']
        except:
            return 'An error occured. Please contact 7eevvan'

    def trophy_count(self):
        if not self.player_info:
            self.run_query()
        try:
            return self.player_info['trophies']
        except:
            return 'An error occured. Please contact 7eevvan'

    def average_trophy_count(self):
        if not self.player_info:
            self.run_query()
        return math.ceil(self.player_info['trophies'] / len(self.player_info['brawlers']))

class ClubMembers:
    def __init__(self) -> None:
        self.base_url = 'https://api.brawlstars.com/v1/clubs/%23'
        self.url = ''
        self.club_members = None

    def run_query(self):
        club_tag = input("What is your club ID? ").lower()
        self.url = f'{self.base_url}{club_tag}/members'
        headers = {
            'Authorization': f'Bearer {API_TOKEN}'
        }
        response = requests.get(self.url, headers=headers)
        self.player_info = json.loads(response.text)

    def top_player(self):
        if not self.club_members:
            self.run_query()
        return self.player_info["items"][0]["name"]



    

# PlayerInfo test
# temp = PlayerInfo('yqlj99qu')
# print(temp.trophy_count())


# temp = ClubMembers()
# print(temp.top_player())
