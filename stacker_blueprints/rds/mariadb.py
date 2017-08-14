from .base import MasterInstance, ReadReplica


class MariaDBMixin(object):
    def engine(self):
        return "mariadb"


class MasterInstance(MariaDBMixin, MasterInstance):
    pass


class ReadReplica(MariaDBMixin, ReadReplica):
    pass
