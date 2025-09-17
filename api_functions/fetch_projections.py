import requests
import json
from datetime import datetime
import os
import sys

def fetch_and_structure_projections(output_folder="json_results"):
    """
    Fetches NFL projection data and stores it in a nested JSON object
    structured by date, then by team ID. Allows specifying a custom output folder.
    """
    output_json = os.path.join(output_folder, "win_projections.json")

    # Ensure the folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    today_str = datetime.now().strftime("%Y-%m-%d")
    current_year = datetime.now().year

    # --- Step 1: Load the entire data object from the JSON file ---
    if os.path.exists(output_json):
        print(f"Loading existing data from {output_json}...")
        with open(output_json, 'r') as f:
            # Use a try-except block to handle empty files
            try:
                all_data = json.load(f)
            except json.JSONDecodeError:
                all_data = {} # File is empty, start with a new dictionary
    else:
        print("No existing JSON file found. Starting a new one.")
        all_data = {}

    # --- Step 2: Fetch new data for all teams ---
    todays_projections = {}
    print(f"Fetching data for {today_str}...")

    for team_id in range(1, 35): # Loop through potential team IDs
        url = f"http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/{current_year}/teams/{team_id}/projection"
        
        try:
            response = requests.get(url)
            response.raise_for_status() # Check for HTTP errors (like 404)
            data = response.json()

            # Create a dictionary with the specific keys from the API response
            metrics = {
                "chanceToWinThisWeek": data.get("chanceToWinThisWeek"),
                "chanceToWinDivision": data.get("chanceToWinDivision"),
                "projectedWins": data.get("projectedWins"),
                "projectedLosses": data.get("projectedLosses")
            }

            # Ensure all expected data points were found before adding
            if all(value is not None for value in metrics.values()):
                # Use the string version of team_id as the JSON key
                todays_projections[str(team_id)] = metrics
                print(f"  Successfully processed data for Team ID: {team_id}")
            else:
                print(f"  Incomplete data found for Team ID: {team_id}")

        except requests.exceptions.HTTPError:
            # This is expected for IDs that don't exist, so we can ignore it
            pass
        except Exception as e:
            print(f"  An error occurred for Team ID {team_id}: {e}")

    # --- Step 3: Add today's collected data to the main object and save ---
    if todays_projections:
        # Add the new dictionary of all teams under today's date key
        all_data[today_str] = todays_projections
        
        print(f"\nSaving updated data to {output_json}...")
        with open(output_json, 'w') as f:
            # The indent=2 parameter makes the JSON file human-readable
            json.dump(all_data, f, indent=2)
        print("Script finished successfully.")
    else:
        print("\nNo new projection data was fetched. File not updated.")

if __name__ == "__main__":
    # Allow specifying a custom output folder via command-line arguments
    custom_output_folder = sys.argv[1] if len(sys.argv) > 1 else "json_results"
    fetch_and_structure_projections(custom_output_folder)