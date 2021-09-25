from players.views.error_view import ErrorView


class ErrorController:
    @classmethod
    def error(cls, store, message):
        ErrorView.error(message)
        return "homepage", None
