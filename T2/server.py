from kazoo.client import KazooClient
from kazoo.exceptions import NoNodeError
import threading
import json
import uuid

class TupleSpaceConnection:
    def __init__(self, zookeeper_hosts='127.0.0.1:2181', namespace='/tuple_space'):
        self.zk = KazooClient(hosts=zookeeper_hosts)
        self.zk.start()
        self.namespace = namespace
        self.zk.ensure_path(self.namespace)
        self.lock = threading.Lock()
    
    def _tuple_path(self, tuple_id):
        return f"{self.namespace}/{tuple_id}"

    def write(self, tuple_data):
        tuple_id = str(uuid.uuid4())
        path = self._tuple_path(tuple_id)
        self.zk.create(path, json.dumps(tuple_data).encode('utf-8'))
        print(f"Tuple written: {tuple_data} with id: {tuple_id}")

    def read(self, query):
        tuples = []
        for tuple_id in self.zk.get_children(self.namespace):
            path = self._tuple_path(tuple_id)
            try:
                data, _ = self.zk.get(path)
                tuple_data = json.loads(data.decode('utf-8'))
                if self._matches(query, tuple_data):
                    tuples.append(tuple_data)
            except NoNodeError:
                print("NoNodeError on TupleSpaceConnection.read(). Continuing...")
                continue
        if tuples:
            # print(f"Tuples read: {tuples}")
            return tuples[0]  # return the first matching tuple
        # print("No matching tuple found")
        return []

    def get(self, query):
        printed_block = False
        while True:
            with self.lock:
                for tuple_id in self.zk.get_children(self.namespace):
                    path = self._tuple_path(tuple_id)
                    try:
                        data, _ = self.zk.get(path)
                        tuple_data = json.loads(data.decode('utf-8'))
                        if self._matches(query, tuple_data):
                            self.zk.delete(path)
                            print(f"Tuple retrieved and removed: {tuple_data}")
                            return tuple_data
                    except NoNodeError:
                        continue
            if not printed_block:
                printed_block = True
                print("Blocking on get, no matching tuple found. Waiting...")
            threading.Event().wait(1)

    def _block(self):
        pass

    def _matches(self, query, tuple_data):
        if len(query) != len(tuple_data):
            return False
        for q, d in zip(query, tuple_data):
            if q != '*' and q != d:
                return False
        return True

    def close(self):
        self.zk.stop()
        self.zk.close()

def test(server: TupleSpaceConnection):

    # Exemplo de escrita
    server.write(["INE5418", "Fulano", "8.5", "80"])

    # Exemplo de leitura
    print(server.read(["INE5418", "*", "*", "*"]))

    # Exemplo de obtenção (get)
    print(server.get(["INE5418", "Fulano", "*", "*"]))

    server.close()