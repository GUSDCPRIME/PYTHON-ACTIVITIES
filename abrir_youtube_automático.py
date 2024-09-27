import pyautogui 
import time

#esse código tem a função de abrir o microsoft edge e abrir o youtube automaticamente

link = "youtube.com"
pyautogui.PAUSE = 1
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(4.0)
pyautogui.click(x=532, y=104)
pyautogui.write("codigo finalizado :)")
