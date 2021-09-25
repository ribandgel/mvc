from datetime import date

from players.models.match import Match
from players.models.round import Round
from players.views.round_view import RoundView


class RoundController:
    @classmethod
    def list(cls, store, rounds):
        choice, mapping, extra_info = RoundView.display_list(rounds)
        route = mapping.get(choice.lower())
        if route:
            if route == "new_round":
                if len(rounds) == 0:
                    return "list_tournament", None
                extra_info = rounds[0].tournament
            return route, extra_info

        return "error", "Invalide choice"

    @classmethod
    def create(cls, store, tournament):
        # Create next round

        players = list(tournament.players)
        import pdb

        pdb.set_trace()
        players.sort(key=lambda player: (-player.ranking, -tournament.get_score(player)))
        next_round = Round(
            id=len(tournament.rounds), tournament=tournament, players=tournament.players, matchs=[]
        )

        tournament.rounds.append(next_round)
        tournament.nb_turns += 1
        for player_index in range(0, len(players) // 2):
            if not len(players) >= 2:
                break
            player = players[0]
            if player in players:
                players.pop(players.index(player))
                associate_player = tournament.get_associate_player_with_next_playable_player(
                    player, players
                )
                if associate_player is not None:
                    players.pop(players.index(associate_player))
                    match = Match(
                        id=store.nb_matchs() + 1,
                        round=next_round,
                        tournament=tournament,
                        player1=player,
                        player2=associate_player,
                        score=None,
                    )
                    next_round.matchs.append(match)
        return "list_round", tournament.rounds

    @classmethod
    def view(cls, store, extra_info):
        round = store.get_round(extra_info)
        if round is None:
            return "error", "This round doesn't exist"
        if round.get_progress() == 100:
            return "finish_round", round.id
        return "list_match", round.matchs

    @classmethod
    def finish(cls, store, extra_info):
        round = store.get_round(extra_info)
        if round is None:
            return "error", "This round doesn't exist"
        # End screen of round, create a new one or finsih round
        round.date_end = date.today()
        choice, mapping, extra_info = RoundView.finish(round)

        route = mapping.get(choice.lower())
        if route:
            if route == "new_round" or route == "finish_tournament":
                return route, round.tournament
            return route, extra_info

        return "error", "Invalide choice"
