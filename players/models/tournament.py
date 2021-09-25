from datetime import date

from players.models.player import Player
from players.models.round import Round


class Tournament:
    def __init__(
        self,
        id,
        name,
        place,
        date,
        time_type,
        description,
        scores=None,
        nb_turns=None,
        rounds=None,
        players=None,
        status=None,
    ) -> None:
        self.name = name
        self.place = place
        self.date = date
        self.nb_turns = nb_turns
        self.rounds = rounds
        self.players = players
        self.time_type = time_type
        self.description = description
        self.scores = scores or {}
        self.status = status
        self.id = id

    def to_serialize(self):
        rounds = []
        players = []
        if self.rounds:
            rounds = [r.to_serialize() for r in self.rounds]
        if self.players:
            players = [p.to_serialize() for p in self.players]
        d = self.date
        if isinstance(d, date):
            d = date.isoformat()
        return {
            "name": self.name,
            "place": self.place,
            "date": d,
            "nb_turns": self.nb_turns,
            "rounds": rounds,
            "players": players,
            "time_type": self.time_type,
            "description": self.description,
            "scores": self.scores,
            "status": self.status,
            "id": self.id,
        }

    @classmethod
    def to_deserialize(cls, serialized_tournament):
        players = [Player.to_deserialize(player) for player in serialized_tournament["players"]]
        tournament = Tournament(
            id=serialized_tournament["id"],
            name=serialized_tournament["name"],
            place=serialized_tournament["place"],
            date=serialized_tournament["date"],
            nb_turns=serialized_tournament["nb_turns"],
            players=players,
            time_type=serialized_tournament["time_type"],
            description=serialized_tournament["description"],
            scores=serialized_tournament["scores"],
            status=serialized_tournament["status"],
        )
        rounds = [
            Round.to_deserialize(r, tournament, players) for r in serialized_tournament["rounds"]
        ]
        tournament.rounds = rounds
        return tournament

    def set_player_score(self, player, score):
        self.scores[player.id] = score

    def get_score(self, player):
        if player.id in self.scores:
            return self.scores[player.id]
        return 0

    def player_win_match(self, player):
        if player.id in self.scores:
            self.scores[player.id] = self.scores[player.id] + 1
        else:
            self.scores[player.id] = 0

    def players_match_null(self, player1, player2):
        if player1.id in self.scores:
            self.scores[player1.id] = self.scores[player1.id] + 0.5
        else:
            self.scores[player1.id] = 0
        if player2.id in self.scores:
            self.scores[player2.id] = self.scores[player2.id] + 0.5
        else:
            self.scores[player2.id] = 0

    def has_players_game_with(self, player1, player2):
        for round in self.rounds:
            player_game_with_1 = round.get_player_game_with(player1)
            if player_game_with_1 is not None and player_game_with_1.id == player2.id:
                return True
        return False

    def get_associate_player_with_next_playable_player(self, player, players_list):
        for associate_player in players_list:
            if not self.has_players_game_with(player, associate_player):
                return associate_player
        return None

    def nb_matchs(self):
        nb_matchs = 0
        for length in [len(r.matchs) for r in self.rounds]:
            nb_matchs += length
        return nb_matchs
