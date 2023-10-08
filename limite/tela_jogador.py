class TelaJogador:
    def tela_opcoes(self):
        print("----- JOGADORES -----")
        print("1 - Cadastrar jogador")
        print("2 - Mostrar ranking dos jogadores")
        print("3 - Excluir jogador")
        print("0 - Retornar")

        opcao = input("Escolha a opção: ")
        return opcao

    def pegar_dados_jogador(self):
        print("-------- DADOS JOGADOR ----------")
        nome = input("Nome: ")
        data_nascimento = input("Data de nascimento: ")
        return {"nome": nome, "data_nascimento": data_nascimento}

    def selecionar_jogador(self):
        nome = input("Nome do jogador que deseja selecionar: ")
        return nome

    def mostrar_jogador(self, dados_jogador):
        print("NOME: ", dados_jogador["nome"])
        print("DATA DE NASCIMENTO: ", dados_jogador["data_nascimento"])

    def mostrar_mensagem(self, mensagem):
        print(mensagem)

