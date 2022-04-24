import random
def jogar():

    print("###########################")
    print("Bem vindo ao jogo de Forca!")
    print("######Modo de frutas#######")
    print("###########################")
    arquivo = open("frutas.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()


    numero = random.randrange(0,len(palavras))

    palavra_secreta = palavras[numero].upper()


    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0
    print(letras_acertadas)
    #enquanto (True and True)
    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()


        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                    print("Você acertou a letra!!")
                index += 1

        else:
            erros += 1
            print("Você errou :(, logo restam {} erros!!".format(6 - erros ))
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    if acertou:
        print("você ganhou!!!!")
    else:
        print("Você perdeu. Tente novamente!")
    print("fim do jogo!!","a palavra secreta era:", palavra_secreta)

if(__name__ == "__main__"):
    jogar()
