import random

class Pokemon:

    def __init__(self, especie, level=None, nome=None):
        self.especie = especie

        if level:
            self.level = level
        else:
            self.level = random.randint(1, 100)


        if nome:
            self.nome = nome
        else:
            self.nome = especie


        self.ataque = self.level * 5
        self.vida = self.level * 10


    def __str__(self):
        return "{} ({})".format(self.nome, self.level)

    def atacar(self, pokemon):
        ataque_efetivo = int((self.ataque * random.random() * 1.3))
        pokemon.vida -= ataque_efetivo

        if ataque_efetivo >= self.ataque:
            print("{} FOI ATINGIDO PELO ESPECIAL DE {} E PERDEU {} DE VIDA!!".format(pokemon, self, ataque_efetivo))
        else:
            print("{} perdeu {} de vida".format(pokemon, ataque_efetivo))

        if pokemon.vida <= 0:
            print("{} foi derrotado".format(pokemon))
            return True
        else:
            return False


class PokemonEletrico(Pokemon):
    tipo = "eletrico"

    def atacar(self, pokemon):
        print("{} lançou um raio do trovão em {}".format(self, pokemon))
        print("------------------------------------------------")
        return super().atacar(pokemon)

class PokemonFogo(Pokemon):
    tipo = "Fogo"

    def atacar(self, pokemon):
        print("{} lançou uma bola de fogo na cabesssss de {}".format(self, pokemon))
        print("------------------------------------------------")
        return super().atacar(pokemon)


class PokemonAgua(Pokemon):
    tipo = "Água"

    def atacar(self, pokemon):
        print("{} lançou um jato da agua em {}".format(self, pokemon))
        print("------------------------------------------------")
        return super().atacar(pokemon)


    


