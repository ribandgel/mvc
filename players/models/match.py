class Match:
    def __init__(self, id, round, tournament, player1, player2, score) -> None:
        self.round = round
        self.tournament = tournament
        self.player1 = player1
        self.player2 = player2
        self.score = score
        self.id = id

    def to_serialize(self):
        return {
            "player1": self.player1.id,
            "player2": self.player2.id,
            "score": self.score,
            "id": self.id,
        }

    @classmethod
    def to_deserialize(cls, serialized_match, round, tournament, player1, player2):
        return cls(
            id=serialized_match["id"],
            round=round,
            tournament=tournament,
            player1=player1,
            player2=player2,
            score=int(serialized_match["score"]) if serialized_match["score"] != None else None,
        )
