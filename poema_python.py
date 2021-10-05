resposta = "sim"

while resposta == "sim":

    cor = input("Escolha uma cor no plural: ")
    cor = cor.lower()

    objeto = input("Escolha um objeto no plural: ")
    objeto = objeto.capitalize()

    nome = input("Escolha um nome: ")
    nome = nome.capitalize()

    print("Rosas são " + cor + ";")

    print(objeto + " são azuis;")

    print("Eu amo " + nome + "!")

    print("Você deseja continuar?")
    resposta = input()

    if resposta == "sim":

        continue

    else:

        print("Obrigado por jogar!")
        break