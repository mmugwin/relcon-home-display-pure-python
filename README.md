# Setup

Follow the steps below to create a fresh SD card that runs the home display code at start up. This code was developed for and tested on the Raspberry Pi Zero W, running the Debian Buster OS (with desktop environment). 

1. Flash an image of the Raspberry Pi OS to an SD card. Instructions [here](https://www.raspberrypi.com/documentation/computers/getting-started.html). For this development, Raspberry Pi Imager v1.7 was used.
2. Enable the drivers for the PiTFT screen on the Raspberry Pi. Instructions [here](https://learn.adafruit.com/adafruit-pitft-28-inch-resistive-touchscreen-display-raspberry-pi/easy-install-2). For this development, the ```install-type``` used is ```fbcp``` with a ```rotation``` of ```270```.
3. Install the latest version of python or or any offering above python3.5 on the Raspberry Pi and make it the default.

4. Uninstall the default ```pygame``` package that comes preinstalled with the OS and reinstall the latest version using ```pip```.

5. Enable ```pygame``` to render fonts and images by running the below commands from the terminal.
   
```
sudo apt-get install libsdl2-ttf-2.0-0
sudo apt-get install libsdl2-image-2.0-0
```

6. Enable the hardware serial port on the Raspberry Pi.
7. Save the folder that contains the home display code on the Desktop. You can clone it from this repo, or send it to the Raspberry Pi another way. Now would be a good time to test if the home display code compiles. Run it from the terminal using:

```
sudo python3 /home/pi/Desktop/relcon-home-display-pure-python/home_disp_pygame.py   
```

8. Enable the Raspberry Pi to bypass the desktop at boot. There are many ways to do this, and for this development we did the following:

Run

```
sudo nano /etc/xdg/autostart/display.desktop
```

Enter the following in the file and save. Note that the second argument may be replaced by the path to the ```home_disp_pygame.py``` file if you did not save it on the Desktop.

```
[Desktop Entry]
Name=HomeDisplay
Exec=/usr/bin/python3 /home/pi/Desktop/relcon-home-display-pure-python/home_disp_pygame.py
```

#### If everything went well, your Raspberry Pi is ready to go.
