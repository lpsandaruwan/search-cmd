from tinydb import TinyDB, Query


class DBMediator(object):
    __instance = None

    def __new__(cls):
        if DBMediator.__instance is None:
            DBMediator.__instance = object.__new__(cls)
            DBMediator.__instance.Model = Query()
        return DBMediator.__instance

    @staticmethod
    def get_db(db_file):
        return TinyDB(db_file)

    @staticmethod
    def get_query():
        return Query()


db_mediator_instance = DBMediator()
