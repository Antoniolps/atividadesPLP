"""1 - Ler um vetor de 8 posições e, em seguida,
    ler dois valores X e Y quaisquer corresponde a 
    duas posições no vetor. O programa então imprime a soma
    dos valores encontrados nas respectivas posições X e Y"""
def soma_Vetor():
    # Declara um vetor de 8 posições
    vetor = [0] * 8
    # Percorre o vetor atribuindo um valor digitado pelo o usuario em cada posição
    for i in range(8):
        vetor[i] = int(input("Digite um valor para a posição {}: ".format(i)))
    # Pede um valor para x e y 
    x = int(input("Digite um valor para a posição X: "))
    y = int(input("Digite um valor para a posição Y: "))
    # Faz a soma dos valores nas posições digitadas pelo usuario 
    soma = vetor[x] + vetor[y]
    # Printas os valores que estão nas posições x, y e a soma dos mesmos
    print("A soma de {} + {} = {}".format(vetor[x], vetor[y], soma))

"""
    2 - Faça um programa em python que receba do usuario
    um vetor com 10 posições. Em seguida devera ser 
    impresso o maior e o menor elemento do valor
    """    

def maior_Menor():
    # Declara um vetor de 10 posições
    vetor = [0] * 10
    # Percorre o vetor atribuindo um valor digitado pelo o usuario em cada posição
    for i in range(10):
        vetor[i] = int(input("Digite um valor para a posição {}: ".format(i)))
    # Declara menor e maior com a primeira posição do vetor
    menor = vetor[0]
    maior = vetor[0]
    # Percorre o vetor 
    for i in range(10):
        # Verifica se o valor na posição i é menor que o valor que está em menor
        if vetor[i] < menor:
            # Se menor atribui o valor atual como menor
            menor = vetor[i]
        # Verifica se o valor na posição i é maior que o valor que está em maior
        if vetor[i] > maior:
            # Se maior atribui o valor atual como maior
            maior = vetor[i]

    # Imprime o menor e o maior
    print("O menor valor é {} e o maior é {}".format(menor, maior))

if __name__ == "__main__":
    #soma_Vetor()
    maior_Menor()