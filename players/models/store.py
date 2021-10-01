from tinydb import Query, TinyDB

from players.models.player import Player
from players.models.tournament import Tournament


class Store:
    def __init__(self, tournaments={}, players={}):
        self.tournaments_db = TinyDB("tournaments_db.json")
        self.players_db = TinyDB("players_db.json")
        self.tournaments = tournaments
        self.players = players

    def save_store(self):
        PlayerQuery = Query()
        for player in self.players.values():
            res_query = self.players_db.search(PlayerQuery.id == player.id)
            if res_query != []:
                self.players_db.update(player.to_serialize(), PlayerQuery.id == player.id)
            else:
                self.players_db.insert(player.to_serialize())
        TournamentQuery = Query()
        for tournament in self.tournaments.values():
            res_query = self.tournaments_db.search(TournamentQuery.id == tournament.id)
            if res_query != []:
                self.tournaments_db.update(
                    tournament.to_serialize(), TournamentQuery.id == tournament.id
                )
            else:
                self.tournaments_db.insert(tournament.to_serialize())

    def import_saved_store(self):
        for tournament in self.tournaments_db.all():
            self.tournaments[tournament["id"]] = Tournament.to_deserialize(tournament)
        for player in self.players_db.all():
            self.players[player["id"]] = Player.to_deserialize(player)

    def get_round(self, round_id):
        for tournament in self.tournaments.values():
            rounds = [r for r in tournament.rounds if r.id == round_id]
            if len(rounds) != 0:
                return rounds[0]
        return None

    def get_match(self, match_id):
        for tournament in self.tournaments.values():
            rounds = tournament.rounds
            for round in rounds:
                matchs = [m for m in round.matchs if m.id == match_id]
                if len(matchs) != 0:
                    return matchs[0]
        return None

    def nb_matchs(self):
        nb_matchs = 0
        for tournament in self.tournaments.values():
            nb_matchs = nb_matchs + tournament.nb_matchs()
        return nb_matchs

    def nb_rounds(self):
        nb_rounds = 0
        for tournament in self.tournaments.values():
           nb_rounds = nb_rounds + len(tournament.rounds)
        return nb_rounds

