import socket
HOST = '127.0.0.1'
PORT = 7777 
def start_program():
    client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try: 
        client_socket.connect((HOST,PORT))
        print("Please enter length of array: ")
        data = input() 
        client_socket.send(data.encode())
        response = client_socket.recv(1024).decode()
        print(response)
    except Exception as ex:
        print("Problem while connecting. Please try again/n")
    finally:
        client_socket.close()

if __name__ == "__main__":
    start_program()