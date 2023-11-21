# class TelaJogador:
#     def tela_opcoes(self):
#         print("----- JOGADORES -----")
#         print("1 - Cadastrar jogador")
#         print("2 - Mostrar ranking dos jogadores")
#         print("3 - Excluir jogador")
#         print("4 - Alterar cadastro")
#         print("5 - Mostrar histórico de partidas")
#         print("0 - Retornar")
#
#         opcao = input("Escolha a opção: ")
#         return opcao
#
#     def pegar_dados_jogador(self):
#         print("-------- DADOS JOGADOR ----------")
#         nome = input("Nome: ")
#         senha = input("Senha: ")
#         data_nascimento = input("Data de nascimento: ")
#         return {"nome": nome, "senha": senha, "data_nascimento": data_nascimento}
#
#     def selecionar_jogador(self):
#         nome = input("Nome do jogador que deseja selecionar: ")
#         senha = input("Senha: ")
#         return {"nome": nome, "senha": senha}
#
#     def mostrar_jogador(self, dados_jogador):
#         print("NOME: " + dados_jogador["nome"])
#         print("DATA DE NASCIMENTO: " + dados_jogador["data_nascimento"])
#
#     def opcoes_alterar_cadastro(self):
#         print("----- OPÇÕES -----")
#         print("1 - Nome")
#         print("2 - Senha")
#         print("3 - Data de nascimento")
#         print("0 - Retornar")
#
#         opcao = input("Escolha a opção que deseja alterar: ")
#         return opcao
#
#     def alterar_nome(self):
#         nome = input("Novo nome: ")
#         return nome
#
#     def alterar_senha(self):
#         senha = input("Nova senha: ")
#         return senha
#
#     def alterar_data_nascimento(self):
#         data_nascimento = input("Nova data de nascimento: ")
#         return data_nascimento
#
#     def mostrar_mensagem(self, mensagem):
#         print(mensagem)
#
#     def mostrar_jogadas(self, jogadas):
#         print("Jogadas: ")
#         print(*jogadas)

import PySimpleGUI as sg

class TelaJogador:
    def __init__(self):
        sg.theme('DarkGrey5')

    def tela_opcoes(self):
        layout = [
            [sg.Text('----- JOGADORES -----', font=('Arial', 16), justification='center')],
            [sg.Button('Cadastrar jogador', size=(25, 2))],
            [sg.Button('Mostrar ranking dos jogadores', size=(25, 2))],
            [sg.Button('Excluir jogador', size=(25, 2))],
            [sg.Button('Alterar cadastro', size=(25, 2))],
            [sg.Button('Mostrar histórico de partidas', size=(25, 2))],
            [sg.Button('Retornar', size=(25, 2))]
        ]

        window = sg.Window('Opções de Jogadores', layout, element_justification='center')

        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED:
                window.close()
                return None

            elif event == 'Cadastrar jogador':
                window.close()
                return 1

            elif event == 'Mostrar ranking dos jogadores':
                window.close()
                return 2

            elif event == 'Excluir jogador':
                window.close()
                return 3

            elif event == 'Alterar cadastro':
                window.close()
                return 4

            elif event == 'Mostrar histórico de partidas':
                window.close()
                return 5

            elif event == 'Retornar':
                window.close()
                return 0
    def pegar_dados_jogador(self):
        layout = [
            [sg.Text('-------- DADOS JOGADOR ----------', font=('Helvetica', 16), justification='center')],
            [sg.Text('Nome:'), sg.InputText(key='nome')],
            [sg.Text('Senha:'), sg.InputText(key='senha', password_char='*')],
            [sg.Text('Data de nascimento:'), sg.InputText(key='data_nascimento')],
            [sg.Button('Cadastrar', size=(10, 2)), sg.Button('Cancelar', size=(10, 2))]
        ]

        window = sg.Window('Dados do Jogador', layout, element_justification='center')

        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED or event == 'Cancelar':
                window.close()
                return None

            elif event == 'Cadastrar':
                window.close()
                return {"nome": values['nome'], "senha": values['senha'], "data_nascimento": values['data_nascimento']}

    def selecionar_jogador(self):
        layout = [
            [sg.Text('Selecionar jogador', font=('Helvetica', 16), justification='center')],
            [sg.Text('Nome do jogador que deseja selecionar:'), sg.InputText(key='nome')],
            [sg.Text('Senha:'), sg.InputText(key='senha', password_char='*')],
            [sg.Button('Selecionar', size=(10, 2)), sg.Button('Cancelar', size=(10, 2))]
        ]

        window = sg.Window('Selecionar Jogador', layout, element_justification='center', size=(400, 150))

        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED or event == 'Cancelar':
                window.close()
                return None

            elif event == 'Selecionar':
                window.close()
                return {"nome": values['nome'], "senha": values['senha']}

    def mostrar_jogador(self, dados_jogador):
        layout = [
            [sg.Text('DADOS DO JOGADOR', font=('Helvetica', 16), justification='center')],
            [sg.Text(f'NOME: {dados_jogador["nome"]}')],
            [sg.Text(f'DATA DE NASCIMENTO: {dados_jogador["data_nascimento"]}')],
            [sg.Button('Fechar', size=(10, 2))]
        ]

        window = sg.Window('Jogador', layout, element_justification='center')

        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED or event == 'Fechar':
                window.close()
                break

    def opcoes_alterar_cadastro(self):
        layout = [
            [sg.Text('----- OPÇÕES -----', font=('Helvetica', 16), justification='center')],
            [sg.Button('Nome', size=(20, 2))],
            [sg.Button('Senha', size=(20, 2))],
            [sg.Button('Data de nascimento', size=(20, 2))],
            [sg.Button('Retornar', size=(20, 2))]
        ]

        window = sg.Window('Opções de Alteração de Cadastro', layout, element_justification='center')

        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED or event == 'Retornar':
                window.close()
                return None

            return event

    def alterar_nome(self):
        layout = [
            [sg.Text('Alterar Nome', font=('Helvetica', 16), justification='center')],
            [sg.Text('Novo nome:'), sg.InputText(key='nome')],
            [sg.Button('Confirmar', size=(10, 2)), sg.Button('Cancelar', size=(10, 2))]
        ]

        window = sg.Window('Alterar Nome', layout, element_justification='center')

        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED or event == 'Cancelar':
                window.close()
                return None

            elif event == 'Confirmar':
                window.close()
                return values['nome']

    def alterar_senha(self):
        layout = [
            [sg.Text('Alterar Senha', font=('Helvetica', 16), justification='center')],
            [sg.Text('Nova senha:'), sg.InputText(key='senha', password_char='*')],
            [sg.Button('Confirmar', size=(10, 2)), sg.Button('Cancelar', size=(10, 2))]
        ]

        window = sg.Window('Alterar Senha', layout, element_justification='center')

        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED or event == 'Cancelar':
                window.close()
                return None

            elif event == 'Confirmar':
                window.close()
                return values['senha']

    def alterar_data_nascimento(self):
        layout = [
            [sg.Text('Alterar Data de Nascimento', font=('Helvetica', 16), justification='center')],
            [sg.Text('Nova data de nascimento:'), sg.InputText(key='data_nascimento')],
            [sg.Button('Confirmar', size=(10, 2)), sg.Button('Cancelar', size=(10, 2))]
        ]

        window = sg.Window('Alterar Data de Nascimento', layout, element_justification='center')

        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED or event == 'Cancelar':
                window.close()
                return None

            elif event == 'Confirmar':
                window.close()
                return values['data_nascimento']

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