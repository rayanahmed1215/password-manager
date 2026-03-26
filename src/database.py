class Database:
    def __init__(self, storage: dict[str, dict[str, str]] | None = None):
        self._storage = storage

    def add(self, key: str, value: dict[str, str]) -> None:
        self._storage[key] = value


    