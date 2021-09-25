from players.views.utils import print_choices


class RoundView:
    @classmethod
    def display_list(cls, rounds):
        print("\tID\tStatus\tDate start\tDate end")
        for r in rounds:
            status = r.get_progress()
            print(f"\t{r.id}\t{status}\t{r.date_start}\t{r.date_end}")

        mapping = print_choices(["view_round", "new_round", "quit", "homepage"])
        choice = input("Choice:")
        extra_info = None

        if choice == "1":
            extra_info = int(input("Enter Round Id:"))

        return choice, mapping, extra_info

    @classmethod
    def finish(cls, round):
        print("Round ended")
        mapping = print_choices(["new_round", "finish_tournament", "quit", "homepage"])

        return input("Choice:"), mapping, None
