from __future__ import annotations

from enum import Enum

import model.average_player_summarizer


class Summarizers(str, Enum):
    average_player_summarizer = "average"

    """
    Build a summarizer instance from the specified summarizer type.
    """
    @staticmethod
    def get_summarizer(summarizer: Summarizers):
        match summarizer:
            case Summarizers.average_player_summarizer:
                return model.average_player_summarizer.AveragePlayerSummarizer()
            case _:
                # TODO: Shouldn't throw generic Exception
                raise Exception("Unsupported summarizer specified.")