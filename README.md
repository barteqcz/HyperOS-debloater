# MIUI-unbloater

### About

This is a simple script, written in Python, which is supposed to safely remove bloatware from Xiaomi MIUI ROM using `adb`.

### Preparing to run

Before running the script, make sure that you're phone is connected to the PC via USB cable, the USB debugging is enabled in the settings, and if you authorized your PC to use USB debugging with your phone. You can check if your phone is being detected, by using `adb devices`.
<br>
On Debian-based distros, you can install `adb` using `sudo apt install adb`.
<br>
On Arch-based distros, you can install `adb` using `sudo pacman -S android-tools`
<br>
On Windows, you'll have to manually download `adb` software and usb android drivers.

#### Enabling usb debugging in MIUI

To enable USB debugging in MIUI, firstly you have to enable developer options. To do that, go to settings > about phone and click 7 times on "MIUI version". Then, go back to the settings main page, and go to advanced settings. Scroll down, and you should see developer options. Open developer options, and scroll down to "USB debugging" option. Enable it.

### Running

#### Linux

Just download the file from the releases page, run `./MIUI-unbloater` on your Linux distro.
<br>
WARNING! Don't run the file by doubleclicking it, since it won't start in CLI mode, and you won't be able to do anything, but the program will be running in the background.

#### Windows

Just download the .exe file from the releases page, and run it.

### Troubleshooting

In case you're getting some errors on Linux, check whether the package 'abd' is installed, and whether the user you're using to run this script is inside a Linux `plugdev` group. In case it isn't, you can add your user to this group by running `sudo usermod -aG plugdev username`.
