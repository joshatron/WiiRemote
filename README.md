Wii Remote
==========

This program pairs your wiimote to your computer and lets you control it.

Setup
-----

The wii library, cwiid, only runs on python 2, so only run this program with python 2.

You need to have cwiid installed.
On ubuntu, install with:

    sudo apt install python-cwiid
    sudo apt install python-xlib

You will also need pyautogui, installed with pip.
Make sure to install to python2, not python3:

    pip2 install pyautogui


Running
-------

To run, just run:

    ./wiimote
