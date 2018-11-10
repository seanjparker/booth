import os
import time
from random import shuffle

import RPi.GPIO as GPIO
from PIL import Image

import twitter

pedalPin = 2
GPIO.setmode(GPIO.BCM)
GPIO.setup(pedalPin, GPIO.IN)


def send(n):
    print("Sending ")
    twitter.postPhoto("out.jpg", "#GreatUniHack #GUH18", n)


photo_number = 0


def take_photos():
    global photo_number
    n = str(photo_number)
    print("Taking picture " + n)
    os.system("gphoto2 --capture-image-and-download --force-overwrite --filename=1.jpg")
    time.sleep(1.5)

    os.system("gphoto2 --capture-image-and-download --force-overwrite --filename=2.jpg")
    time.sleep(1.5)

    os.system("gphoto2 --capture-image-and-download --force-overwrite --filename=3.jpg")
    time.sleep(1.5)

    os.system("gphoto2 --capture-image-and-download --force-overwrite --filename=4.jpg")
    time.sleep(1.5)

    print("Stitching photos: " + n)
    # Get Image size
    img_names = ["1.jpg", "2.jpg", "3.jpg", "4.jpg"]
    w, h = Image.open(img_names[0]).size
    out = Image.new("RGB", (2 * w + 30, 2 * h + 30), "white")

    shuffle(img_names)
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

    photo_number += 1


GPIO.add_event_detect(pedalPin, GPIO.FALLING, callback=take_photos, bouncetime=300)

# Main method
if __name__ == "__main__":
    while True:
        time.sleep(300)
