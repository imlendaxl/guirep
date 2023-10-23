import PySimpleGUI as psg
layout = [
    [psg.Button('--- GANHE DINHEIRO FACIL E RAPIDO! ---', size=(200, 200))]]
window = psg.Window('qlq coisa', layout, no_titlebar=True, size=(1280,720))


while True:
    evento, valor = window.read()
    if evento == psg.WIN_CLOSED:
        break
    else:
        psg.popup('ANÚNCIO IMPORTANTE !!! \n VOCÊ GANHOU 1 MILHÃO DE REAIS!', title='SENAI', no_titlebar=True,  button_type = 4,
                  button_color = 'indian red', background_color = 'red')

window.close()