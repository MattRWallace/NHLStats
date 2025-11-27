from loggingconfig.logging_config import LoggingConfig
from model.player_info import GoalieInfo, SkaterInfo

logger = LoggingConfig.get_logger(__name__)

class AveragePlayerSummarizer:

    def summarize(self, homeRoster, awayRoster):
        logger.info("Summarizing home and away rosters.")
        homeSummary = self.summarize_roster(homeRoster)
        awaySummary = self.summarize_roster(awayRoster)

        return homeSummary, awaySummary

    def summarize_roster(self, roster):
        logger.info(f"Summarizing roster. Roster: '{roster}'.")
        forwards = self.summarize_skaters(roster["forwards"])
        defense = self.summarize_skaters(roster["defense"])
        goalies = self.summarize_goalies(roster["goalies"])
        return f"{forwards},{defense},{goalies}"

    def summarize_skaters(self, players):
        logger.info(f"Summarizing skaters. Skaters: '{players}'.")
        player_objects = []
        for player in players:
            player_objects.append(SkaterInfo.from_json(player))

        count = 0   
        goals = 0
        assists = 0
        points = 0
        plus_minus = 0
        pim = 0
        hits = 0
        pp_goals = 0
        sog = 0
        faceoff_win_pct = 0
        toi = 0
        blocked_shots = 0
        giveaways = 0
        takeaways = 0

        for player in player_objects:
            logger.info(f"Adding skater to summary. Goalie: '{player}'.")
            count += 1
            goals += player.goals
            assists += player.assists
            points += player.points
            plus_minus += player.plus_minus
            pim += player.pim
            hits += player.hits
            pp_goals += player.pp_goals
            sog += player.sog
            faceoff_win_pct += player.faceoff_win_pct
            toi += player.toi
            blocked_shots += player.blocked_shots
            giveaways += player.giveaways
            takeaways += player.takeaways

        # TODO: can't just average the FO %, it needs to be weighted    
        summary = SkaterInfo(
            goals,
            assists,
            points,
            plus_minus,
            pim,
            hits,
            pp_goals,
            sog,
            faceoff_win_pct,
            toi,
            blocked_shots,
            giveaways,
            takeaways
        )

        logger.info(f"Summarized goalies. Summary: '{summary}'.")
        return repr(summary)

    def summarize_goalies(self, players):
        logger.info(f"Summarizing goalies. Goalies: '{players}'.")
        player_objects = []
        for player in players:
            player_objects.append(GoalieInfo.from_json(player))

        count = 0
        es_shots_against = 0
        es_saves = 0
        pp_shots_against = 0
        pp_saves = 0
        sh_shots_against = 0
        sh_saves = 0
        save_shots_against = 0
        save_pct = 0
        es_goals_against = 0
        pp_goals_against = 0
        sh_goals_against = 0
        pim = 0
        goals_against = 0
        toi = 0
        # starter = 0
        # decision = 0
        shots_against = 0
        saves = 0

        for player in player_objects:
            logger.info(f"Adding goalie to summary. Goalie: '{player}'.")
            count += 1
            es_shots_against += player.es_shots_against
            es_saves += player.es_saves
            pp_shots_against += player.pp_shots_against
            pp_saves += player.pp_saves
            sh_shots_against += player.sh_shots_against
            sh_saves += player.sh_saves
            save_shots_against += player.save_shots_against
            save_pct += player.save_pct
            es_goals_against += player.es_goals_against
            pp_goals_against += player.pp_goals_against
            sh_goals_against += player.sh_goals_against
            pim += player.pim
            goals_against += player.goals_against
            toi += player.toi
            # starter += player.starter
            # decision += player.decision
            shots_against += player.shots_against
            saves += player.saves

        # TODO: can't just average the FO %, it needs to be weighted
        summary = GoalieInfo(
            es_shots_against,
            es_saves,
            pp_shots_against,
            pp_saves,
            sh_shots_against,
            sh_saves,
            save_shots_against,
            save_pct,
            es_goals_against,
            pp_goals_against,
            sh_goals_against,
            pim,
            goals_against,
            toi,
            # starter,
            # decision,
            shots_against,
            saves
        )

        logger.info(f"Summarized goalies. Summary: '{summary}'.")
        return repr(summary)