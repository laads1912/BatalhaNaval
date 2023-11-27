import PySimpleGUI as sg


class TelaPartida:
    def __init__(self):
        sg.theme('DarkGrey2')
        self.__window = None
        self.__init_opcoes()

    def iniciar_partida(self):
        self.__init_opcoes()
        event, values = self.__window.read()

        if event == sg.WINDOW_CLOSED:
            self.__window.close()
            return None

        if event == 'Iniciar Partida':
            self.__window.close()
            return {
                'nome': values['nome'],
                'senha': values['senha'],
                'tamanho_oceano': values['tamanho_oceano']
            }

    def atirar1(self):
        layout = [
            [sg.Text('ATIRAR', font=('Helvetica', 16), justification='center')],
            [sg.Text('Insira a posição do tiro:'), sg.InputText(key='posicao')],
            [sg.Button('Atirar', size=(10, 2))]
        ]

        self.__window = sg.Window('Batalha Naval - Atirar', layout, element_justification='center')

        while True:
            event, values = self.__window.read()

            if event == sg.WINDOW_CLOSED:
                self.__window.close()
                return None

            if event == 'Atirar':
                self.__window.close()
                return {'posicao': values['posicao']}

    def mostrar_legenda_oceano(self):
        sg.popup('~ = OCEANO   x = TIRO    B = BOTE    S = SUBMARINO   F = FRAGATA     P = PORTA-AVIÕES    O = ACERTO DE TIRO EM ALGUM NAVIO')

    def mostrar_mensagem(self, mensagem):
        sg.popup(mensagem)

    def mostrar_linha(self, char, linha):
        sg.popup(char + ' ' + ' '.join(linha))

    def mostrar_coordenada(self, contador):
        sg.popup(str(contador), title='Coordenada')

    def mostrar_espaco(self):
        sg.popup('  ')

    def __init_opcoes(self):
        layout = [
            [sg.Text('INICIAR PARTIDA', font=('Helvetica', 16), justification='center')],
            [sg.Text('Nome do jogador:'), sg.InputText(key='nome')],
            [sg.Text('Senha:'), sg.InputText(key='senha', password_char='*')],
            [sg.Text('Tamanho do oceano (mínimo = 7, máximo = 10):'), sg.InputText(key='tamanho_oceano')],
            [sg.Button('Iniciar Partida', size=(15, 2))],
        ]

        self.__window = sg.Window('Batalha Naval - Iniciar Partida', layout, element_justification='center')

    def atirar(self, oceanos):
        layout = [
            [sg.Text(oceanos, font=('Arial', 16), justification='center')],
            [sg.Text('ATIRAR', font=('Helvetica', 16), justification='center')],
            [sg.Text('Insira a posição do tiro:'), sg.InputText(key='posicao')],
            [sg.Button('Atirar', size=(10, 2))]
        ]

        self.__window = sg.Window('Batalha Naval - Atirar', layout, element_justification='center')

        while True:
            event, values = self.__window.read()

            if event == sg.WINDOW_CLOSED:
                self.__window.close()
                return None

            if event == 'Atirar':
                self.__window.close()
                return {'posicao': values['posicao']}

    def mostrar_oceano_add_embarcacoes(self, oceano, barco):
        layout = [
            [sg.Text(oceano, font=('Arial', 16), justification='center')],
            [sg.Text(f'Posicionar {barco}', font=('Helvetica', 16), justification='center')],
            [sg.Text('Escolha a posição:'), sg.InputText(key='posicao')],
            [sg.Button('Continuar', size=(15, 2))],
        ]

        self.__window = sg.Window(f'Batalha Naval - Posicionar {barco}', layout, element_justification='center')

        while True:
            event, values = self.__window.read()

            if event == sg.WINDOW_CLOSED:
                self.__window.close()
                return None

            if event == 'Continuar':
                self.__window.close()
                return {'posicao': values['posicao']}
