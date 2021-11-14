from players.views.utils import print_choices


class PlayerView:
    @classmethod
    def display_list(cls, players):
        print("\tID\tFirst name\tLast name\tRanking")
        for player in players:
            print(f"\t{player.id}\t{player.first_name}\t{player.last_name}\t{player.ranking}")

        print("1. View Player")
        print("2. New Player")
        print("3. Delete Player")
        print("4. List Players by rank")
        print("5. List Players by name")
        print("Q. Exit")
        print("H. Homepage")

        choice = input("Choice:")
        extra_info = None

        if choice in ("1", "3"):
            extra_info = int(input("Enter Player Id:"))

        return choice, extra_info

    @classmethod
    def detail_player(cls, player):
        print(f"Id: {player.id}")
        print(f"First name: {player.first_name}")
        print(f"Last name: {player.last_name}")
        print(f"Date of birth: {player.date_of_birth}")
        print(f"Sexe: {player.sexe}")
        print(f"Ranking: {player.ranking}")

        print("Q. Exit")
        print("H. Homepage")
        return input("Choice:")

    @classmethod
    def create_player(cls):
        return {
            "first_name": input("Enter first name: "),
            "last_name": input("Enter last name: "),
            "date_of_birth": input("Date of birth: "),
            "sexe": input("Enter sexe: "),
            "ranking": input("Enter ranking: "),
        }

    @classmethod
    def display_scores(cls, players, tournament):
        print("\tID\tFirst name\tLast name\tScores")
        for player in players:
            print(f"\t{player.id}\t{player.first_name}\t{player.last_name}\t{tournament.get_score(player)}")

        mapping = print_choices(
            ["view_tournament", "list_round", "display_scores", "homepage", "quit"], {"display_scores": "Edit score"}
        )
        choice = input("Choice: ")
        player_id = None
        if choice == "3":
            player_id = input("Enter Player Id:")
            score = input("Enter Score:")

        return choice, mapping, player_id, score
