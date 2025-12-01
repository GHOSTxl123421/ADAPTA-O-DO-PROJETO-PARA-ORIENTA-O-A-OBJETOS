import random
from inimigos import Goblin, Orc, Troll

def gerar_inimigo():
    escolha = random.choice([Goblin, Orc, Troll])
    return escolha()

def batalha(jogador, inimigo):
    print(f"\nUm {inimigo.nome} apareceu!")

    while jogador.esta_vivo() and inimigo.esta_vivo():
        dano_jog = jogador.atacar(inimigo)
        print(f"Você causou {dano_jog} de dano. Vida do inimigo: {inimigo.vida}")

        if inimigo.esta_vivo():
            dano_ini = inimigo.atacar(jogador)
            print(f"O {inimigo.nome} causou {dano_ini} de dano. Sua vida: {jogador.vida}")

    if jogador.esta_vivo():
        print("\nVocê venceu a batalha!")
        jogador.inventario.append("poção")
    else:
        print("\nVocê foi derrotado...")