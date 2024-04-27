# ### Fortnite Stats Tracker
# - **Objective**: Create a Python program that fetches and displays the player's Fortnite statistics.
# - **Features**:
#   - Interface to show stats such as win rate, average kills, and highest elimination count.
#   - Progress tracking over time with visual graphs and charts.
#   - Automated data retrieval using the Epic Games API.

# ### Step 1: Install Required Libraries
# - `requests`: to send HTTP requests to the Fortnite API.
# - `matplotlib`: to plot graphs and charts.
# - `numpy`: to perform numerical operations on the data.
# - `pandas`: to store and manipulate the data in a tabular format.
# - `tabulate`: to display the data in a formatted table.

# !pip install requests matplotlib numpy pandas tabulate

# ### Step 2: Import Required Libraries

import requests
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from tabulate import tabulate

# ### Step 3: Set Up the API Key
# - You need to obtain an API key from the Epic Games Developer Portal to access the Fortnite API.
# - Replace `'YOUR_API_KEY_HERE'` with your actual API key.

API_KEY = 'YOUR_API_KEY_HERE'

# ### Step 4: Define the `FortniteStats` Class


class FortniteStats:
    def __init__(self, username):
        self.username = username
        self.platform = 'pc'
        self.base_url = 'https://api.fortnitetracker.com/v1/profile/'
        self.headers = {'TRN-Api-Key': API_KEY}
        self.stats = self.get_stats()

    def get_stats(self):
        url = f'{self.base_url}{self.platform}/{self.username}'
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def get_lifetime_stats(self):
        if self.stats:
            return self.stats['lifeTimeStats']
        else:
            return None

    def get_lifetime_stats_dict(self):
        lifetime_stats = self.get_lifetime_stats()
        if lifetime_stats:
            stats_dict = {stat['key']: stat['value']
                          for stat in lifetime_stats}
            return stats_dict
        else:
            return None

    def get_lifetime_stats_table(self):
        lifetime_stats = self.get_lifetime_stats()
        if lifetime_stats:
            stats_table = [[stat['key'], stat['value']]
                           for stat in lifetime_stats]
            return stats_table
        else:
            return None

    def get_lifetime_stats_df(self):
        lifetime_stats = self.get_lifetime_stats()
        if lifetime_stats:
            stats_df = pd.DataFrame(lifetime_stats, columns=['key', 'value'])
            return stats_df
        else:
            return None

    def get_stat(self, stat_name):
        stats_dict = self.get_lifetime_stats_dict()
        if stats_dict:
            return stats_dict.get(stat_name, None)
        else:
            return None

    def get_stat_table(self, stat_names):
        stats_dict = self.get_lifetime_stats_dict()
        if stats_dict:
            stats_table = [[stat_name, stats_dict.get(
                stat_name, None)] for stat_name in stat_names]
            return stats_table
        else:
            return None

    def get_stat_df(self, stat_names):
        stats_dict = self.get_lifetime_stats_dict()
        if stats_dict:
            stats_df = pd.DataFrame([[stat_name, stats_dict.get(
                stat_name, None)] for stat_name in stat_names], columns=['key', 'value'])
            return stats_df
        else:
            return None

    def plot_stat(self, stat_name):
        stats_dict = self.get_lifetime_stats_dict()
        if stats_dict:
            stat_value = stats_dict.get(stat_name, None)
            if stat_value:
                plt.figure(figsize=(8, 6))
                plt.bar(stat_name, int(stat_value))
                plt.xlabel(stat_name)
                plt.ylabel('Value')
                plt.title(f'{stat_name} for {self.username}')
                plt.show()
            else:
                print(f'Statistic "{stat_name}" not found.')
        else:
            print('No stats found for the user.')

    def plot_stats(self, stat_names):
        stats_dict = self.get_lifetime_stats_dict()
        if stats_dict:
            stat_values = [stats_dict.get(stat_name, None)
                           for stat_name in stat_names]
            if all(stat_values):
                plt.figure(figsize=(12, 6))
                plt.bar(stat_names, [int(value) for value in stat_values])
                plt.xlabel('Statistic')
                plt.ylabel('Value')
                plt.title(f'Statistics for {self.username}')
                plt.show()
            else:
                print('One or more statistics not found.')
        else:
            print('No stats found for the user.')

    def display_stats_table(self, stat_names):
        stats_table = self.get_stat_table(stat_names)
        if stats_table:
            print(tabulate(stats_table, headers=[
                  'Statistic', 'Value'], tablefmt='grid'))
        else:
            print('No stats found for the user.')

    def display_stats_df(self, stat_names):
        stats_df = self.get_stat_df(stat_names)
        if stats_df is not None:
            print(stats_df)
        else:
            print('No stats found for the user.')

# ### Step 5: Create an Instance of the `FortniteStats` Class
# - Replace `'YOUR_USERNAME_HERE'` with the Fortnite username you want to track.


username = 'YOUR_USERNAME_HERE'
stats = FortniteStats(username)

# ### Step 6: Display Lifetime Stats
# - Display all the lifetime stats available for the user.

lifetime_stats_table = stats.get_lifetime_stats_table()
if lifetime_stats_table:
    print(tabulate(lifetime_stats_table, headers=[
          'Statistic', 'Value'], tablefmt='grid'))
else:
    print('No stats found for the user.')

# ### Step 7: Display Specific Stats
# - Display specific lifetime stats for the user.
# - Replace `['Wins', 'K/d', 'Kills']` with the stats you want to display.

specific_stats = ['Wins', 'K/d', 'Kills', 'Matches Played', 'Top 10', 'Win %', 'Kills Per Min', 'Kills Per Match', 'Score', 'Score Per Match', 'Score Per Min', 'Time Played', 'Avg Survival Time', 'Avg Match Time', 'Avg Score Per Match', 'Avg Score Per Min', 'Avg Time Played', 'Avg Top 10',
                  'Avg Top 25', 'Avg Kills', 'Avg Deaths', 'Avg KD', 'Avg Kills Per Min', 'Avg Kills Per Match', 'Avg Score', 'Avg Score Per Match', 'Avg Score Per Min', 'Avg Time Played', 'Avg Win %', 'Avg Top 10 %', 'Avg Top 25 %', 'Avg Top 5 %', 'Avg Top 12 %', 'Avg Top 3 %', 'Avg Top 6 %', 'Avg Top 1 %']
stats.display_stats_table(specific_stats)

# ### Step 8: Plot Specific Stats
# - Plot specific lifetime stats for the user.
# - Replace `'Wins'` with the stat you want to plot.

stats.plot_stat('Wins')

# ### Step 9: Plot Multiple Stats

stats.plot_stats(['Wins', 'Kills', 'K/d'])

# ### Conclusion
# - You have successfully created a Fortnite Stats Tracker in Python.
# - You can now track and display various statistics for a Fortnite user.
# - You can further enhance this program by adding more features and visualizations.
# - You can also explore other APIs to fetch additional data and insights.

# ### References
# - [Fortnite API Documentation](https://fortnitetracker.com/site-api)
# - [Requests Library Documentation](https://docs.python-requests.org/en/master/)
# - [Matplotlib Library Documentation](https://matplotlib.org/stable/contents.html)
# - [Numpy Library Documentation](https://numpy.org/doc/stable/user/index.html)
# - [Pandas Library Documentation](https://pandas.pydata.org/docs/user_guide/index.html)
# - [Tabulate Library Documentation](https://pypi.org/project/tabulate/)

# ### Thank You!
