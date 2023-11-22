# class TelaPartida:
#
#     def iniciar_partida(self):
#         print("-------- INICIAR PARTIDA ----------")
#         nome = input("Nome do jogador: ")
#         senha = input("Senha: ")
#         tamanho_oceano = input("Tamanho do oceano (mínimo = 7, máximo = 10): ")
#         return {"nome": nome, "tamanho_oceano": tamanho_oceano, "senha": senha}
#
#     def posicionar_barcos(self, barco):
#         if barco == "Bote":
#             posicao = input("Escolha a posição do bote (Apenas 1 espaço. Exemplo: 'A2'): ")
#         elif barco == "Submarino":
#             posicao = input("Escolha a posição do submarino (2 espaços. Exemplo: 'B3 B4'): ")
#         elif barco == "Fragata":
#             posicao = input("Escolha a posição da fragata (3 espaços. Exemplo: 'C6 D6 E6'): ")
#         else:
#             posicao = input("Escolha a posição do porta aviões (4 espaços. Exemplo: 'D1 D2 D3 D4'): ")
#         return posicao
#
#     def atirar(self):
#         posicao = input("INSIRA A POSIÇÃO DO TIRO (Exemplo: A1): ")
#         return posicao
#
#     def mostrar_legenda_oceano(self):
#         print("LEGENDAS")
#         print("~ = OCEANO   x = TIRO    B = BOTE    S = SUBMARINO   F = FRAGATA     P = PORTA-AVIÕES    O = ACERTO DE "
#               "TIRO EM ALGUM NAVIO")
#
#     def mostrar_mensagem(self, mensagem):
#         print(mensagem)
#
#     def mostrar_linha(self, char, linha):
#         print(char, end=" ")
#         print(*linha)
#
#     def mostrar_coordenada(self, contador):
#         print(str(contador), end=" ")
#
#     def mostrar_espaco(self):
#         print("  ", end="")

import PySimpleGUI as sg

class TelaPartida:
    def __init__(self):
        sg.theme('DarkGrey2')

    def iniciar_partida(self):
        layout = [
            [sg.Text('INICIAR PARTIDA', font=('Helvetica', 16), justification='center')],
            [sg.Text('Nome do jogador:'), sg.InputText(key='nome')],
            [sg.Text('Senha:'), sg.InputText(key='senha')],
            [sg.Text('Tamanho do oceano (mínimo = 7, máximo = 10):'), sg.InputText(key='tamanho_oceano')],
            [sg.Button('Iniciar Partida', size=(15, 2))],
        ]

        window = sg.Window('Batalha Naval - Iniciar Partida', layout, element_justification='center')

        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED:
                window.close()
                return None

            if event == 'Iniciar Partida':
                window.close()
                return {
                    'nome': values['nome'],
                    'senha': values['senha'],
                    'tamanho_oceano': values['tamanho_oceano']
                }

    def posicionar_barcos(self, barco):
        layout = [
            [sg.Text(f'Posicionar {barco}', font=('Helvetica', 16), justification='center')],
            [sg.Text('Escolha a posição:'), sg.InputText(key='posicao')],
            [sg.Button('Confirmar', size=(10, 2))]
        ]

        window = sg.Window(f'Batalha Naval - Posicionar {barco}', layout, element_justification='center')

        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED:
                window.close()
                return None

            if event == 'Confirmar':
                window.close()
                return {'posicao': values['posicao']}

    def atirar(self):
        layout = [
            [sg.Text('ATIRAR', font=('Helvetica', 16), justification='center')],
            [sg.Text('Insira a posição do tiro:'), sg.InputText(key='posicao')],
            [sg.Button('Atirar', size=(10, 2))]
        ]

        window = sg.Window('Batalha Naval - Atirar', layout, element_justification='center')

        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED:
                window.close()
                return None

            if event == 'Atirar':
                window.close()
                return {'posicao': values['posicao']}

    def mostrar_legenda_oceano(self):
        sg.popup('LEGENDAS\n~ = OCEANO   x = TIRO    B = BOTE    S = SUBMARINO   F = FRAGATA     P = PORTA-AVIÕES    O = ACERTO DE TIRO EM ALGUM NAVIO')

    def mostrar_mensagem(self, mensagem):
        sg.popup(mensagem)

    def mostrar_linha(self, char, linha):
        sg.popup(char + ' ' + ' '.join(linha))

    def mostrar_coordenada(self, contador):
        sg.popup(str(contador), title='Coordenada')

    def mostrar_espaco(self):
        sg.popup('  ')
