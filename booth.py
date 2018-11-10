import os
from PIL import Image
from random import shuffle
import twitter
import RPi.GPIO as GPIO
import json
import sys
import time
import requests

pedalPin = 2
GPIO.setmode(GPIO.BCM)
GPIO.setup(pedalPin, GPIO.IN)

def main():
    while True:
        if GPIO.input(pedalPin) == 0:
            print("WOW")
            time.sleep(2)
            takePhotos();

def takePhotos():
    print("Taking picture")
    os.system("gphoto2 --capture-image-and-download --force-overwrite --filename=1.jpg")
    time.sleep(4)

    os.system("gphoto2 --capture-image-and-download --force-overwrite --filename=2.jpg")
    time.sleep(4)

    os.system("gphoto2 --capture-image-and-download --force-overwrite --filename=3.jpg")
    time.sleep(4)

    os.system("gphoto2 --capture-image-and-download --force-overwrite --filename=4.jpg")
    time.sleep(4)

    # Get Image size
    img_names = ["1.jpg", "2.jpg", "3.jpg", "4.jpg"]
    w, h = Image.open(img_names[0]).size
    out = Image.new("RGB", (2 * w + 30, 2 * h + 30), "white")

    shuffle(img_names)
    out.paste(Image.open(img_names[0]), (10, 10))
    out.paste(Image.open(img_names[1]), (w + 20, 10))
    out.paste(Image.open(img_names[2]), (10, h + 20))
    out.paste(Image.open(img_names[3]), (w + 20, h + 20))
    out.save("out.jpg")
    twitter.postPhoto("out.png", "#GreatUniHack #GUH18")
    

# Main method
if __name__ == "__main__":
    main()
