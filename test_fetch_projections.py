import os
import subprocess
import sys
import unittest
from api_functions.fetch_teams import fetch_team_data

def run_tests():
    """
    Runs tests for the fetch_projections script and saves results in a test folder.
    """
    test_output_folder = "test_json_results"

    # Ensure the test folder exists
    if not os.path.exists(test_output_folder):
        os.makedirs(test_output_folder)

    # Use the correct Python executable from the virtual environment
    python_executable = sys.executable

    # Run the fetch_projections script with the test folder as the output
    try:
        subprocess.run([python_executable, "api_functions/fetch_projections.py", test_output_folder], check=True)
        print(f"Test run completed. Results saved in {test_output_folder}.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running the test: {e}")

class TestFetchTeams(unittest.TestCase):
    def test_fetch_team_data(self):
        """Test the fetch_team_data function for a valid year."""
        year = 2025
        teams = fetch_team_data(year)
        self.assertIsInstance(teams, dict)
        self.assertGreater(len(teams), 0)
        for team_name, team_id in teams.items():
            self.assertIsInstance(team_name, str)
            self.assertIsInstance(team_id, int)

if __name__ == "__main__":
    run_tests()
    unittest.main()