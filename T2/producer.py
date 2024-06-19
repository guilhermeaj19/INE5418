
from tupleSpaceConnection import TupleSpaceConnection

class Producer:
    def __init__(self, tuplespace_adrs: str = '127.0.0.1:2181'):
        self.__tuplespace = TupleSpaceConnection(tuplespace_adrs)
    
    def solve_passwords(self, filename: str):
        file = open(filename)
        passwords = file.readlines()

        for password in passwords:
            #TODO: verificar o formato da tupla
            tuple_ = password.split()
            self.__tuplespace.write(tuple_)
