import time

from pynput import keyboard, mouse

time.sleep(5)

# 模拟键盘输入
keyboard.Controller().type('Hello, World!')

# 模拟鼠标点击
mouse.Controller().click(mouse.Button.left)


