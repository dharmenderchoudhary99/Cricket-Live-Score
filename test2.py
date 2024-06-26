import requests
from tabulate import tabulate

def fetch_cricket_scores():
    url = 'https://cricbuzz-cricket.p.rapidapi.com/mcenter/v1/41881/comm'
    headers = {
        'x-rapidapi-key': '2a746d5cc9mshc20b335fc9618bap125d5djsn3fffca65970f',
        'x-rapidapi-host': 'cricbuzz-cricket.p.rapidapi.com'
    }
    response = requests.get(url, headers=headers)
    
    # Print the response content for debugging
    print(response.text)
    
    data = response.json()

    # Check if 'typeMatches' is in the response
    if 'typeMatches' not in data:
        print("Error: 'typeMatches' key not found in the response")
        return

    matches = data['typeMatches'][0]['seriesMatches'][0]['seriesAdWrapper']['matches']

    for match in matches:
        table = []
        table.append(["Match Description", f"{match['matchInfo']['matchDesc']} , {match['matchInfo']['team1']['teamName']} vs {match['matchInfo']['team2']['teamName']}"])
        table.append(["Match Details", ""])
        table.append(["Series Name", match['matchInfo']['seriesName']])
        table.append(["Match Format", match['matchInfo']['matchFormat']])
        table.append(["Result", match['matchInfo']['status']])
        table.append([f"{match['matchInfo']['team1']['teamName']}", f"{match['matchScore']['team1Score']['inngs1']['runs']}/{match['matchScore']['team1Score']['inngs1']['wickets']} in {match['matchScore']['team1Score']['inngs1']['overs']} overs"])
        table.append([f"{match['matchInfo']['team2']['teamName']}", f"{match['matchScore']['team2Score']['inngs1']['runs']}/{match['matchScore']['team2Score']['inngs1']['wickets']} in {match['matchScore']['team2Score']['inngs1']['overs']} overs"])

        headers = ["Key", "Value"]
        print(tabulate(table, headers=headers, tablefmt="grid"))
        print("\n")

fetch_cricket_scores()