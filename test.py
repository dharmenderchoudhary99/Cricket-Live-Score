import requests 


url = 'https://cricbuzz-cricket.p.rapidapi.com/mcenter/v1/41881/comm'
headers = {
    'x-rapidapi-key': '2a746d5cc9mshc20b335fc9618bap125d5djsn3fffca65970f',
    'x-rapidapi-host': 'cricbuzz-cricket.p.rapidapi.com'
  }

response = requests.get(url, headers=headers)
print(response.json())