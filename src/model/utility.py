class Utility:
    """
    Check the json_data for a value associated with the provided key.  If no
    such key exists, return the default value instead.

    TODO: Does this need to be broadly available or can it be a staticmethod
    on the player_info class?
    """
    @staticmethod
    def json_value_or_default(json_data, key, default=0):
        try:
            return json_data[key]
        except KeyError:
            # TODO: Log
            return default