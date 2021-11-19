from players.models.match import Match
from players.models.round import Round
from players.models.tournament import Tournament
from players.views.tournament_view import TournamentView


class TournamentController:
    @classmethod
    def list(cls, store, route_params=None):
        choice, mapping, extra_info = TournamentView.display_list(store.tournaments.values())

        if mapping.get(choice.lower()):
            return mapping.get(choice.lower()), extra_info

        return "error", "Invalide choice"

    @classmethod
    def create(cls, store, route_params=None):
        # call the view that will return us a dict with the new tournament info
        data = TournamentView.create_tournament()
        new_id = len(store.tournaments.values())
        tournament = Tournament(id=new_id, **data)
        tournament.status = "WAITING PLAYERS"

        # we add the tournament to the store
        store.tournaments[tournament.id] = tournament

        return "list_tournament", None

    @classmethod
    def view(cls, store, route_params):
        """
        Display one single tournament, the route_params correspond to the tournament ID
        we want to display
        """
        # search the tournament on the store
        try:
            tournament = store.tournaments[route_params]
        except KeyError:
            return "error", "This tournament doesn't exist"

        # we pass the tournament to the view that will display the tournament info and
        # the next options
        choice, mapping, extra_info = TournamentView.detail_tournament(tournament)
        route = mapping.get(choice.lower())
        if route:
            if route == "list_round":
                extra_info = tournament.rounds
            elif route == "list_match":
                rounds = tournament.rounds
                matchs = []
                for round in rounds:
                    matchs += round.matchs
                extra_info = matchs
            elif route == "list_player" or route == "list_players_by_ranking":
                if tournament.players is not None:
                    displayed_players = list(tournament.players)
                    displayed_players.sort(key=lambda player: player.id)
                else:
                    displayed_players = []
                extra_info = displayed_players
            elif route in [
                "play_tournament",
                "select_players",
                "select_all_players",
                "deselect_players",
                "dislay_scores",
            ]:
                extra_info = tournament
            return route, extra_info

        return "error", "Invalide choice"

    @classmethod
    def select_players(cls, store, tournament):
        players_available = list(store.players.values())
        tournament.status = "WAITING ROUND"
        if tournament.players is not None:
            players_available = set(store.players.values()) - set(tournament.players)
            players_available = list(players_available)

        players_available.sort(key=lambda player: player.id)

        choice, mapping, player_id = TournamentView.select_players(players_available, tournament)
        route = mapping.get(choice.lower())
        if route:
            if route == "select_players" and player_id is not None:
                try:
                    player = store.players[player_id]
                except KeyError:
                    return "error", "This player doesn't exist"
                if tournament.players is None:
                    tournament.players = [player]
                else:
                    tournament.players.append(player)
                return route, tournament
            elif route == "select_all_players":
                return route, tournament
            else:
                return route, tournament.id

        return "error", "Invalide choice"

    @classmethod
    def select_all_players(cls, store, tournament):
        tournament.status = "WAITING ROUND"
        tournament.players = store.players.values()
        return "view_tournament", tournament.id

    @classmethod
    def deselect_players(cls, store, tournament):
        if tournament.players is None or len(tournament.players) == 0:
            return "error", "There is no player on this tournament"
        displayed_players = list(tournament.players)
        displayed_players.sort(key=lambda player: player.id)
        choice, player_id = TournamentView.deselect_players(displayed_players, tournament)
        try:
            player = store.players[player_id]
            tournament.players.remove(player)
        except KeyError:
            return "error", "This player doesn't exist"
        except ValueError:
            return "error", "This player is not in this tournament"

        if choice.lower() == "q":
            return "quit", None
        elif choice.lower() == "h":
            return "homepage", None

    @classmethod
    def play(cls, store, tournament):
        if tournament.status == "ENDED":
            return "list_tournament", None
        elif tournament.players is None or len(tournament.players) < 2:
            return "select_players", tournament
        elif tournament.rounds is not None and len(tournament.rounds) != 0:
            return "list_round", tournament.rounds
        tournament.status = "PLAYING"
        players = list(tournament.players)
        players.sort(key=lambda player: -int(player.ranking))
        middle_index = len(players) // 2
        first_part = players[:middle_index]
        second_part = players[middle_index:]
        first_round = Round(id=store.nb_rounds() + 1, tournament=tournament, players=tournament.players, matchs=[])
        tournament.rounds = [first_round]
        tournament.nb_turns = 1
        for player_index in range(0, len(first_part)):
            match = Match(
                id=store.nb_matchs() + 1,
                round=first_round,
                tournament=tournament,
                player1=first_part[player_index],
                player2=second_part[player_index],
                score=None,
            )
            first_round.matchs.append(match)
        return "list_round", tournament.rounds

    @classmethod
    def finish(cls, store, tournament):
        tournament.status = "ENDED"
        for player in store.players.values():
            player.ranking = int(player.ranking) + tournament.get_score(player)
        return "list_tournament", None
