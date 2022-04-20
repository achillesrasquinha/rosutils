#!/usr/bin/env python

import ezros

node = ezros.Node("test")

@node.pub("/test", rate = 10, queue_size = 10)
def handle_ping(message):
    message.data = "test"
    return message

@node.on("/ping")
def handle_ping(message):
    node.pub_msg("/pong", "pong")

if __name__ == "__main__":
    node.run()