import sqlite3
import requests
from functions import *
from vars import *

current_token = getAccessToken()

dbConnection = sqlite3.connect("test.db", check_same_thread=False)
cursor = dbConnection.cursor()

def updateColumnByTrack(columnName, value, trackID):
	cursor.execute(f'UPDATE Instances SET {columnName} = ? WHERE Song = ?', (value, trackID))

def updateColumnByIP(columnName, value, IPAddress):
	cursor.execute(f'UPDATE Instances SET {columnName} = ? WHERE IP = ?', (value, IPAddress))

newColumnsText = ["country", "country_code", "region", "region_code", "city", "album_name", "artist_name", "song_name", "release_date"]
newColumnsFloats = ["acousticness", "danceability", "energy", "instrumentalness", "liveness", "loudness", "speechiness", "tempo", "valence"]
newColumnsIntegers = ["duration_ms", "key", "mode", "time_signature"]

for i in newColumnsText:
	cursor.execute(f'ALTER TABLE Instances ADD {i} TEXT')
for i in newColumnsFloats:
	cursor.execute(f'ALTER TABLE Instances ADD {i} REAL')
for i in newColumnsIntegers:
	cursor.execute(f'ALTER TABLE Instances ADD {i} INTEGER')
dbConnection.commit()

ipList = set([ip[0] for ip in cursor.execute("SELECT IP from Instances")])

for ip in ipList:
	location = getLocation(ip)
	if location == "failure":
		print(f"failure for {ip}")	
	for column in location.keys():
		updateColumnByIP(column, location[column], ip)
dbConnection.commit()

trackList = set([song[0] for song in cursor.execute("SELECT Song from Instances")])

for track in trackList:
	response = requests.get(url=f"{api_baseurl}/tracks/{track}", headers={"Authorization": f"Bearer {current_token}"})
	responseJSON = response.json()

	responseFeatures = requests.get(url=f"{api_baseurl}/audio-features/{track}", headers={"Authorization": f"Bearer {current_token}"})
	responseFeaturesJSON = responseFeatures.json()

	album_name = responseJSON['album']['name']
	artist_name = str(getArtistName(responseJSON))
	song_name = responseJSON['name']
	release_date = responseJSON['album']['release_date']
	duration_ms = responseFeaturesJSON['duration_ms']

	featureList = ["acousticness", "danceability", "energy", "instrumentalness", "key", "liveness", "loudness", "mode", "speechiness", "tempo", "time_signature", "valence"]
	otherColumns = {"album_name": album_name, "artist_name": artist_name, "song_name": song_name, "release_date": release_date, "duration_ms": duration_ms}
	for feature in featureList:
		updateColumnByTrack(feature, responseFeaturesJSON[feature], track)
	for column in otherColumns.keys():
		updateColumnByTrack(column, otherColumns[column], track)
dbConnection.commit()