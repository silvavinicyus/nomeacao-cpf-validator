import socket
from utils import cpfValidator

HOST = '127.0.0.1'  
PORT = 65432

HOST_NOMINATOR = '127.0.0.1'
PORT_NOMINATOR = 65431

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
    s.connect((HOST_NOMINATOR, PORT_NOMINATOR))
    data = 'create-name-service;cpfValidator;'+HOST+';'+str(PORT)
    s.sendall(data.encode())
    s.close()

while True:    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:            
        s.bind((HOST, PORT))        
        s.listen()                

        conn, addr = s.accept()
        with conn:                               
            while True:
                data = conn.recv(1024)                
                if not data:                    
                    break
                else:
                    data = data.decode()
                    if(cpfValidator(data)):
                        anwser = 'CPF VALIDO'                        
                        conn.sendall(anwser.encode())
                    else:
                        anwser = 'CPF INVALIDO'                        
                        conn.sendall(anwser.encode())