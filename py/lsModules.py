import utils


def ls(search_str=None):
    # list packages from package.json
    data = utils.get_package_json()
    num = 1
    for module in data['browser']:
        if search_str is None or search_str in module:
            print str(num) + ':', module
            num += 1