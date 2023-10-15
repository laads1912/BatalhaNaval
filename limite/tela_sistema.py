class TelaSistema:

    def tela_opcoes(self):
        print("----- BATALHA NAVAL -----")
        print("1 - Iniciar partida")
        print("2 - Gerenciar Jogadores")
        print("0 - Fechar Jogo")
        opcao = input("Escolha sua opção: ")
        return opcao
    
    def mostrar_mensagem(self, texto: str):
        return print(texto)
