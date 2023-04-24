import os
import subprocess

try:
    print("Make sure you connected the phone to the PC via USB, enabled USB debugging, and clicked ok in the windows that allows USB debugging from this PC.\n")

    while True:
        response = input("Do you wanna uninstall Mi Music? [Y/n] ")
        if response == '' or response == 'y' or response == 'Y':
            print("Uninstalling Mi Music...")
            os.system('adb shell pm uninstall -k --user 0 com.miui.player')
            break
        elif response == 'n' or response == 'N':
            print("Skipping...")
            break
        else:
            print("Invalid input")

    while True:
        response = input("Do you wanna uninstall Mi Video? [Y/n] ")
        if response == '' or response == 'y' or response == 'Y':
            print("Uninstalling Mi Music...")
            os.system('adb shell pm uninstall -k --user 0 com.miui.videoplayer')
            break
        elif response == 'n' or response == 'N':
            print("Skipping...")
            break
        else:
            print("Invalid input")

    while True:
        response = input("Do you wanna uninstall Mi File Manager? [Y/n] ")
        if response == '' or response == 'y' or response == 'Y':
            print("Uninstalling Mi File Manager...")
            os.system('adb shell pm uninstall -k --user 0 com.mi.android.globalFileexplorer')
            break
        elif response == 'n' or response == 'N':
            print("Skipping...")
            break
        else:
            print("Invalid input")

    while True:
        response = input("Do you wanna uninstall Mi Calculator? [Y/n] ")
        if response == '' or response == 'y' or response == 'Y':
            print("Uninstalling Mi Calculator...")
            os.system('adb shell pm uninstall -k --user 0 com.miui.calculator')
            break
        elif response == 'n' or response == 'N':
            print("Skipping...")
            break
        else:
            print("Invalid input")
            
    while True:
        response = input("Do you wanna uninstall Xiaomi Game Center? [Y/n] ")
        if response == '' or response == 'y' or response == 'Y':
            print("Uninstalling Xiaomi Game Center...")
            os.system('adb shell pm uninstall -k --user 0 com.xiaomi.glgm')
            break
        elif response == 'n' or response == 'N':
            print("Skipping...")
            break
        else:
            print("Invalid input")
                
    while True:
        response = input("Do you wanna uninstall MIUI daily wallpaper (not recommended) [y/N] ")
        if response == '' or response == 'n' or response == 'N':
            print("Skipping...")
            break
        elif response == 'y' or response == 'Y':
            print("Uninstalling MIUI daily wallpaper...")
            os.system('adb shell pm uninstall -k --user 0 com.miui.android.fashiongallery')
            break
        else:
            print("Invalid input")

    while True:
        response = input("Do you wanna uninstall MIUI Cleaner (not recommended) [y/N] ")
        if response == '' or response == 'n' or response == 'N':
            print("Skipping...")
            break
        elif response == 'y' or response == 'Y':
            print("Uninstalling MIUI daily wallpaper...")
            os.system('adb shell pm uninstall -k --user 0 com.miui.android.fashiongallery')
            break
        else:
            print("Invalid input")

except KeyboardInterrupt:
    quit("\n")
