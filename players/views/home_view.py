from players.models.constant import trad_routes


class HomeView:

    routes = [
        "list_player",
        "list_players_by_ranking",
        "list_tournament",
        "save_store",
        "import_saved_store",
        "quit",
    ]

    @classmethod
    def home(self):
        print("Welcome\n")
        mapping = {}
        index = 1
        for route in self.routes:
            selector = str(index)
            if route == "quit":
                selector = "q"
            else:
                index += 1

            mapping[selector] = route
            print(f"{selector.upper()}. {trad_routes.get(route)}")
        choice = input("Choice: ")
        return choice, mapping
