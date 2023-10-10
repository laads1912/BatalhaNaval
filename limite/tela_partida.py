class TelaPartida:

    def tela_opcoes(self):
        print("----- JOGADORES -----")
        print("1 - Iniciar Partida")
        print("0 - Retornar")

        opcao = input("Escolha a opção: ")
        return opcao

    def iniciar_partida(self):
        print("-------- INICIAR PARTIDA ----------")
        nome = input("Nome do jogador: ")
        tamanho_oceano = input("Tamanho do oceano: ")
        return {"nome": nome, "tamanho_oceano": tamanho_oceano}

    def posicionar_barcos(self, barco):
        if barco == "Bote":
            posicao = input("Escolha a posição do bote (Apenas 1 espaço. Exemplo: 'A2'): ")
        elif barco == "Submarino":
            posicao = input("Escolha a posição do submarino (2 espaços. Exemplo: 'B3 B4'): ")
        elif barco == "Fragata":
            posicao = input("Escolha a posição da fragata (3 espaços. Exemplo: 'C6 D6 E6'): ")
        else:
            posicao = input("Escolha a posição do porta aviões (4 espaços. Exemplo: 'D1 D2 D3 D4'): ")
        return posicao

    def atirar(self):
        posicao = input("-------- INSIRA A POSIÇÃO DO TIRO ----------")

    def mostrar_mensagem(self, mensagem):
        print(mensagem)
