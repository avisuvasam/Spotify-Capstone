import requests
from vars import *

def getLocation(ip):
		response = requests.get(url=f"https://ipwho.is/{ip}", params={"fields":"success,country,country_code,region,region_code,city"})
		if response.status_code != 200:
			raise RuntimeError("website down, unable to get IP data.")
		result = response.json()
		if result["success"] == True:
			del result["success"]
			return result
		return "failure"

def getArtistName(jsonData):
		if len(jsonData['artists']) > 1:
			artistList = []
			for i in range(len(jsonData['artists'])):
				artistList.append(jsonData['artists'][i]['name'])
			return artistList
		return jsonData['artists'][0]['name']

def getAccessToken():
	response = requests.post(url = f"{account_baseurl}/api/token",
		headers = {
			"Content-Type":"application/x-www-form-urlencoded",
			"Authorization":f"Basic {combo_client}"
		},
		params = {
			"grant_type":"refresh_token",
			"refresh_token":refresh_token
		})
	
	currentToken = response.json()["access_token"]
	return currentToken