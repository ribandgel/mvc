from players.views.home_view import HomeView


class HomePageController:
    @classmethod
    def dispatch(cls, store=None, input=None):
        choice, mapping = HomeView.home()
        if mapping.get(choice.lower()):
            return mapping.get(choice.lower()), None

        return "error", "Invalide choice"
