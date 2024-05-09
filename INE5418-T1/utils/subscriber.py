import zmq


def subscriber():
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect("tcp://localhost:5556")

    topic = "events"
    socket.setsockopt_string(zmq.SUBSCRIBE, topic)

    while True:
        message = socket.recv_string()
        topic, update = message.split()
        print(f"Received {topic} {update}")


if __name__ == "__main__":
    subscriber()
