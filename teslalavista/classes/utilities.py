

class Utilities:

    @staticmethod
    def set_if_available(key: str, json_dict: dict):
        """
        Args:
            key (str):
            json_dict (dict):
        """
        if key in json_dict:
            return json_dict[key]
        else:
            return None