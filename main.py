import pickle

from pokemon import *
from pessoa import *


def escolher_pokemon_inicial(player):


    pikachu = PokemonEletrico("Pikachu", level=1)
    charmander = PokemonFogo("Charmander", level=1)
    squirtle = PokemonFogo("Squirtle", level=1)

    print("Você possui 3 escolhas: ")
    print("1 -", pikachu)
    print("2 -", charmander)
    print("3 -", squirtle)

    while True:
        escolha = input("Escola seu Pokemon")

        if escolha == "1":
            player.capturar(pikachu)
            break
        elif escolha == "2":
            player.capturar(charmander)
            break
        elif escolha == "3":
            player.capturar(squirtle)
            break
        else:
            print("Escolha inválida")

def salvar_jogo(player):
    try:
        with open("database.db", "wb") as arquivo:
            pickle.dump(player, arquivo)
            print("Jogo salvo com sucesso!")
    except Exception as error:
        print ("Erro ao salvar o jogo")
        print(error)

def carregar_jogo():
    try:
        with open("database.db", "rb") as arquivo:
            player = pickle.load(arquivo)
            print("Loading feito com sucesso")
            return player
            print("Jogo salvo com sucesso!")
    except Exception as error:
        print("Save não encontrado")


if __name__ == "__main__":
    print("---------------------------------------------------------------")
    print("Bem vindo ao game Pokemon RPG de terminal :D")
    print("---------------------------------------------------------------")

    player = carregar_jogo()

    if not player:
        nome = input("Olá, qual é seu nome: ")
        player = Player(nome)

        print("Olá {}, esse é um mundo habitado por pokemons a partir de agora sua missão é se tornar um mestre dos Pokemons".format(player))
        print("Capture o máximo de pokemons que conseguir!!")
        player.mostrar_dinheiro()

        if player.pokemons:
            print("Já vi que você ja tem alguns pokemons")
            player.mostrar_pokemon()
        else:
            print("Você não tem nenhum pokemons portanto precisa escolher um")
            escolher_pokemon_inicial(player)

        print("Agora que você possui um pokemon, enfrente seu primeiro inimigo ")
        inimigo1 = Inimigo(nome="Gary", pokemons=[PokemonEletrico("Pikachu", level=1)])
        player.batalhar(inimigo1)
        salvar_jogo(player)

    while True:
        print("---------------- -----------------------------------------------")
        print("O que deseja fazer?")
        print("1 - Explorar o mundo")
        print("2 - Lutar com um inimigo")
        print("3 - Mostrar Pokemons")
        print("4 - Abrir banco")
        print("0 - sair do jogo")
        escolha = input("Sua escolha: ")

        if escolha == "0":
            print("Fechando o jogo")
            break
        elif escolha == "1":
            player.explorar()
            salvar_jogo(player)
        elif escolha == "2":
            inimigo_aleatorio = Inimigo()
            player.batalhar(inimigo_aleatorio)
            salvar_jogo(player)
        elif escolha == "3":
            player.mostrar_pokemon()
        elif escolha == "4":
            player.mostrar_dinheiro()
        else:
            print("Escolha invalida")
        
