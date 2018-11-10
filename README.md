# booth

- Pin in source must be set to correct pin
- The stepper has an arbitrary point at which it is triggered. Fully down is 1. Fully up is 1. Somewhere in between is 0. That's why sleep is needed when we find a 0. Because at that arbitrary point, lots of 0s will be sent.
- Deps:
    - `apt install libjpeg-dev`
    - some python deps should be in reqs.txt
    - `apt install gphoto2`
- Error: "Unable to mount device"
    - This happens because when you plug in your camera, gphoto2 mounts the device so you can copy the images!
    - `ps aux | grep gphoto2` should show stuff, other than grep ofc
    - `pkill -9 -f gphoto2` will kill them all!
    - then you can run this stuff
