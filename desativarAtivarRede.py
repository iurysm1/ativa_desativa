import time
import pyautogui
from flask import flash

def resetaPlacaDeRede():
    # abre menu windows
    pyautogui.hotkey('winleft','x')
    time.sleep(1)
    # entra nas conexões de rede
    pyautogui.press('down', presses=6)
    pyautogui.press('enter')
    time.sleep(2)

    # entra nas configurações do adaptador
    pyautogui.press('tab', presses=5)
    pyautogui.press('enter')
    time.sleep(1)

    # seleciona a placa de rede
    pyautogui.press('right')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)

    # desativa, espera 10s e ativa
    pyautogui.press('tab', presses=2)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(10) # espera 10 segundos
    pyautogui.press('enter')

    # fecha janelas
    time.sleep(5)
    pyautogui.hotkey('alt', 'f4')
    pyautogui.hotkey('alt', 'f4')
    
