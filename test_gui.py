import PySimpleGUI as sg

sg.theme('DarkBlue14')

layout = [
    [sg.Text('Your name'), sg.InputText(key='_NAME_')],
    [sg.Button('Show')]
]

window = sg.Window('My first GUI application', layout = layout)


while True:
    event, values = window.read()

    if event == None:
        break

    if event == 'Show':
        sg.popup(f'Input: {values["_NAME_"]}')

window.close()