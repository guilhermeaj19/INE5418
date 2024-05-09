import zmq
from zmq.utils.monitor import recv_monitor_message

class ChatMonitor:
    def __init__(self, chat_name: str, socket: zmq.Socket):
        self.__chat_name = chat_name
        self.__monitor = socket
        self.__user_counter = 0

    def start_monitoring(self):
        while self.__monitor.poll():
            evt = dict()
            mon_evt = recv_monitor_message(self.__monitor)
            evt.update(mon_evt)

            if evt['event'] == zmq.EVENT_ACCEPTED:
                self.__user_counter += 1
                print(f"{self.__chat_name}\t|\tUsers connected: {self.__user_counter}")
            elif evt['event'] == zmq.EVENT_DISCONNECTED:
                self.__user_counter -= 1
                print(f"{self.__chat_name}\t|\tUsers connected: {self.__user_counter}")
            elif evt['event'] == zmq.EVENT_MONITOR_STOPPED:
                break

        self.__monitor.close()