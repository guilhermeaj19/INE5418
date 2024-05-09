import zmq
import time


def client():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    for request in range(1, 6):

        socket.send_string(f"Sending Request {request}")
        message = socket.recv_string()
        print(f"Received reply {request}: {message}")
        time.sleep(1)


if __name__ == "__main__":
    client()
