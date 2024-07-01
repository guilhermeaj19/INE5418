import zmq

class Archiver:
    def __init__(self) -> None:

        context = zmq.Context()
        self.__from_solver_mq = context.socket(zmq.SUB)
        self.__from_solver_mq.bind("tcp://*:63000")
        self.__from_solver_mq.setsockopt_string(zmq.SUBSCRIBE, "")

    def wait_result(self, callback=None):
        while True:
            data = self.__from_solver_mq.recv_json()
            if callback == None:
                callback = print
            callback(data)