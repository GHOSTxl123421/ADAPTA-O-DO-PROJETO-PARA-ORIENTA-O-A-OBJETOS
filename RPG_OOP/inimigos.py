from personagem import Personagem

class Inimigo(Personagem):
    def __init__(self, nome, vida, ataque, defesa):
        super().__init__(nome, vida, ataque, defesa)


class Goblin(Inimigo):
    def __init__(self):
        super().__init__("Goblin", 40, 10, 3)


class Orc(Inimigo):
    def __init__(self):
        super().__init__("Orc", 60, 15, 5)


class Troll(Inimigo):
    def __init__(self):
        super().__init__("Troll", 90, 20, 8)
