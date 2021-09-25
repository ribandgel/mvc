import subprocess as sp

from players.controllers.error_controller import ErrorController
from players.controllers.home_controller import HomePageController
from players.controllers.match_controller import MatchController
from players.controllers.player_controller import PlayerController
from players.controllers.round_controller import RoundController
from players.controllers.store_controller import StoreController
from players.controllers.tournament_controller import TournamentController
from players.models.store import Store


class Application:

    routes = {
        "homepage": HomePageController.dispatch,
        "list_player": PlayerController.list,
        "new_player": PlayerController.create,
        "view_player": PlayerController.view,
        "delete_player": PlayerController.delete,
        "list_tournament": TournamentController.list,
        "list_players_by_ranking": PlayerController.list_players_by_ranking,
        "list_players_by_name": PlayerController.list_players_by_name,
        "new_tournament": TournamentController.create,
        "view_tournament": TournamentController.view,
        "select_players": TournamentController.select_players,
        "select_all_players": TournamentController.select_all_players,
        "deselect_players": TournamentController.deselect_players,
        "play_tournament": TournamentController.play,
        "finish_tournament": TournamentController.finish,
        "list_round": RoundController.list,
        "new_round": RoundController.create,
        "view_round": RoundController.view,
        "finish_round": RoundController.finish,
        "list_match": MatchController.list,
        "play_match": MatchController.play,
        "save_store": StoreController.save_store,
        "import_saved_store": StoreController.import_saved_store,
        "error": ErrorController.error,
    }

    def __init__(self) -> None:
        self.route = "homepage"
        self.exit = False
        self.route_params = None
        self.store = Store()

    def run(self):
        while not self.exit:
            # Clear the shell output
            sp.call("clear", shell=True)

            # Get the controller method that should handle our current route
            controller_method = self.routes[self.route]

            # Call the controller method, we pass the store and the route's
            # parameters.
            # Every controller should return two things:
            # - the next route to display
            # - the parameters needed for the next route
            next_route, next_params = controller_method(self.store, self.route_params)

            # set the next route and input
            self.route = next_route
            self.route_params = next_params

            # if the controller returned "quit" then we end the loop
            if next_route == "quit":
                self.store.save_store()
                self.exit = True
