# import requests
# from pprint import pprint
# import json
# def top_kino():
# 	name=input("kino nomini kiriting EN:")
# 	info=requests.get(f"https://imdb-api.com/en/API/Search/k_wj2v3oer/{name}")
# 	data=info.json()
# 	for kino in data["results"]:
# 		print(f'kino nomi:{kino["title"]} VA '
# 			  f'kino yili:{kino["description"]}')
# top_kino()

import requests

url = "https://grammarbot.p.rapidapi.com/check"

payload = "text=Susan%20go%20to%20the%20store%20everyday&language=en-US"
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Host": "grammarbot.p.rapidapi.com",
	"X-RapidAPI-Key": "99f301d9bbmsh70c4a2d3c5529d8p11ba16jsn9a08b7c2eef0"
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
