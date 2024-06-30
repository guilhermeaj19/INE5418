from tuplespace.tuple_space_connection import TupleSpaceConnection


class Producer:
    def __init__(self, tuplespace_adrs: str = "127.0.0.1:5590"):
        self.__tuplespace = TupleSpaceConnection(tuplespace_adrs)

    def solve_passwords(self, filename: str, mode: str, param: str = None):
        """Modos: range (números), list (fornecida pelos consumers)

        range: parâmetro no formato (a-b), ex: 0-10000000
        list: parâmetro especifica qual lista utilizar
        """

        file = open(filename)
        passwords = file.readlines()

        for password in passwords:
            # TODO: verificar o formato da tupla
            tuple_ = password.split()[0]
            self.__tuplespace.write((tuple_, mode, param))
