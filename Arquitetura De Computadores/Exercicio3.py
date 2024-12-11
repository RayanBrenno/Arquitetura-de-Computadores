# Escreva um código que dado um valor binário retorne seu valor negativo através do método de complemento de dois. Caso a saída exceda o tamanho da palavra, deverá ser emitido um erro DATA OVERFLOW
from Exercicio2 import complementoUm


def soma(binario1, binario2):

    binario1 = binario1[::-1]
    binario2 = binario2[::-1]
    resultado = ""
    c = 0

    for a, b in zip(binario1, binario2):
        sum = int(a) ^ int(b) ^ c
        c = int(a) and int(b) or ((int(a) ^ int(b)) and c)
        resultado = str(sum) + resultado

    if c == 1:
        print("OBS: Ocorreu um Overflow na soma")

    return resultado


def complementoDois(binario):

    binComp1 = complementoUm(binario)
    binSoma = "00000001"
    binComp2 = soma(binComp1, binSoma)

    vetor = []

    for x in binComp2:
        vetor.append(x)

    if binComp2[0] != binComp1[0]:
        return "O numero execedou o tamanho permitido = OVERFLOW"
    else:
        return vetor


if __name__ == "__main__":
    binario = "110"
    print(f"Complemento de dois -> {complementoDois(binario)}")
