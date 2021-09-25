from players.models.constant import trad_routes


def print_choices(routes, overrides=None):
    mapping = {}
    index = 1
    for route in routes:
        selector = str(index)
        if route == "quit":
            selector = "q"
        elif route == "homepage":
            selector = "h"
        else:
            index += 1

        mapping[selector] = route
        if overrides and route in overrides:
            print(f"{selector.upper()}. {overrides.get(route)}")
        else:
            print(f"{selector.upper()}. {trad_routes.get(route)}")
    return mapping
