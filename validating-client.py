import socket

HOST = '127.0.0.1'  
PORT = 65432        

while True:
    print("Digite o CPF para ser validado: ")
    cpf = input()    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        cpf = cpf.encode()
        s.sendall(cpf)
        data = s.recv(1024)
        

    print('Received:', repr(data.decode()))