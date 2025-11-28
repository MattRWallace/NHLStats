from __future__ import annotations

from enum import Enum

from model.average_player_summarizer import AveragePlayerSummarizer


class Summarizers(str, Enum):
    average_player_summarizer = "average"

    """
    Build a summarizer instance from the specified summarizer type.
    """
    @staticmethod
    def get_summarizer(summarizer: Summarizers):
        match summarizer:
            case Summarizers.average_player_summarizer:
                return AveragePlayerSummarizer()