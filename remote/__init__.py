import cwiid 
import time
# Connecting to the Wiimote.
# Tries multiple times
print 'Press 1+2 on your Wiimote now...' 
wm = None 
i=2 
while not wm: 
  try: 
    wm=cwiid.Wiimote() 
  except RuntimeError: 
    if (i>10): 
      quit() 
      break 
    print "Error opening wiimote connection" 
    print "attempt " + str(i) 
    i +=1 

# Set Wiimote to report button presses and accelerometer state 
wm.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC 
 
# Turn on led to show connected 
wm.led = 1

while True:
    buttons = wm.state["buttons"]
    if(buttons & cwiid.BTN_A):
        print("Button a pressed")
    if(buttons & cwiid.BTN_B):
        print("Button b pressed")
    if(buttons & cwiid.BTN_1):
        print("Button 1 pressed")
    if(buttons & cwiid.BTN_2):
        print("Button 2 pressed")
    if(buttons & cwiid.BTN_MINUS):
        print("Button minus pressed")
    if(buttons & cwiid.BTN_PLUS):
        print("Button plus pressed")
    if(buttons & cwiid.BTN_HOME):
        print("Button home pressed")
    if(buttons & cwiid.BTN_LEFT):
        print("Button left pressed")
    if(buttons & cwiid.BTN_RIGHT):
        print("Button right pressed")
    if(buttons & cwiid.BTN_UP):
        print("Button up pressed")
    if(buttons & cwiid.BTN_DOWN):
        print("Button down pressed")
    if(buttons != 0):
        time.sleep(.2)
