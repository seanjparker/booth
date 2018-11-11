# booth

# Development

- Pin in source must be set to correct pin
- The stepper has an arbitrary point at which it is triggered. Fully down is 1. Fully up is 1. Somewhere in between is 0. That's why sleep is needed when we find a 0. Because at that arbitrary point, lots of 0s will be sent.
- Dependencies:
    - `apt install libjpeg-dev`
    - some python deps should be in reqs.txt, including `pip install pillow`
    - `apt install gphoto2`
- Error: "Unable to mount device"
    - This happens because when you plug in your camera, gphoto2 mounts the device so you can copy the images!
    - `ps aux | grep gphoto2` should show stuff, other than grep ofc
    - `pkill -9 -f gphoto2` will kill them all!
    - then you can run this stuff
- Networking: get [@samialabed](https://github.com/samialabed) to do it for you

# Operations

- Tape down all the wires and do cable management (taping at an angle helps make it easier to remove)
- Use electrical tape around the photo area so people know how far away to stand (the camera is fairly wide angle)
- Power:
    - Unless there is a separate power input for the camera, the camera can't use the Pi for power (over USB)
    - Have a spare battery. Keep one charging, and keep the other in the camera. Mark the battery at the bottom so you know whose is whose.
- Keep liquids off the damn table!

# Extensions

- Progress with getting a stream to work:
    - `mkfifo fifo.jpg`
    - `gphoto2 --capture-movie --stdout > fifo.jpg &`
    - `omxplayer --live fifo.jpg` - this crashes because apparently omxplayer can't play to "LCD screens" (?)
    - Trying to read `fifo.jpg` with VLC results in 2 FPS (`omxplayer` apparently has this problem as well, but the `--live` flag should fix that, leaving circa 25fps instead)
- Using a LED display or something to show countdown numbers
    - Not attempted yet
- Making the Pi app just sent photos to a web service with an associated "session id" (session id = links four photos together for one session, i.e one montage / collage)
    - Web service would perform stitching & uploading photos to flickr as well as twitter.
