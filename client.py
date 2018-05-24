import sys
from socket import AF_INET, SOCK_STREAM, socket

def usage():
    print("python client.py host port")

def quit():
    socket.send("quit".encode())
    exit(0)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        usage()
        exit(0)
    else:
        address = (sys.argv[1], int(sys.argv[2]))

    socket = socket(AF_INET, SOCK_STREAM)
    cmd = ""
    try:
        socket.connect(address)
        while (cmd != "/quit"):
            cmd = input()
            argv = cmd.split(' ',1)
            if len(argv) == 1:
                if argv[0] == "/quit":
                    quit()
            else:
                if argv[0] == "/send":
                    socket.send(argv[1].encode())
    except ConnectionRefusedError:
        print("try different address")
    finally:
        socket.close()
