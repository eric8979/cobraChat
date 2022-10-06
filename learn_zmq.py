# Learning Note

# 0. About ZMQ
# ZeroMQ message is length-specified binary data
# ZMQ is basically Transport layer protocols on steroids.

# 1. CONTEXT
# Always start by creating "context"
# Create and use exactly one context in your process
# "context" : container for all sockets in a single process,

# 2. The ZMQ Way
# Create Socket -> Config Socket(type) -> bind/connect socket to network -> Send/Receive messages

# bind()
# addr format -> protocol://interface:port

# accept() is automatic in ZMQ.

# send(), recv()

# 3. Messaging Patterns
#   req-rep
#   pub-sub
#   pipeline
#   Exclusive

# Valid Pair
    # PUB and SUB
    # REQ and REP
    # REQ and ROUTER (take care, REQ inserts an extra null frame)
    # DEALER and REP (take care, REP assumes a null frame)
    # DEALER and ROUTER
    # DEALER and DEALER
    # ROUTER and ROUTER
    # PUSH and PULL
    # PAIR and PAIR

# Handling Multiple Sockets - poll()
import zmq
context = zmq.Context()
receiver = context.socket(zmq.PULL)
receiver.connect("tcp://localhost:5557")

subscriber = context.socket(zmq.SUB)
subscriber.connect("tcp://localhost:5556")
poller = zmq.Poller()
poller.register(receiver, zmq.POLLIN)
poller.register(subscriber, zmq.POLLIN)

while True:
    try:
        socks = dict(poller.poll())
    except KeyboardInterrupt:
        break

    if receiver in socks:
        message = receiver.recv()
        # process task

    if subscriber in socks:
        message = subscriber.recv()


# How do pieces know about each other?
# That's when "Pub-Sub" (with a proxy(XSUB, XPUB)) comes in.






# One socket can have multiple outgoing/ingoing connections.

# ZMQ doesn't know anything about the data you send except its size in bytes.
# Need formatting data before sending

# problem -> check the version(it could be fixed in a later version)
# How to check ver.
# import zmq
#
# print(f"Current libzmq version is {zmq.zmq_version()}")
# print(f"Current  pyzmq version is {zmq.__version__}")

