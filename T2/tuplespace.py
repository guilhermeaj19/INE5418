


class TupleSpace:
    def __init__(self, init_tuples: list = []):
        self.__size = len(init_tuples)
        self.__tuples = init_tuples

    #Retira uma tupla, se encontrada, do espaço
    def getTuple(self, tuple_) -> tuple:
        pass
    
    #Devolve uma tupla, se encontrada no espaço (sem removê-la)
    def read(self, tuple_) -> tuple:
        pass
    
    #Adiciona uma tupla ao espaço
    def write(self, tuple_) -> None:
        pass