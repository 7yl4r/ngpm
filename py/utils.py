import json

import CONFIG


def get_package_json():
    with open(CONFIG.package_json) as json_file:
        return json.load(json_file)