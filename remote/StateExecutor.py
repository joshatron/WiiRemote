from pyautogui import press, hotkey

class StateExecutor:
    
    def buttonAPress(self):
        press(' ')

    def buttonBPress(self):
        press('esc')

    def button1Press(self):
        hotkey('ctrl', 'alt', 'up')

    def button2Press(self):
        hotkey('ctrl', 'alt', 'down')

    def buttonPlusPress(self):
        press('volumeup')

    def buttonMinusPress(self):
        press('volumedown')

    def buttonHomePress(self):
        hotkey('ctrl', 'alt', 'up')
        hotkey('ctrl', 'alt', 'up')
        hotkey('ctrl', 'alt', 'up')
        hotkey('ctrl', 'alt', 'up')
        hotkey('ctrl', 'alt', 'up')
        hotkey('ctrl', 'alt', 'up')

    def buttonUpPress(self):
        press('up')

    def buttonDownPress(self):
        press('down')

    def buttonLeftPress(self):
        press('left')

    def buttonRightPress(self):
        press('right')
