class TelaSistema():

    def tela_opcoes(self):
        print("Batalha Naval")
        print("1 - Gerenciar Jogadores")
        print("0 - Fechar Jogo")
        opcao = int(input("Escolha sua opção:"))
        return opcao
    
    def mensagem(self, texto: str):
        return print(texto)