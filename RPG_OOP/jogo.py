import random
from jogador import Jogador
from mapa import Mapa
from batalha import batalha, gerar_inimigo

class Jogo:
    def __init__(self, tamanho=5):
        self.mapa = Mapa(tamanho)
        self.jogador = Jogador("Herói")
        self.pos = (0, 0)

    def iniciar(self):
        print("=== RPG ORIENTADO A OBJETOS ===\n")

        while self.jogador.esta_vivo():
            self.mapa.exibir(self.pos)
            print(f"Vida: {self.jogador.vida} | Inventário: {self.jogador.inventario}")

            comando = input("Mover (w/a/s/d), usar poção (u) ou sair (q): ").lower()

            if comando == "q":
                print("Saindo do jogo...")
                break

            if comando == "u":
                if self.jogador.usar_pocao():
                    print("Você usou uma poção e recuperou vida!")
                else:
                    print("Você não tem poções!")
                continue

            if comando in ["w", "a", "s", "d"]:
                self.pos = self.jogador.mover(self.pos, comando, self.mapa.tamanho)

                # chance de batalha
                if random.random() < 0.35:
                    inimigo = gerar_inimigo()
                    batalha(self.jogador, inimigo)

        print("\nFim de jogo!")


if __name__ == "__main__":
    jogo = Jogo()
    jogo.iniciar()
