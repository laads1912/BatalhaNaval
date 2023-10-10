class TelaPartida:

    def tela_opcoes(self):
        print("----- JOGADORES -----")
        print("1 - Iniciar Partida")
        print("2 - Mostrar ranking dos jogadores")
        print("3 - Excluir jogador")
        print("0 - Retornar")

        opcao = input("Escolha a opção: ")
        return opcao

    def iniciar_partida(self):
        print("-------- INICIAR PARTIDA ----------")
        nome = input("Nome do jogador: ")
        tamanho_oceano = input("Tamanho do oceano: ")
        return {"nome": nome, "tamanho_oceano": tamanho_oceano}

    def posicionar_barcos(self):
        print("-------- INSIRA A POSIÇÃO DO BOTE ----------")
        posicao = input("Posicao separado por espaço: ")
        return posicao

    def mostrar_jogador(self, dados_jogador):
        print("NOME: ", dados_jogador["nome"])
        print("DATA DE NASCIMENTO: ", dados_jogador["data_nascimento"])

    def mostrar_mensagem(self, mensagem):
        print(mensagem)
