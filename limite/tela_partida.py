class TelaPartida:

    def iniciar_partida(self):
        print("-------- INICIAR PARTIDA ----------")
        nome = input("Nome do jogador: ")
        senha = input("Senha: ")
        tamanho_oceano = input("Tamanho do oceano: ")
        return {"nome": nome, "tamanho_oceano": tamanho_oceano, "senha": senha}

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
        posicao = input("INSIRA A POSIÇÃO DO TIRO (Exemplo: A1): ")
        return posicao

    def mostrar_legenda_oceano(self, qual_oceano: str):
        print("LEGENDAS " + qual_oceano)
        print("~ = OCEANO   x = TIRO    B = BOTE    S = SUBMARINO   F = FRAGATA     P = PORTA-AVIÕES    O = ACERTO DE "
              "TIRO EM ALGUM NAVIO")

    def mostrar_mensagem(self, mensagem):
        print(mensagem)

    def mostrar_linha(self, char, linha):
        print(char, end=" ")
        print(*linha)

    def mostrar_coordenada(self, contador):
        print(str(contador), end=" ")

    def mostrar_espaco(self):
        print("  ", end="")
