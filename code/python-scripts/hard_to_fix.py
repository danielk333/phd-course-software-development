import string
import random
import socket
import struct
import argparse


HOST = "localhost"
PORT = 8083
random.seed(2)

msgs = [
    "".join(
        random.choices(
            string.ascii_uppercase + string.digits,
            k=random.randint(1, 257),
        )
    )
    for ind in range(500)
]


def run_server():
    msg_index = 0
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s_sock:
        s_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s_sock.bind((HOST, PORT))
        s_sock.listen(1)
        server_running = True
        while server_running:
            conn, addr = s_sock.accept()
            with conn:
                while True:
                    msg_len_b_first = conn.recv(1)
                    if len(msg_len_b_first) == 0:
                        continue
                    msg_len_first = struct.unpack(">B", msg_len_b_first)[0]
                    if msg_len_first == 0:
                        server_running = False
                        conn.send(struct.pack("2s", "OK".encode("UTF8")))
                        break
                    elif msg_len_first == 255:
                        msg_len_b = conn.recv(2)
                        msg_len = struct.unpack(">H", msg_len_b)[0]
                    else:
                        msg_len = msg_len_first
                    data = conn.recv(msg_len)
                    conn.send(struct.pack("2s", "OK".encode("UTF8")))
                    msg = struct.unpack(f"{msg_len}s", data)[0].decode("UTF8")
                    assert msg == msgs[msg_index]
                    msg_index += 1
                    print("Server: ", msg)
                    break
    print("Server exiting...")


def run_client(msg):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        if len(msg) <= 255:
            data = struct.pack(f">B{len(msg)}s", len(msg), msg.encode("UTF8"))
        else:
            sock.send(struct.pack(">B", 255))
            data = struct.pack(f"<H{len(msg)}s", len(msg), msg.encode("UTF8"))
        sock.send(data)
        data = sock.recv(16)
        print("Client: ", struct.unpack("2s", data)[0].decode("UTF8"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parsers = parser.add_subparsers(dest="cmd")
    server_parser = parsers.add_parser("server")
    client_parser = parsers.add_parser("client")

    args = parser.parse_args()

    match args.cmd:
        case "server":
            try:
                run_server()
            except KeyboardInterrupt:
                print("exit server")
        case "client":
            for msg in msgs:
                run_client(msg)
            run_client("")
