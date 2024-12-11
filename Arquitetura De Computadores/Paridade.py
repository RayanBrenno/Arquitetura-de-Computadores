def paridade(binario):
    vetorNome = [""] * len(binario)
    vetorValor = list(binario)
    expoente = 0
    
    for x in range(len(binario)):
        if (x+1) % (2 ** expoente) == 0:
            vetorNome[x] = "Paridade"
            expoente += 1

        else:
            vetorNome[x] = "Dado"
            
    print(vetorNome)
            
    expoente = 0
    contParidade = 1

    for x in range(len(vetorValor)) :

        if vetorNome[x] == "Paridade":
            aux1 = x
            soma = 0
            intervalo = 2**expoente

            while aux1 <= len(vetorValor):
                aux2 = 0

                if aux1 == x:
                    aux2 += 1

                while aux2 < intervalo:
                    if (aux1 + aux2) >= len(vetorValor):
                        break
                    soma += int(vetorValor[aux1+aux2])
                    aux2 += 1
                
                aux1 += intervalo + aux2

            expoente += 1

            if soma % 2 == int(vetorValor[x]):
                print(f"A pariade de numero P{contParidade} está certo")
                
            else:
                print(f"A pariade de numero P{contParidade} está errado")

            contParidade += 1
            
binario = "011110011111"
paridade(binario)