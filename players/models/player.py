from datetime import date


class Player:
    def __init__(self, id, first_name, last_name, date_of_birth, sexe="", ranking=0) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.sexe = sexe
        self.ranking = ranking
        self.id = id

    def to_serialize(self):
        date_of_birth = self.date_of_birth.isoformat() if isinstance(self.date_of_birth, date) else self.date_of_birth
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "date_of_birth": date_of_birth,
            "sexe": self.sexe,
            "ranking": self.ranking,
            "id": self.id,
        }

    @classmethod
    def to_deserialize(cls, serialized_player):
        return cls(
            id=serialized_player["id"],
            first_name=serialized_player["first_name"],
            last_name=serialized_player["last_name"],
            date_of_birth=serialized_player["date_of_birth"],
            sexe=serialized_player["sexe"],
            ranking=serialized_player["ranking"],
        )
