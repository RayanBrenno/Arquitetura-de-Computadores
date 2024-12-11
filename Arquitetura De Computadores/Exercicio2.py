#Escreva um código que dado um valor binário retorne seu valor negativo através do método de complemento de um.
def complementoUm(binario):
    
    if len(binario) < 8:
        binario = "0" * (8 - len(binario)) + binario
             
    binComp=""
    for n in binario:
        if n=="0":
            binComp = binComp+"1"
        else: binComp = binComp+"0"
    
    if len(binComp) >8:
        return "O numero execedou o tamanho permitido = OVERFLOW"
    
    vetor = []

    for x in binComp :
        vetor.append(x)

    return vetor

if __name__ == "__main__":
    binario = "110"
    print(f"Complemento de um -> {complementoUm(binario)}")