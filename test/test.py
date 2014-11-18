import os

from test_runner import BaseComponentTestCase
from qubell.api.private.testing import instance, environment, workflow, values

@environment({
    "default": {},
})
class MSSQLComponentTestCase(BaseComponentTestCase):
    name = "component-mssql"
    apps = [{
        "name": name,
        "file": os.path.realpath(os.path.join(os.path.dirname(__file__), '../%s.yml' % name))
    }]
    @classmethod
    def timeout(cls):
        return 60
    @instance(byApplication=name)
    @values({"MSSQL.Database Host": "hosts"}, "MSSQL.Database listen port": "db-port")
    def test_port(self, instance, hosts, db-port):
        import socket
        import time
        time.sleep(60)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((hosts, int(port)))

        assert result == 0

