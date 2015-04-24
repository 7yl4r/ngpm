import re


def get_space_name(string):
    # convert CamelCase or hyphen-delimited to "space name"
    # camel-case to spaces
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1 \2', string)
    s2 = re.sub('([a-z0-9])([A-Z])', r'\1 \2', s1).lower()
    # hyphens to spaces
    return s2.replace('-', ' ')


def get_hyphen_name(name):
    name = get_space_name(name)
    name.replace(" ", "-")
    return name


def get_camel_name(name):
    name = get_space_name(name)
    words = name.split(' ')
    if len(words) == 1:
        return words[0]
    elif len(words) > 1:
        c_name = words[0]
        for word in words[1:]:
            c_name += word.title()
        return c_name
    else:
        raise ValueError('wordlist ' + str(words) + 'len < 1')