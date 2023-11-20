class TelaJogador:
    def tela_opcoes(self):
        print("----- JOGADORES -----")
        print("1 - Cadastrar jogador")
        print("2 - Mostrar ranking dos jogadores")
        print("3 - Excluir jogador")
        print("4 - Alterar cadastro")
        print("5 - Mostrar histórico de partidas")
        print("0 - Retornar")

        opcao = input("Escolha a opção: ")
        return opcao

    def pegar_dados_jogador(self):
        print("-------- DADOS JOGADOR ----------")
        nome = input("Nome: ")
        senha = input("Senha: ")
        data_nascimento = input("Data de nascimento: ")
        return {"nome": nome, "senha": senha, "data_nascimento": data_nascimento}

    def selecionar_jogador(self):
        nome = input("Nome do jogador que deseja selecionar: ")
        senha = input("Senha: ")
        return {"nome": nome, "senha": senha}

    def mostrar_jogador(self, dados_jogador):
        print("NOME: " + dados_jogador["nome"])
        print("DATA DE NASCIMENTO: " + dados_jogador["data_nascimento"])

    def opcoes_alterar_cadastro(self):
        print("----- OPÇÕES -----")
        print("1 - Nome")
        print("2 - Senha")
        print("3 - Data de nascimento")
        print("0 - Retornar")

        opcao = input("Escolha a opção que deseja alterar: ")
        return opcao

    def alterar_nome(self):
        nome = input("Novo nome: ")
        return nome

    def alterar_senha(self):
        senha = input("Nova senha: ")
        return senha

    def alterar_data_nascimento(self):
        data_nascimento = input("Nova data de nascimento: ")
        return data_nascimento

    def mostrar_mensagem(self, mensagem):
        print(mensagem)

    def mostrar_jogadas(self, jogadas):
        print("Jogadas: ")
        print(*jogadas)
