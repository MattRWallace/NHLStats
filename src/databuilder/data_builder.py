import json
import logging

import pandas as pd
from nhlpy import NHLClient

from model.game_entry import GameEntry
from model.game_type import GameType
from model.seasons import PastSeasons
from model.team_map import TeamMap

logger = logging.getLogger("BuildData")
logging.basicConfig(filename="buildData.log", level=logging.INFO)
logger.info("Starting data fetch")


class DataBuilder:

    def build_games():
        
        """
        Avoid multiple rows for a single game by recoding the IDs for games already processed.
        """
        games_processed = []


        client = NHLClient()

        for season in PastSeasons:
            data = []
            logger.info(f"Start of processing for season '{season}'.")
            
            for team in TeamMap:
                try:
                    logger.info(f"Start processing for team '{team}' in season '{season}'.")
                    
                    games = client.schedule.team_season_schedule(team, season)["games"]
                    logger.info(f"Found '{len(games)}' games for team '{team}' in season '{season}'.")
                    
                    for game in games:
                        try:
                            if game["id"] in games_processed:
                                logger.info(f"Skipping game '{game["id"]}' which was already processed.")
                                continue
                            games_processed.append(game["id"])
                            box_score = client.game_center.boxscore(game["id"])
                            if box_score["gameType"] != GameType.RegularSeason.value:
                                logger.info(f"Skipping game '{game["id"]}' which is not a regular season game.")
                                continue
                            entry = repr(GameEntry.from_json(box_score))
                            logger.info(f"Adding game entry to data set: '{entry}'.")
                            data.append(entry)

                        except Exception as e:
                            print("\033[31mException occured. Check logs.\033[0m")
                            logger.exception(f"Exception processing box_score query. Exception: '{str(e)}', box_score: '{json.dumps(box_score, indent=4)}'.", stack_info=True)

                except Exception as e:
                    print("\033[31mException occured. Check logs.\033[0m")
                    logger.exception(f"Exception processing team_season_schedule query. Exception: '{str(e)}', games: '{json.dumps(games, indent=4)}', box_score: '{json.dumps(box_score, indent=4)}'.", stack_info=True)


            df = pd.DataFrame(data)
            df.to_csv(f"{season}.csv", index=False, header=False)
                                
                
        #print(data) # TODO: remove debugging statement
        print(f"Total games added to database: '{len(games_processed)}'.") # TODO: Remove debugging statement

        logger.info("Completed data fetch")

    def build_players():
        print("build_players not implemented.")