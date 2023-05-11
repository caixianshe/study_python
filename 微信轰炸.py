# 微信短信轰炸
import time
from pynput import mouse, keyboard

time.sleep(5)

# m_mouse = mouse.Controller()  # 创建一个鼠标对象
m_keyboard = keyboard.Controller()  # 创建一个键盘

# m_mouse.position = (850, 670) #鼠标放置的坐标位置
# m_mouse.click(mouse.Button.left) # 模拟鼠标左键点击一次

i = 0
while i < 1150:
    m_keyboard.type('亲')
    m_keyboard.press(keyboard.Key.enter)  # 按下enter键
    m_keyboard.release(keyboard.Key.enter)  # 松开enter键
    i += 1

time.sleep(5)
