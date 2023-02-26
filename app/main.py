# Uncomment this to pass the first stage
import socket


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    conn, addr = server_socket.accept() # wait for client

    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.send("+PONG\r\n".encode())

if __name__ == "__main__":
    main()
