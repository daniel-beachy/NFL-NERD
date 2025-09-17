import requests

def fetch_team_data(year):
    """
    Fetches team data for the given NFL season year and returns a dictionary mapping team names to team IDs.
    
    Args:
        year (int): The NFL season year.

    Returns:
        dict: A dictionary where keys are team names and values are team IDs.
    """
    base_url = f"https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/{year}/teams/"
    team_data = {}

    for team_id in range(1, 35):
        response = requests.get(base_url + str(team_id))
        if response.status_code == 200:
            data = response.json()
            team_name = data.get("displayName")
            if team_name:
                team_data[team_name] = team_id

    return team_data

if __name__ == "__main__":
    year = 2025
    teams = fetch_team_data(year)
    print(teams)