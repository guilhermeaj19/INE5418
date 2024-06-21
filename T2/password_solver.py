from tuple_space_connection import TupleSpaceConnection
import zmq

class PasswordSolver:
    def __init__(self, tuplespace_adrs: str = '127.0.0.1:2181', archiver_adr: str = 'localhost:63000') -> None:
        self.__tuplespace = TupleSpaceConnection(tuplespace_adrs)
        context = zmq.Context()
        self.__to_archiver_mq = context.socket(zmq.PUB)
        self.__to_archiver_mq.connect(addr=archiver_adr)
    
    def wait_password(self):
        while True:
            #TODO: verificar como será o formato da tupla
            tuple_password = self.__tuplespace.get(...)
    
    def solve_password(self, tuple_password):
        """
            TODO: implementar o solver
        """
        data = {'Password Criptografada': ..., 'Password real': ...}
        self.__to_archiver_mq.send(data)
