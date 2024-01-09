'''server handling'''
import socket
import mergesort
import random
# import threading
#import _thread
PORT = 7777
HOST="127.0.0.1"

def generate_arrar(length):
    return [random.randint(0, length) for _ in range(length)]

def handle_client(connection):
    data = generate_arrar(int(connection.recv(1024).decode()))
    answer = mergesort.run_merge(data)
    answer2= mergesort.run_par_merge(data)
    connection.send(f"{answer}\n{answer2}\n".encode())
    connection.close()

def start_server():
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server:
        server.bind((HOST,PORT))
        server.listen()
        while True:
            client_socket, addr = server.accept()
            print('Connected to address: ', addr[0], ':', addr[1])
            #_thread.start_new_thread(handle_client,(client_socket,))

if __name__ == "__main__":
    start_server()