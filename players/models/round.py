from datetime import date

from players.models.match import Match


class Round:
    def __init__(
        self, id, tournament, players, date_start=None, date_end=None, matchs=None
    ) -> None:
        self.tournament = tournament
        self.players = players
        self.matchs = matchs
        self.date_start = date.today()
        self.date_end = None
        self.id = id

    def to_serialize(self):
        date_end = self.date_end.strftime('%Y-%m-%d') if isinstance(self.date_end, date) else ""
        return {
            "players": [player.id for player in self.players],
            "matchs": [match.to_serialize() for match in self.matchs],
            "date_start": self.date_start.isoformat(),
            "date_end": date_end,
            "id": self.id,
        }

    @classmethod
    def to_deserialize(cls, serialized_round, tournament, players):
        round = cls(
            id=serialized_round["id"],
            tournament=tournament,
            players=players,
            date_start=serialized_round["date_start"],
            date_end=serialized_round["date_end"],
        )
        players_list = {}
        for player in players:
            players_list[player.id] = player
        round.matchs = []
        for match in serialized_round["matchs"]:
            round.matchs.append(
                Match.to_deserialize(
                    match,
                    round,
                    tournament,
                    players_list[match["player1"]],
                    players_list[match["player2"]],
                )
            )
        return round

    def get_player_game_with(self, player):
        for match in self.matchs:
            if match.player1.id == player.id:
                return match.player2
            if match.player2.id == player.id:
                return match.player1
        return None

    def get_progress(self):
        if self.matchs is None or len(self.matchs) == 0:
            return 0
        progress = 0
        for match in self.matchs:
            if match.score is not None:
                progress += 1

        return (progress / len(self.matchs)) * 100
