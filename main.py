from api_functions.fetch_teams import fetch_team_data

def main():
    """
    Main function to fetch and print the dictionary of team mappings.
    """
    year = 2025
    teams = fetch_team_data(year)
    print("Team Mappings:")
    for team_name, team_id in teams.items():
        print(f"{team_name}: {team_id}")

if __name__ == "__main__":
    main()