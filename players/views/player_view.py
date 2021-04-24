class PlayerView:

    @classmethod
    def display_list(cls, players):
        print("\tID\tName\tAge")
        for player in players:
            print(f"\t{player.id}\t{player.name}\t{player.age}")

        print("1. View Player")
        print("2. New Player")
        print("3. Delete Player")
        print("4. Update Player")
        print("Q. Exit")
        print("H. Homepage")

        choice = input("Choice:")
        extra_info = None

        if choice in ("1", "3", "4"):
            extra_info = int(input("Enter Player Id:"))

        return choice, extra_info

    @classmethod
    def detail_player(cls, player):
        print(f"Id: {player.id}")
        print(f"Name: {player.name}")
        print(f"Age: {player.age}")
        print(f"Email: {player.email}")

        print("Q. Exit")
        print("H. Homepage")
        return input("Choice:")

    @classmethod
    def create_player(cls):
        return {
            "id": input("Enter an ID: "),
            "name": input("Enter a name: "),
            "age": input("Enter an age: "),
            "email": input("Enter an email: ")
        }

    @classmethod
    def update(cls, player):
        return {
            "id": input(f"Enter a new ID [{player.id}]: "),
            "name": input(f"Enter a new name [{player.name}]: "),
            "age": input(f"Enter a new age [{player.age}]: "),
            "email": input(f"Enter a new email [{player.email}]: ")
        }