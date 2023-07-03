import os
import subprocess
import sys

try:

    def check_adb_exists():
        try:
            result = subprocess.run(['adb', 'version'], capture_output=True, text=True)
            return True
        except FileNotFoundError:
            return False

    if not check_adb_exists():
        print("ADB is not installed or not accessible. Please make sure ADB is installed and added to the system's PATH.")
        input("Press Enter to exit...")
        sys.exit()

    def check_devices_connected():
        result = subprocess.run(['adb', 'devices'], capture_output=True, text=True)
        output = result.stdout.strip().split('\n')[1:]
        devices = [line.split('\t')[0] for line in output if line.strip()]
        return bool(devices)

    if not check_devices_connected():
        print("No devices found. Please connect a device and/or accept USB debugging, and try again.")
        input("Press Enter to exit...")
        sys.exit()    

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
        response = input("Do you wanna uninstall Xiaomi ShareMe? [Y/n] ")
        if response == '' or response == 'y' or response == 'Y':
            print("Uninstalling Xiaomi Game Center...")
            os.system('adb shell pm uninstall -k --user 0 com.xiaomi.midrop')
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
            
    input("Finished! Press Enter to exit...")
    sys.exit() 

except KeyboardInterrupt:
    sys.exit()
