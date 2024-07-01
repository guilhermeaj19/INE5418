from tuplespace.tuple_space_connection import TupleSpaceConnection
import zmq
import hashlib
from passwordbruteforce.brute_forcer import BruteForcer

class PasswordSolver:
    def __init__(self, tuplespace_adrs: str = '127.0.0.1:5590', archiver_adr: str = 'tcp://127.0.0.1:63000') -> None:
        self.__tuplespace = TupleSpaceConnection(tuplespace_adrs)
        context = zmq.Context()
        self.__to_archiver_mq = context.socket(zmq.PUB)
        self.__to_archiver_mq.connect(addr=archiver_adr)
        self.brute_forcer = BruteForcer()

    def wait_password(self, callback=None):
        while True:
            tuple_password = self.__tuplespace.get(["*","*","*"])
            passwd = self.brute_forcer.force(*tuple_password, callback=callback)
            if passwd is not None:
                self.solve_password(tuple_password[0], passwd)
    
    def solve_password(self, criptografada, real):
        """
            TODO: implementar o solver
        """
        data = {'Senha criptografada': criptografada, 'Senha real': real}
        self.__to_archiver_mq.send_json(data)
