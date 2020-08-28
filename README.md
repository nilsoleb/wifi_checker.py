# wifi_checker.py
This is a python script to checks continously if the computer has a connection to the internet and if there is no connection, it restarts the WiFi adapter.

The idea arrose when my Macbook Pro (Late 2011) constantly lost it's WiFi connection with no reason and restarting the WiFi adapter would fix it.

It consists of a very rudimentary GUI writen in Tkinter with a status text, a start and a stop button.

## Prerequisites
**This currently only works for Mac OSX.**


## Installation
You can either run the wifi_checker.py-file in the terminal or use pyinstaller to generate an executable app.
For instructions how to install and use pyinstaller please refere to [the official pyinstaller GitHub](https://github.com/pyinstaller/pyinstaller)

**How to use pyinstaller**
```
cd path/to/wifi_checker.py
pyinstaller wifi_checker.py -F -w
```

`-F` will make it one file and `-w` creates a windowed, no-console version (on MAC OSX it creates a standalone app)

## Usage
When you start the script or the app, you'll see the following screen with an empty status text:

![Start_up](images/start_up.png?raw=true "Initial start up")

You then (obviously) click the Start button and depending on whether you have a connection or not you'll see the following:

![Connection](images/all_good.png?raw=true "Connection")

or

![No Connection](images/no_connection.png?raw=true "No Connection")


It automatically pings every 10 secs for a response of "google.com".

## Roadmap
Windows (and potentially Unix) will be added later.
