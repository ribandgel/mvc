class ErrorView:
    @classmethod
    def error(cls, message):
        print(message)

        input("Press any key to return homepage...")
        return "homepage"
