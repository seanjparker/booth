# booth

- Pin in source must be set to correct pin
- The stepper has an arbitrary point at which it is triggered. Fully down is 1. Fully up is 1. Somewhere in between is 0. That's why sleep is needed. Because at that arbitrary point, lots of 0s will be sent.
- Deps:
    - `apt install libjpeg-dev`
    - some python deps should be in reqs.txt
    - `apt install gphoto2`

