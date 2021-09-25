from players.views.match_view import MatchView


class MatchController:
    @classmethod
    def list(cls, store, matchs):
        choice, mapping, match_id = MatchView.list(matchs)
        route = mapping.get(choice.lower())
        if route:
            if route == "play_match" and match_id:
                matchs_ids = [m.id for m in matchs]
                if match_id in matchs_ids:
                    return route, match_id
                else:
                    return "error", "You can't play this match"
            elif route == "finish_round":
                return route, matchs[0].round
            return route, None

        return "error", "Invalide choice"

    @classmethod
    def play(cls, store, extra_info):
        match = store.get_match(extra_info)
        if match is None:
            return "error", "This match doesn't exist"

        choice, mapping, extra_info = MatchView.play(match)
        route = mapping.get(choice.lower())
        if route:
            if route == "player1_win":
                match.score = 0
                match.tournament.player_win_match(match.player1)
            if route == "player2_win":
                match.score = 1
                match.tournament.player_win_match(match.player2)
            if route == "null":
                match.score = 2
                match.tournament.players_match_null(match.player1, match.player2)
            return "view_round", match.round.id

        return "error", "Invalide choice"
