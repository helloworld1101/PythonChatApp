from socket import AF_INET, SOCK_STREAM, socket

socket = socket(AF_INET, SOCK_STREAM)
socket.bind(('localhost', 10000))
socket.listen(1)

def client_thread(conn, addr):
    print("hello " + str(addr[1]))
    while True:
        message = conn.recv(16).decode()
        if(message):
            print(str(addr[1]) + ": " + message)
        else:
            break

while True:
    conn, addr = socket.accept()
    client_thread(conn, addr)
    conn.close()
    socket.close()
    #exit(0)