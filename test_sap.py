from pywinauto.application import Application
from pywinauto.keyboard import send_keys
from pywinauto import timings
import pyautogui
import time

app = Application(backend='uia').connect(title_re="Enter Incoming Invoice")
miro_window = app.window(title_re="Enter Incoming Invoice")
# miro_window.set_focus()
miro_window.print_control_identifiers(depth=5)