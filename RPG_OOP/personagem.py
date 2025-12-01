class Personagem:
    def __init__(self, nome, vida, ataque, defesa):
        self._nome = nome
        self._vida = vida
        self._ataque = ataque
        self._defesa = defesa

    @property
    def nome(self):
        return self._nome

    @property
    def vida(self):
        return self._vida

    def esta_vivo(self):
        return self._vida > 0

    def receber_dano(self, dano):
        self._vida -= dano
        if self._vida < 0:
            self._vida = 0

    def atacar(self, alvo):
        dano = max(0, self._ataque - alvo._defesa)
        alvo.receber_dano(dano)
        return dano
