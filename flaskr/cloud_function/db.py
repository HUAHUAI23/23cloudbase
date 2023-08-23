from pymongo import MongoClient

# uri "mongodb://localhost:27017/"
# database name
# client = MongoClient("mongodb://localhost:27017/")
# db = client["test-database"]


class Db:
    _client = None
    _db = None

    def __init__(self, uri, database_name):
        self.uri = uri
        self.database_name = database_name

        # Ensure the client exists
        if not Db._client:
            Db._initialize_client(self.uri)

        # Ensure the database connection exists
        if not Db._db:
            Db._initialize_db(self.database_name)

    @classmethod
    def _initialize_client(cls, uri):
        if cls._client is None:
            cls._client = MongoClient(uri)

    @classmethod
    def _initialize_db(cls, database_name):
        if cls._client and cls._db is None:
            cls._db = cls._client[database_name]

    @classmethod
    def _close_client(cls):
        if cls._client:
            cls._client.close()
        else:
            raise Exception("DB Client is not initialized")

    @property
    def client(self):
        return Db._client

    @property
    def db(self):
        return Db._db
