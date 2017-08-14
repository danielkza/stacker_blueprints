from .base import MasterInstance, ReadReplica


class PostgresMixin(object):
    def engine(self):
        return "postgres"

    def port(self):
        return 5432

class MasterInstance(PostgresMixin, MasterInstance):
    pass


class ReadReplica(PostgresMixin, ReadReplica):
    pass
