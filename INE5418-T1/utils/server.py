import zmq


def server():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    while True:
        message = socket.recv_string()
        print("Received request: %s" % message)
        response = f"Hello {message}"
        socket.send_string(response)


if __name__ == "__main__":
    server()
