from players.views.utils import print_choices


class RoundView:
    @classmethod
    def display_list(cls, rounds):
        print("\tID\tStatus\tDate start\tDate end")
        nb_finished = 0
        for r in rounds:
            status = r.get_progress()
            if int(status) == 100:
                nb_finished += 1
            print(f"\t{r.id}\t{status}\t{r.date_start}\t{r.date_end}")
        choices = ["view_round", "new_round", "quit", "homepage"]
        overrides = {}
        if nb_finished == len(rounds):
            choices.insert(1, "finish_tournament")
            overrides["finish_tournament"] = "All rounds are ended, finish tournament ?"

        mapping = print_choices(choices, overrides)
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
