import json
from enum import Enum

from nhlpy import NHLClient

#########################################
# Supporting classes. These should become interfaces eventually
#########################################

"""
Class to hold all the info for a single game row
"""
class GameEntry:
    def __init__(
            self, 
            num_periods, 
            home_score, 
            home_sog,
            away_score,
            away_sog,
            game_type):
        self._num_periods = num_periods
        self._home_score = home_score
        self._home_sog = home_sog
        self._away_score = away_score
        self._away_sog = away_sog
        self._game_type = game_type

    @classmethod
    def from_json(cls, json_data):
        return cls(
            json_data["periodDescriptor"]["number"], 
            json_data["homeTeam"]["score"],
            json_data["homeTeam"]["sog"],
            json_data["awayTeam"]["score"],
            json_data["awayTeam"]["sog"],
            json_data["gameType"]
            )


    """
    serialize the game data to a single row
    """
    def __repr__(self):
        return f"{self._num_periods},{self._home_score},{self._home_sog},{self._away_score},{self._away_sog},{self._game_type}"


"""
Enumeration to map positions to numerical values
"""
class Position(Enum):
    C = 1       # Center
    L = 2       # Left wing
    R = 3       # Right wing
    D = 4       # Defenseman
    G = 5       # Goalie

class GameType(Enum):
    Preseason = 1
    RegularSeason = 2
    Playoff = 3
    AllStar = 4


#########################################
# Start of experimentation code
#########################################

supported_seasons = [
    "20222023",
    "20232024",
    "20242025",
    "20252026"
]

months_of_play = [
    "October"
]

"""
This is the set of team IDs for the current teams in the leage.
Note: Team id is a different identifier than franchise ID

TODO: This is a working list.  Depending on implementation, a map
of some sort might be better.  E.g. FranchiseId => TeamId
"""
current_teams = {
    "SEA": 55,             # Kraken
    "Canadiens": 0,
    "Red Wings": 0,
    "Maple Leafs": 0,
    "Bruins": 0,
    "Lightning": 0,
    "Senators": 0,
    "Sabres": 0,
    "Panthers": 0,
    "devils": 0,
    "Pneguins": 0,
    "Hurricaines": 0,
    "captials": 0,
    "Flyers": 0,
    "Islanders": 0,
    "Blue Javkets": 0,
    "Rangers": 0,
    "Avalanche": 0,
    "Jets": 0,
    "Mammoth": 0,
    "Stars": 0,
    "Blackhawks": 0,
    "Predators": 0,
    "wild": 0,
    "Blues": 0,
    "Ducks": 0,
    "Knights": 0,
    "kings": 0,
    "EDM": 0,               #Oilers
    "Canucks": 0,
    "sharks": 0,
    "flames": 0
}

"""
Avoid multiple rows for a single game by recoding the IDs for games already processed.
"""
games_processed = []

"""
Cache the generated rows to write out to csv
"""
data = []

client = NHLClient()

# TODO: Still hard coded to only Kraken games
games = client.schedule.team_season_schedule("SEA", 20222023)["games"]

print(f"Found games: {len(games)}") # TODO: remove debugging statement

for game in games:
    if game["id"] in games_processed:
        print(f"Duplicate game data. GameId: '{game["id"]}'")  # TODO: remove debugging statment
        continue
    print(f"Processing game: {game["id"]}")
    games_processed.append(game["id"])
    box_score = client.game_center.boxscore(game["id"])
    if box_score["gameType"] != GameType.RegularSeason.value:
        print(f"Not a regular season game. GameId:{game["id"]}', GameType: '{box_score["gameType"]}'") # TODO: remove debugging statement
        continue
    data.append(repr(GameEntry.from_json(box_score)))

print(data)
