from players.models.player import Player
from players.views.player_view import PlayerView


class PlayerController:
    @classmethod
    def list(cls, store, players=None):
        if players is None:
            players = list(store.players.values())
        players.sort(key=lambda player: player.id)
        choice, player_id = PlayerView.display_list(players)

        if choice == "1":
            return "view_player", player_id
        elif choice == "2":
            return "new_player", None
        elif choice == "3":
            return "delete_player", player_id
        elif choice == "4":
            return "list_players_by_ranking", players
        elif choice == "5":
            return "list_players_by_name", players
        elif choice.lower() == "q":
            return "quit", None
        elif choice.lower() == "h":
            return "homepage", None
        else:
            return "error", "Invalide choice"

    @classmethod
    def list_players_by_ranking(cls, store, players=None):
        if players is None:
            players = list(store.players.values())
        players.sort(key=lambda player: -int(player.ranking))
        choice, player_id = PlayerView.display_list(players)

        if choice == "1":
            return "view_player", player_id
        elif choice == "2":
            return "new_player", None
        elif choice == "3":
            return "delete_player", player_id
        elif choice == "4":
            return "list_players_by_ranking", players
        elif choice == "5":
            return "list_players_by_name", players
        elif choice.lower() == "q":
            return "quit", None
        elif choice.lower() == "h":
            return "homepage", None
        else:
            return "error", "Invalide choice"

    @classmethod
    def list_players_by_name(cls, store, players=None):
        if players is None:
            players = list(store.players.values())
        players.sort(key=lambda player: player.first_name.lower())
        choice, player_id = PlayerView.display_list(players)

        if choice == "1":
            return "view_player", player_id
        elif choice == "2":
            return "new_player", None
        elif choice == "3":
            return "delete_player", player_id
        elif choice == "4":
            return "list_players_by_ranking", players
        elif choice == "5":
            return "list_players_by_name", players
        elif choice.lower() == "q":
            return "quit", None
        elif choice.lower() == "h":
            return "homepage", None
        else:
            return "error", "Invalide choice"

    @classmethod
    def create(cls, store, route_params=None):
        # call the view that will return us a dict with the new player info
        data = PlayerView.create_player()

        # You could specify each argument like:
        # player = Player(id=data["id"], name=data["name"], age=data["age"])
        # but it's easier to use `**` to pass the arguments
        new_id = len(store.players)
        player = Player(**data, id=new_id)

        # we add the player to the store
        store.players[player.id] = player

        return "list_player", None

    @classmethod
    def delete(cls, store, route_params):
        # remove the player from the store
        try:
            del store.players[route_params]
        except KeyError:
            return "error", "This player doesn't exist"
        return "list_player", None

    @classmethod
    def view(cls, store, route_params):
        """
        Display one single player, the route_params correspond to the player ID
        we want to display
        """
        # search the player on the store
        try:
            player = store.players[route_params]
        except KeyError:
            return "error", "This player doesn't exist"

        # we pass the player to the view that will display the player info and
        # the next options
        choice = PlayerView.detail_player(player)
        if choice.lower() == "q":
            return "quit", None
        elif choice.lower() == "h":
            return "homepage", None
