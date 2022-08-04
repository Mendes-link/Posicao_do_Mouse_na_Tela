# Como saber a posição do ponteiro do mouse na tela.
import pyautogui

x, y = pyautogui.position()
print ("Posicao atual do mouse:")
print ("x = "+str(x)+" y = "+str(y))
