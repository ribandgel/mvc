class StoreView:
    @classmethod
    def save_store(cls, success):
        if success:
            print("Saved successfully\n")
        else:
            print("Error")
        input("Press any key to return homepage...")

    @classmethod
    def import_saved_store(cls, success):
        if success:
            print("Successfull while importing saved store\n")
        else:
            print("Error")
        input("Press any key to return homepage...")
