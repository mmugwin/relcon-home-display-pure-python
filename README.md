# Setup

Follow the steps below to create a fresh SD card that runs the home display code at start up. This code was developed for and tested on the Raspberry Pi Zero W, running the Debian Buster OS. 

1. Flash an image of the Raspberry Pi OS to an SD card. Instructions [here](https://www.raspberrypi.com/documentation/computers/getting-started.html). For this development, Raspberry Pi Imager v1.7 was used.
2. Enable the drivers for the PiTFT screen on the Raspberry Pi. Instructions [here](https://learn.adafruit.com/adafruit-pitft-28-inch-resistive-touchscreen-display-raspberry-pi/easy-install-2). For this development, the ```install-type``` used is fbcp with a ```rotation``` of ```270```.
3. Install python3.6 or higher and make it the default python on the Raspberry Pi.

Run
```
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 10
```
    
The response should be:

```
update-alternatives: using /usr/bin/python3 to provide /usr/bin/python (python) in auto mode
```

<!-- Check baseline again:

```
python --version Python 3.7.3 $ python3 --version Python 3.7.3
``` -->

4. Uninstall the default ```pygame``` package that comes preinstalled on the Raspberry Pi and reinstall the latest version using ```pip```.

5. Enable ```pygame``` to render fonts and images by running the below commands from the terminal.
   
```
sudo apt-get install libsdl2-ttf-2.0-0
sudo apt-get install libsdl2-image-2.0-0
```

6. Enable the Raspberry Pi to bypass the desktop at boot. There are many ways to do this, and for this development we did the following:

Run

```
sudo nano /etc/xdg/autostart/display.desktop
```

Enter the following in the file and save by ```Ctrl + Y```

```
[Desktop Entry]
Name=HomeDisplay
Exec=/usr/bin/python3 /home/pi/Desktop/relcon-home-display-pure-python/home_disp_pygame.py
```

7. Enable the hardware serial port on the Raspberry Pi.
8. Save the folder that contains the home display code on the Desktop. You can clone it from this repo, or send it to the Raspberry Pi another way. 

If everything went well, your Raspberry Pi is ready to go.
