# Escreva um código que dado dois valores binários de tamanho fixo, seus sinais (0 – positivo; 1 – negativo) e um valor de um bit de operação (0 – subtração; 1 – soma), realize a operação aritmética entre os valores e retorne seu resultado.
from Exercicio3 import *


def subtracao(binario1, binario2):

    binario2 = complementoDois(binario2)

    return soma(binario1, binario2)


def exercicio4():

    operacao = input("Qual operação deseja realizar? \n"
                     "0 - Subtração (B1-B2)\n"
                     "1 - Adição (B1+B2)\n"
                     "")

    binario1 = input(
        "Digite o primerio binario para realizar a operação (Max 8 Bits) - ")
    sinal1 = input("Qual sinal do binario digitado? \n"
                   "0 - Positivo\n"
                   "1 - Negativo\n"
                   "")

    binario2 = input(
        "Digite o segundo binario para realizar a operação (Max 8 Bits) - ")
    sinal2 = input("Qual sinal do binario digitado? \n"
                   "0 - Positivo\n"
                   "1 - Negativo\n"
                   "")

    if len(binario1) < 8 or len(binario2) < 8:
        binario1 = "0" * (8 - len(binario1)) + binario1
        binario2 = "0" * (8 - len(binario2)) + binario2

    if sinal1 == "1":
        binario1 = complementoDois(binario1)

    if sinal2 == "1" and operacao == "0":
        operacao = "1"

    elif sinal2 == "1":
        binario2 = complementoDois(binario2)

    if operacao == "0":
        resultado = subtracao(binario1, binario2)
    else:
        resultado = soma(binario1, binario2)

    vetor = []

    for x in resultado:
        vetor.append(x)

    return vetor


if __name__ == "__main__":
    print(exercicio4())
