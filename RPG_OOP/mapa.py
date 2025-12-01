class Mapa:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.matriz = [["." for _ in range(tamanho)] for _ in range(tamanho)]

    def exibir(self, pos_jogador):
        for i in range(self.tamanho):
            for j in range(self.tamanho):
                if (i, j) == pos_jogador:
                    print("P", end=" ")
                else:
                    print(self.matriz[i][j], end=" ")
            print()
        print()