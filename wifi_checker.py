import os
import time
import platform    # For getting the operating system name
import subprocess  # For executing a shell command
from tkinter import *

def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    if platform.system().lower()=='windows':
        param = '-n'
    else:
        param = '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]

    return subprocess.call(command) == 0

def main():
    # Run ping function
    result = ping(hostname)
    # If there is a connection to google.com, all good
    if result == True:
        return('WiFi is up.')
    # If there is no connection to google.com, restart the WiFi-module
    else:
        time.sleep(2)
        scnd = ping(hostname)
        if scnd == False:
            os.system("networksetup -setairportpower airport off")
            v.set('No response. Deactivating now...')
            time.sleep(5)
            os.system("networksetup -setairportpower airport on")
            time.sleep(5)
            return('WiFi restarted.')
        else:
            return('Slow response. Might break.')


running = True  # Global flag
def scanning():
    if running:  # Only do this if the Stop button has not been clicked
        v.set(main())

    # After 10 seconds, call scanning again (create a recursive loop)
    root.after(10000, scanning)

def start():
    """Enable scanning by setting the global flag to True."""
    global running
    running = True
    # 1 second after start call scanning
    root.after(1000, scanning)

def stop():
    """Stop scanning by setting the global flag to False."""
    global running
    running = False
    v.set('Stopped.')

# Define TKinter GUI
hostname = "google.com" #example
root = Tk()
# width x height + x_offset + y_offset:
root.geometry("150x115+10+5")
root.title("WiFi Checker")
v = StringVar()
w = Label(root, textvariable=v, relief=RIDGE, height=2, wraplength=100)
w.pack(fill = X, padx=5, pady=5)
button1 = Button(root, text='Start', command=start)
button1.pack(fill = X, padx=5, pady=2)
button2 = Button(root, text='Stop',command=stop)
button2.pack(fill = X, padx=5, pady=2)

root.mainloop()


# To compile new file run pyinstaller wifi_checker.py -F -w in the .py-file's directory
# -F will make it one file and -w creates a windowed, no-console version (on MAC OSX it creates a standalone app)