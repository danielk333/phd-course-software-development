---
title: "Chatroom"
weight: 2
---

## A chat room server and client

In order to improve and develop one must be exposed to many different problems, patterns, situations, and ways to do things. Something that most researchers maybe never encounter are sockets, networks, and real-time applications. It forces you to think differently, apply different patterns, test and develop in new ways. 

As such, the goal of this practical is to write two programs:

1. A server, allowing for clients to connect, and relays all incoming messages from a client to all other clients.
2. A client that can connect to a server, send and receive messages, and display these messages to the user.

This practical has an enormous complexity range: just implementing the sockets locally can be quite simple. Creating a fully fledged terminal [IRC](https://en.wikipedia.org/wiki/IRC) server/client software is nowhere near simple. For this task we will keep to the simple end, and those who want to, they can sprinkle some polish and advanced concepts in there as they please.

### Requirements

The server should:

- Have a command line interface for starting
- Have a way to configure the server (e.g. detailing IP and port)
- Accept connections from clients
- Receive messages from clients
- Relay all messages to all other connected clients
- Store all received messages locally

Optionally it could also:

- Support reacting to commands issued by the clients
- Support client identification upon connection

The client should:

- Have a command line interface for connecting to a target server
- Receive messages from the server and display them
- Send messages to the server

Optionally it could also:

- Provide a fancy Terminal User Interface for message display

### Development

The team should split responsibilities between each member. Plan out then work first, i.e. do a software design, and then get to coding.

- Use git to collaborate
- Design on a high level
- Define interfaces for each other
- Allow the design to change over time
- Implement the code into a single python package 

### Methods 

It is recommended that the  network communication be implemented using [socket](https://docs.python.org/3/library/socket.html). For a minimal example of a server / client pair see [socket examples](https://docs.python.org/3/library/socket.html#example).

Ideally the communication protocol you design should use [struct](https://docs.python.org/3/library/struct.html) to pack and unpack the data. It is possible to also send e.g. [pickle](https://docs.python.org/3/library/pickle.html#module-pickle) data but this is unsafe and might be hard to debug.

A suggestion to get started is:
- Send a fixed length struct with message length.
- Send message.
- Receive the above in that order.

This is a simple way to do binary communication. If you want to you can also implement sending and receiving in chunks (where the last chunk is smaller than the chunk size) and checksums. 

But you can of course do whatever for you communication design if you want to! 

### Tips

#### Server application

It is recommended to use the python built-in [argparse](https://docs.python.org/3/library/argparse.html) package for the CLI.

Also look into [entry points](https://setuptools.pypa.io/en/latest/userguide/entry_point.html) for your package.

#### Client application

There are many options for creating the client application. But a good and built in place to start is [cmd](https://docs.python.org/3/library/cmd.html). Otherwise one can always roll ones own interface with [input](https://docs.python.org/3/library/functions.html#input). 

For the Terminal User Interface inclined who wants a challenge, I would recommend [urwid](https://urwid.org/index.html). Another popular options is [textual](https://github.com/Textualize/textual).

#### Configuration

For configuration there are several options

- All trough the CLI
- [cfg files - configparser](https://docs.python.org/3/library/configparser.html)
- [toml files - tomllib](https://docs.python.org/3/library/tomllib.html)
- [yaml files - pyyaml](https://pyyaml.org/)
- custom format

Probably `cfg` or `toml` files are the best choice here, with a CLI option for a config path that has a default path for looking in the current folder. An advanced but fun option is to store the client configuration in the standard config folder of your OS, e.g. `~/.config/name-of-your-client.config`.

#### OS-agnostic

There are many ways to make code independent of the operating system. E.g. for paths the recommended method is to use [pathlib](https://docs.python.org/3/library/pathlib.html) for all path manipulation.


#### Alternative socket implementations

There are other options out there for socket handling, such as [ZeroMQ](https://zeromq.org/) that has python bindings: [PyZMQ](https://github.com/zeromq/pyzmq). However, this is only recommended if you already are very familiar with sockets, networks or software development. It might be hard to jump into a framework like ZMQ without any pre-existing knowledge.  

## Task

Once the program works, we will all have a chat in class using the software!
