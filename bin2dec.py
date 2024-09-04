entrada = str(input()) [::-1]
limite = 8
endereco = 0
indexExpoentes = []
calculo = []
soma = 0

#Definindo ordem binaria
for i in range(len(entrada)):
    if int(entrada[i]) == 1 or int(entrada[i]) == 0:
        if len(entrada) > limite:
            print("Max number: 8")
            break
        else:
            if len(entrada) == limite or len(entrada) < limite:
                if int(entrada[i]) == 0:
                    endereco += 1
                elif int(entrada[i]) == 1:
                    indexExpoentes.append(int(endereco))
                    endereco += 1

#Calculo Binario
for i in range(len(indexExpoentes)):
    unidade = 2**indexExpoentes[i]
    calculo.append(unidade)
for i in range(len(calculo)):
    soma = calculo[i] + soma

print(soma)