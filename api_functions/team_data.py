# This file serves as the central point for interacting with team-related data.

from .fetch_teams import fetch_team_data

# Dictionary mapping team IDs to team names
TEAM_ID_TO_NAME = {}

def initialize_team_data(year):
    """Fetch team data for the given year and initialize the TEAM_ID_TO_NAME dictionary."""
    global TEAM_ID_TO_NAME
    TEAM_ID_TO_NAME = {v: k for k, v in fetch_team_data(year).items()}

# Initialize the dictionary for the current year
initialize_team_data(2025)

# Function to get team name by ID
def get_team_name_by_id(team_id):
    """Retrieve the team name for a given team ID."""
    return TEAM_ID_TO_NAME.get(team_id, "Unknown Team")

# Function to get team ID by name
def get_team_id_by_name(team_name):
    """Retrieve the team ID for a given team name."""
    for id, name in TEAM_ID_TO_NAME.items():
        if name.lower() == team_name.lower():
            return id
    return None

class NFLTeamInfo:
    """
    A class to store and manage NFL team information, including conferences and divisions.
    """

    def __init__(self):
        self.conferences = {
            "AFC": {
                "East": ["Buffalo Bills", "Miami Dolphins", "New England Patriots", "New York Jets"],
                "North": ["Baltimore Ravens", "Cincinnati Bengals", "Cleveland Browns", "Pittsburgh Steelers"],
                "South": ["Houston Texans", "Indianapolis Colts", "Jacksonville Jaguars", "Tennessee Titans"],
                "West": ["Denver Broncos", "Kansas City Chiefs", "Las Vegas Raiders", "Los Angeles Chargers"]
            },
            "NFC": {
                "East": ["Dallas Cowboys", "New York Giants", "Philadelphia Eagles", "Washington Commanders"],
                "North": ["Chicago Bears", "Detroit Lions", "Green Bay Packers", "Minnesota Vikings"],
                "South": ["Atlanta Falcons", "Carolina Panthers", "New Orleans Saints", "Tampa Bay Buccaneers"],
                "West": ["Arizona Cardinals", "Los Angeles Rams", "San Francisco 49ers", "Seattle Seahawks"]
            }
        }

    def get_conference(self, team_name):
        """
        Get the conference and division of a given team.

        Args:
            team_name (str): The name of the team.

        Returns:
            tuple: A tuple containing the conference and division, or None if not found.
        """
        for conference, divisions in self.conferences.items():
            for division, teams in divisions.items():
                if team_name in teams:
                    return conference, division
        return None

    def get_teams_in_division(self, conference, division):
        """
        Get all teams in a specific conference and division.

        Args:
            conference (str): The conference name (e.g., "AFC").
            division (str): The division name (e.g., "East").

        Returns:
            list: A list of team names in the specified division, or an empty list if not found.
        """
        return self.conferences.get(conference, {}).get(division, [])

# Example usage
if __name__ == "__main__":
    print(get_team_name_by_id(1))  # Output: Arizona Cardinals
    print(get_team_id_by_name("Buffalo Bills"))  # Output: 4