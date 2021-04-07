from pynput import mouse

m_mouse = mouse.Controller()

import time
from pynput import mouse, keyboard

time.sleep(5)
m_mouse = mouse.Controller()
m_keyboard = keyboard.Controller()

m_mouse.position = (850, 670)

m_mouse.click(mouse.Button.left)

while(True) :
    m_keyboard.type("狗比")
    m_keyboard.press(keyboard.Key.enter)
    m_keyboard.release(keyboard.Key.enter)

    time.sleep(0.5)
