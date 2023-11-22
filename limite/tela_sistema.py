# import PySimpleGui as sg

# class TelaSistema:
#
#     def tela_opcoes(self):
#         print("----- BATALHA NAVAL -----")
#         print("1 - Iniciar partida")
#         print("2 - Gerenciar Jogadores")
#         print("0 - Fechar Jogo")
#         opcao = input("Escolha sua opção: ")
#         return opcao
#
#     def mostrar_mensagem(self, texto: str):
#         return print(texto)

import PySimpleGUI as sg


class TelaSistema:

    def __init__(self):
        self.__window = None
        self.init_components()

    def tela_opcoes(self):
        self.init_components()
        event, values = self.__window.read()

        if event == sg.WINDOW_CLOSED or event == 'Fechar Jogo':
            return 0

        elif event == 'Iniciar Partida':
            self.__window.close()
            return 1

        elif event == 'Gerenciar Jogadores':
            self.__window.close()
            return 2

        elif event == 'Partida Teste':
            self.__window.close()
            return 123

    def mostrar_mensagem(self, mensagem):
        layout = [
            [sg.Text(mensagem, font=('Helvetica', 16), justification='center')],
            [sg.Button('OK', size=(10, 2))]
        ]

        window = sg.Window('Mensagem', layout, element_justification='center', size=(300, 75))

        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED or event == 'OK':
                window.close()
                break

    def init_components(self):
        sg.theme('DarkGrey2')
        layout = [
            [sg.Text('----- BATALHA NAVAL -----')],
            [sg.Button('Iniciar Partida', size=(20, 2))],
            [sg.Button('Gerenciar Jogadores', size=(20, 2))],
            [sg.Button('Fechar Jogo', size=(20, 2))],
            [sg.Button('Partida Teste', size=(20, 2))]
        ]
        self.__window = sg.Window('Batalha Naval', layout)
