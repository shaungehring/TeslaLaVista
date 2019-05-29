

class Utilities:

    @staticmethod
    def set_if_available(key, json_dict):
        if key in json_dict:
            return json_dict[key]
        else:
            return None