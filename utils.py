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

def cutter(data):
    data = data.split(';')

    identificador = data[1]
    endereco = data[2]
    porta = data[3]

    return(identificador, endereco, porta)