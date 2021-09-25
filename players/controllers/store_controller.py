from players.models.store import Store
from players.views.store_view import StoreView


class StoreController:
    @classmethod
    def save_store(cls, store=None, input=None):
        if isinstance(store, Store):
            store.save_store()
            success = True
        else:
            success = False
        StoreView.save_store(success)
        return "homepage", None

    @classmethod
    def import_saved_store(cls, store=None, input=None):
        if isinstance(store, Store):
            store.import_saved_store()
            success = True
        else:
            success = False
        StoreView.import_saved_store(success)
        return "homepage", None
