from datetime import date

from players.views.utils import print_choices


class TournamentView:
    @classmethod
    def display_list(cls, tournaments):

        print("\tID\tName\tPlace\tDate\tStatus")
        for tournament in tournaments:
            print(
                f"\t{tournament.id}\t{tournament.name}\t{tournament.place}\t{tournament.date}\t{tournament.status}"
            )

        mapping = print_choices(["view_tournament", "new_tournament", "homepage", "quit"])
        choice = input("Choice: ")
        extra_info = None

        if choice == "1":
            extra_info = int(input("Enter Tournament Id:"))

        return choice, mapping, extra_info

    @classmethod
    def detail_tournament(cls, tournament):
        print(f"Id: {tournament.id}")
        print(f"Name: {tournament.name}")
        print(f"Status : {tournament.status}")
        print(f"Place: {tournament.place}")
        nb_players = 0
        if tournament.players:
            nb_players = len(tournament.players)
        print(f"Number of players: {nb_players}")
        print(f"Number of turns: {tournament.nb_turns}")
        print(f"Control of time: {tournament.time_type}")
        print(f"Description: {tournament.description}")

        mapping = print_choices(
            [
                "play_tournament",
                "list_round",
                "list_match",
                "list_player",
                "list_players_by_ranking",
                "select_all_players",
                "select_players",
                "deselect_players",
                "homepage",
                "quit",
            ]
        )

        return input("Choice: "), mapping, None

    @classmethod
    def select_players(cls, players_available, tournament):
        print("List of available players:")
        print("\tID\tFirst name\tLast name")
        for p in players_available:
            print(f"\t{p.id}\t{p.first_name}\t{p.last_name}")

        mapping = print_choices(
            ["select_players", "select_all_players", "view_tournament", "quit", "homepage"],
            {"view_tournament": "End of selection"},
        )

        choice = input("Choice:")
        extra_info = None

        if choice == "1":
            extra_info = int(input("Enter Player Id:"))

        return choice, mapping, extra_info

    @classmethod
    def deselect_players(cls, players_available, tournament):
        print("List of available players:")
        print("\tID\tFirst name\tLast name")
        for p in players_available:
            print(f"\t{p.id}\t{p.first_name}\t{p.last_name}")

        print("1. Deselect player")
        print("2. End of selection")
        print("Q. Exit")
        print("H. Homepage")

        choice = input("Choice:")
        extra_info = None

        if choice == "1":
            extra_info = int(input("Enter Player Id:"))

        return choice, extra_info

    @classmethod
    def create_tournament(cls):
        return {
            "name": input("Enter a name: "),
            "date": date.today(),
            "place": input("Enter a place: "),
            "time_type": input("Enter control of time: "),
            "description": input("Enter description: "),
        }
