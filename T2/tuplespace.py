
class TupleSpace:
    def __init__(self, init_tuples: list = []):
        self.__size = len(init_tuples)
        self.__tuples = init_tuples

    def __find_tuple_index(self, tuple_to_find):
        size_tuple_to_find = len(tuple_to_find)

        for index in range(self.__size):
            tuple_checking = self.__tuples[index]

            if len(tuple_checking) == size_tuple_to_find:
                valid_tuple = [(tuple_to_find[i] == "*" or \
                                tuple_to_find[i] == tuple_checking[i]) \
                                                for i in range(len(tuple_to_find))]

                if all(valid_tuple):
                    return index
        return None

    #Retira uma tupla, se encontrada, do espaço
    def get_tuple(self, tuple_) -> tuple:
        index_in_tuplespace = self.__find_tuple_index(tuple_)
        if index_in_tuplespace:
            self.__size -= 1
            return self.__tuples.pop(index_in_tuplespace)
    
    #Devolve uma tupla, se encontrada no espaço (sem removê-la)
    def read(self, tuple_) -> tuple:
        index_in_tuplespace = self.__find_tuple_index(tuple_)
        if index_in_tuplespace:
            return self.__tuples[index_in_tuplespace]

    #Adiciona uma tupla ao espaço
    def write(self, tuple_) -> None:
        self.__tuples.append(tuple_)
        self.__size += 1

# if __name__ == "__main__":
#     t = TupleSpace([(1,1,1),(0,0,0),(4,3,2),(231,5,21,12,2),(4,3,1),(5,3,1,5)])
#     t.write((0,0,31,2))
#     print(t.read(("*","*","*","*",2)))
#     print(t.read(("*","*","*",5)))
#     print(t.read((4,3,4)))
#     print(t.get_tuple(("*","*","*","*",2)))
#     print(t.get_tuple(("*","*","*",5)))
#     print(t.get_tuple(("*",0,"*")))