lines = open('Arquitetura De Computadores/Exercicio5.txt').readlines()

transformações = {
    "ILOAD": "0x15 0x0",
    "BIPUSH": "0x10 0x0",
    "IADD": "0x60",
    "IF_ICMPEQ": "0x9F 0x00 0x0D",
    "ISUB": "0x64",
    "ISTORE": "0x36 0x0",
    "GOTO": "0xA7 0x00 0x07"
}

qtdNaPilha = 0
qtdNoStore = 0
fraseFinal = ""

for i in lines:
    j = i.split('\n')
    j = j[0].split(' ')
    for x in j:
        if x in transformações.keys():
            add = transformações.get(x)
            if x == 'ILOAD' or x == 'BIPUSH':
                qtdNaPilha += 1
                fraseFinal += f'{add}{qtdNaPilha}\n'
                continue

            elif x == 'ISTORE':
                qtdNoStore += 1
                qtdNaPilha = 0
                fraseFinal += f'{add}{qtdNoStore}\n'
                continue

            elif x == 'IADD' or x == 'ISUB':
                qtdNaPilha -= 1
            elif x == 'IF_ICMPEQ':
                qtdNaPilha = 0

            fraseFinal += f'{add}\n'

tex_final = open('Arquitetura De Computadores/Exercicio5Resposta.txt', 'w')
tex_final.write(fraseFinal)
tex_final.close()

