from .base import MasterInstance, ReadReplica


class MariaDBMixin(object):
    def engine(self):
        return "mariadb"

    def port(self):
        return 3306


class MasterInstance(MariaDBMixin, MasterInstance):
    pass


class ReadReplica(MariaDBMixin, ReadReplica):
    pass
