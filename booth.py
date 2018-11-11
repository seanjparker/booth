import os
from PIL import Image
from random import shuffle
import twitter
from threading import Thread
import RPi.GPIO as GPIO
import json
import sys
import time
import requests
import subprocess

pedalPin = 2
GPIO.setmode(GPIO.BCM)
GPIO.setup(pedalPin, GPIO.IN)

def main():
    while True:
        if GPIO.input(pedalPin) == 0:
            print("WOW")
            time.sleep(2)
            takePhotos();

def cowsay(str):
    subprocess.call(['cowsay', str])

def send(n):
    twitter.postPhoto(cowsay, "out.jpg", "#GreatUniHack #GUH18", n)


photoNumber = 0
def takePhotos():
    global photoNumber
    n = str(photoNumber) + " "
    cowsay(n + "Taking picture ")
    os.system("gphoto2 --capture-image-and-download --force-overwrite -F 4 -I 2")

    cowsay(n + "Stitching photos")
    # Get Image size
    img_names = ["capt0000.jpg", "capt0001.jpg", "capt0002.jpg", "capt0003.jpg"]
    w, h = Image.open(img_names[0]).size
    out = Image.new("RGB", (2 * w + 30, 2 * h + 30), "white")

    # shuffle(img_names)
    out.paste(Image.open(img_names[0]), (10, 10))
    out.paste(Image.open(img_names[1]), (w + 20, 10))
    out.paste(Image.open(img_names[2]), (10, h + 20))
    out.paste(Image.open(img_names[3]), (w + 20, h + 20))

    out.thumbnail((1920, 1080), Image.ANTIALIAS)
    out.save("out.jpg")

    # print("Push thread " + n)
    # thread = Thread(target = send, args = (n, ))
    # thread.start()

    send(n)

    photoNumber += 1
    

# Main method
if __name__ == "__main__":
    main()
