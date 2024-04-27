# # Fortnite Stats Tracker
# - **Objective**: Create a Python program that fetches and displays the player's Fortnite statistics.
# - **Features**:
#   - Interface to show stats such as win rate, average kills, and highest elimination count.
#   - Progress tracking over time with visual graphs and charts.
#   - Automated data retrieval using the Epic Games API.


import requests
import matplotlib.pyplot as plt

class FortniteStatsTracker:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.fortnitetracker.com/v1/profile/"
        self.headers = {'TRN-Api-Key': self.api_key}

    def get_player_stats(self, platform, epic_nickname):
        url = f"{self.base_url}{platform}/{epic_nickname}"
        response = requests.get(url, headers=self.headers)
        return response.json()

    def display_stats(self, stats):
        print("Player Stats:")
        print(f"Win Rate: {stats['lifeTimeStats'][8]['value']}")
        print(f"Average Kills: {stats['lifeTimeStats'][10]['value']}")
        print(f"Highest Elimination Count: {stats['lifeTimeStats'][9]['value']}")

    def plot_progress(self, stats_history):
        dates = [stat['dateCollected'] for stat in stats_history]
        win_rates = [float(stat['stats']['winRate']['value']) for stat in stats_history]
        plt.plot(dates, win_rates)
        plt.xlabel('Date')
        plt.ylabel('Win Rate')
        plt.title('Win Rate Over Time')
        plt.show()

# Example usage:
api_key = 'YOUR_API_KEY_HERE'
tracker = FortniteStatsTracker(api_key)
player_stats = tracker.get_player_stats('pc', 'player_nickname')
tracker.display_stats(player_stats)
stats_history = [
    {'dateCollected': '2021-09-01', 'stats': {'winRate': {'value': '5'}}},
    {'dateCollected': '2021-10-01', 'stats': {'winRate': {'value': '10'}}}
]
tracker.plot_progress(stats_history)
