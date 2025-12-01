from personagem import Personagem

class Jogador(Personagem):
    def __init__(self, nome):
        super().__init__(nome, vida=100, ataque=15, defesa=5)
        self.inventario = []

    def mover(self, pos, direcao, tamanho):
        x, y = pos

        if direcao == "w" and x > 0:
            x -= 1
        elif direcao == "s" and x < tamanho - 1:
            x += 1
        elif direcao == "a" and y > 0:
            y -= 1
        elif direcao == "d" and y < tamanho - 1:
            y += 1

        return (x, y)

    def usar_pocao(self):
        if "poção" in self.inventario:
            self._vida += 30
            if self._vida > 100:
                self._vida = 100
            self.inventario.remove("poção")
            return True
        return False
