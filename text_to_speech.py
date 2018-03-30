<<<<<<< HEAD
#!/usr/env python
# -*- coding : utf-8 -*-
#
# text_to_speech.py
#
'''
Text to speech part that reads from 'test.txt'
'''

# import pywin
try:
    import pyttsx3 as pyttsx
except ImportError:
    import pyttsx
from pytesseract import image_to_string
try:
    import pillow
except ImportError:
    from PIL import Image
import os, sys, subprocess
from cv2 import *
import image_to_text as itt

# Initialize the camera
cam = VideoCapture(1)   # 1 -> index of camera
s, img = cam.read()

itt.func()

# Initialize TTS engine
engine = pyttsx.init()
engine.setProperty('rate', 100)

# Read text file
with open("test.txt", "r+") as testFile:
    for line in testFile.readlines():
        engine.say(line)

engine.runAndWait()
