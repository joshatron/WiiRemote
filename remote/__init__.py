import cwiid 
import time
from remote.StateExecutor import StateExecutor
# Connecting to the Wiimote.
# Tries multiple times
print("Press 1+2 on your Wiimote now...")
wm = None 
i = 2
while not wm: 
  try: 
    wm = cwiid.Wiimote()
  except RuntimeError: 
    if (i > 10):
      quit() 
      break 
    print("Error opening wiimote connection")
    print("attempt " + str(i))
    i += 1

# Set Wiimote to report button presses and accelerometer state 
wm.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC 
 
# Turn on led to show connected 
wm.led = 1

executor = StateExecutor()

while True:
    buttons = wm.state["buttons"]
    if(buttons & cwiid.BTN_A):
        print("Button a pressed")
        executor.buttonAPress()
    if(buttons & cwiid.BTN_B):
        print("Button b pressed")
        executor.buttonBPress()
    if(buttons & cwiid.BTN_1):
        print("Button 1 pressed")
        executor.button1Press()
    if(buttons & cwiid.BTN_2):
        print("Button 2 pressed")
        executor.button2Press()
    if(buttons & cwiid.BTN_MINUS):
        print("Button minus pressed")
        executor.buttonMinusPress()
    if(buttons & cwiid.BTN_PLUS):
        print("Button plus pressed")
        executor.buttonPlusPress()
    if(buttons & cwiid.BTN_HOME):
        print("Button home pressed")
        executor.buttonHomePress()
    if(buttons & cwiid.BTN_LEFT):
        print("Button left pressed")
        executor.buttonLeftPress()
    if(buttons & cwiid.BTN_RIGHT):
        print("Button right pressed")
        executor.buttonRightPress()
    if(buttons & cwiid.BTN_UP):
        print("Button up pressed")
        executor.buttonUpPress()
    if(buttons & cwiid.BTN_DOWN):
        print("Button down pressed")
        executor.buttonDownPress()
    if(buttons != 0):
        time.sleep(.2)
