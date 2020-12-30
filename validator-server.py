import socket

HOST = '127.0.0.1'  
PORT = 65432     

def cpfValidator(data):
    
    if(len(data)!=11):
        return False
    else:
        soma = 0
        b = 1
        num = list(data)

        num.pop(9)
        num.pop(9)

        for j in num:
            mult = 11 - b
            soma = soma + int(j) * mult
            b+=1

        ult = soma%11

        if(ult < 2):
            num.append('0')
        else:
            ult = (11 - ult)
            num.append(str(ult))

        soma = 0
        b = 1

        for j in num:
            mult = 12 - b
            soma = soma + int(j) * mult
            b+=1

        ult = soma%11

        if(ult < 2):
            num.append('0')
        else:
            ult = (11 - ult)
            num.append(str(ult))    

        i = 0
        palavra = ''
        while (i < 11):
            palavra+=num[i]
            i+=1

        if(palavra == data):
            return True
        else: 
            return False

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
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