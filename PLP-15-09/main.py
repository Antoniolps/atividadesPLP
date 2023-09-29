#Faça um programa em python que receba 6 numeros inteiros e mostre:
#   Os numeros pares digitados;
#   A soma dos numeros pares digitados;
#   Os numeros impares digitados;
#   A quantidade de numeros impares digitados;

def numeros():
    #Declaração de variaveis 
    numeros = []
    numeros_pares = []
    numeros_impares = []
    soma_pares = 0
    
    # Lendo os numeros do usuario 
    for i in range(6):
        numeros.append(int(input("Digite um numero: ")))

    # Atribuindo pares e impares 
    for numero in numeros:
        if numero % 2 == 0:
            numeros_pares.append(numero)
            soma_pares += numero
        else: 
            numeros_impares.append(numero)

    print("Os numeros pares digitados são: ")
    for numero in numeros_pares: 
        print(numero)

    print("A soma dos numeros pares é ", soma_pares)

    print("Os numeros impares digitados são: ")
    for numero in numeros_impares:
        print(numero)

    print("A quantidade numeros impares é ", len(numeros_impares))

    print("O maior valor digitado foi: ", max(numeros))
    print("O menor valor digitado foi: ", min(numeros))
    
"""
Faça um programa em python para gerar automaticamente
numero entre 0 e 99 e uma cartela de bingo.
sabendo que cada cartela devera conter 5 linhas e 5 numeros
gere estes dados de modo a nao ter numeros repetidos dentro 
das cartelas . O programa deve exibir nas tela a cartela gerada
"""
import random 

def gerar_cartela():
    numeros = set()
    cartela = []
    
    for i in range(5): 
        numero = random.randint(0, 99)
        while numero in numeros: 
            numero = random.randint(0,99)
        numeros.add(numero)
        cartela.append(numero)

    return cartela

def bingo():
    cartela = gerar_cartela()
    print("Cartela: ")
    for linha in cartela:
        print(linha)


if __name__ == "__main__":
    #numeros()
    bingo()