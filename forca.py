import forcafrutas
import forcanomes


def choice():
    print("###############################")
    print("#######Jogando forca!!!########")
    print("###############################")

    print("(1) Modo Frutas", "(2) Modo Nomes")

    modo = int(input("Qual Modo você quer jogar? "))

    if modo == 1:
        print("Forca modo Frutas...")
        forcafrutas.jogar()
    elif modo == 2:
        print("Forca modo Nomes...")
        forcanomes.jogar()


if __name__ == "__main__":
    choice()
