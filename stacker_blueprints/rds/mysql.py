from .base import MasterInstance, ReadReplica


class MySQLMixin(object):
    def engine(self):
        return "MySQL"

    def port(self):
        return 3306

class MasterInstance(MySQLMixin, MasterInstance):
    pass


class ReadReplica(MySQLMixin, ReadReplica):
    pass
