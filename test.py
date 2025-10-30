import json

from nhlpy import NHLClient

client = NHLClient()

"""
teams = client.teams.teams()
kraken = [x for x in teams if x["abbr"] == "SEA"][0]
standings = client.standings.league_standings()
games = client.schedule.daily_schedule()
players = client.players.players_by_team("SEA", 20252026)
"""

class PlayerStats:
    def __init__(self, value):
        self.__dict__.update(value)

stats = client.stats.skater_stats_summary(20252026, 20252026, franchise_id=39)
filtered_stats = [ PlayerStats(item) for item in stats]

#print(json.dumps(stats, indent=4))
print(filtered_stats)