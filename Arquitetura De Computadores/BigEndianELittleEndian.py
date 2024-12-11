import math

def bigEndian(texto_usuario):
    
    x = math.floor(len(texto_usuario)/4) + 4
    array_multidimensional = [['' for j in range(4)] for i in range(x)]
    caracteres = list(texto_usuario)
    aux = 0

    for linha in range(x):

        if aux == len(caracteres):
            break    

        if caracteres[aux+1].isnumeric():
            coluna = 3
            aux += 1
            colocar = ""
            while True:
                colocar += caracteres[aux]
                aux += 1
                if aux >= len(caracteres) or caracteres[aux] == " ":
                    break
            array_multidimensional[linha][coluna] = colocar 
            coluna -= 1 
            while coluna >=0:
                array_multidimensional[linha][coluna] = "0" 
                coluna -= 1 

        else:
            coluna = 0
            while coluna <=3:
                if caracteres[aux] == " " and caracteres[aux+1].isdigit():
                    while coluna <= 3:
                        array_multidimensional[linha][coluna] = "0"
                        coluna += 1
                    break 
                array_multidimensional[linha][coluna] = caracteres[aux]
                aux += 1
                coluna += 1

        print(array_multidimensional[linha])

def littleEndian(texto_usuario):
    
    x = math.floor(len(texto_usuario)/4) + 4
    array_multidimensional = [['' for j in range(4)] for i in range(x)]
    caracteres = list(texto_usuario)
    aux = 0

    for linha in range(x):

        if aux == len(caracteres):
            break    

        if caracteres[aux+1].isnumeric():
            coluna = 3
            aux += 1
            colocar = ""
            while True:
                colocar += caracteres[aux]
                aux += 1
                if aux >= len(caracteres) or caracteres[aux] == " ":
                    break   
            array_multidimensional[linha][coluna] = colocar 
            coluna -= 1      
            while coluna >=0:
                array_multidimensional[linha][coluna] = "0" 
                coluna -= 1 

        else:
            coluna = 3
            while coluna >= 0:
                if caracteres[aux] == " " and caracteres[aux+1].isdigit():
                    while coluna >= 0:
                        array_multidimensional[linha][coluna] = "0"
                        coluna -= 1
                    break 
                array_multidimensional[linha][coluna] = caracteres[aux]
                aux += 1
                coluna -= 1

        print(array_multidimensional[linha])

texto_usuario = "Rayan Brenno 12345 2711 200"
bigEndian(texto_usuario)
print("")
littleEndian(texto_usuario)