from PySimpleGUI import PySimpleGUI as sg
from bot import CorreiosBot

# Theme
sg.theme('Reddit')

# Layout
layout = [
    [sg.Text('Código de Rastreio'), sg.Input(justification='center',key='rastreio', size=(20, 1))],
    [sg.Button('Rastrear!')]
]

# Window
janela = sg.Window('Rastreio de encomendas', layout)

# Read events
while True:
    evento, valor = janela.read()
    if evento == sg.WINDOW_CLOSED:
        break
    if evento == 'Rastrear!':
        codigo = CorreiosBot('rastreio')
        codigo.rastrear()
