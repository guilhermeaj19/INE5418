import zmq
import time


def publisher():
    context = zmq.Context()

    socket = context.socket(zmq.PUB)
    socket.bind("tcp://*:5556")

    topic = "events"

    for request in range(0, 100):

        message = f"Update_{request}"

        print(f"Publishing {topic} {message}")

        socket.send_string(f"{topic} {message}")

        time.sleep(1)


if __name__ == "__main__":
    publisher()
