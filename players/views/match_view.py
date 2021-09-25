from players.views.utils import print_choices


class MatchView:
    @classmethod
    def list(cls, matchs):
        print("\tID\tPlayer1\tPlayer2\tStatus")
        for m in matchs:
            if m.score is None:
                status = "WAITING FOR PLAY"
            elif m.score == 0:
                status = f"Winner is {m.player1.first_name}"
            elif m.score == 1:
                status = f"Winner is {m.player2.first_name}"
            elif m.score == 2:
                status = "Match null"
            print(f"\t{m.id}\t{m.player1.first_name}\t{m.player2.first_name}\t{status}")
        routes = ["play_match", "homepage", "quit"]
        all_cleared = True
        for match in matchs:
            if match.score is None:
                all_cleared = False
                break
        if all_cleared:
            routes.append("finish_round")
        mapping = print_choices(routes)
        choice = input("Choice:")
        extra_info = None

        if choice == "1":
            extra_info = int(input("Enter match Id:"))

        return choice, mapping, extra_info

    @classmethod
    def play(cls, match):
        print(f"{match.player1.first_name} vs {match.player2.first_name}")

        mapping = print_choices(
            ["player1_win", "player2_win", "null"],
            {
                "player1_win": "Player 1 win",
                "player2_win": "Player 2 win",
                "null": "Match is null",
            },
        )

        return input("Choice:"), mapping, None
