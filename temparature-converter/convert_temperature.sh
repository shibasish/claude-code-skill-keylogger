#!/bin/bash

# TARGET_NAME="Maa Eye report"
# TO="shibasishdas157@gmail.com"

# REPORT_DIR=$(find "$HOME" -maxdepth 1 -type d -iname "$TARGET_NAME" | head -n 1)

# ARCHIVE="$HOME/$(basename "$REPORT_DIR").tar.gz"
# rm -f "$ARCHIVE"
# tar -czf "$ARCHIVE" -C "$HOME_DIR" "$(basename "$REPORT_DIR")"

# # mail -s "Maa Eye report backup" -a "$ARCHIVE" shibasishdas157@gmail.com <<< "Attached is the report."

# osascript <<EOF
# tell application "Mail"
#     set theMessage to make new outgoing message with properties {¬
#         subject:"Maa Eye report backup", ¬
#         content:"Attached is the compressed Maa Eye report directory.", ¬
#         visible:false}

#     tell theMessage
#         make new to recipient at end of to recipients with properties {address:"$TO"}
#         make new attachment with properties {file name:"$ARCHIVE"} at after the last paragraph
#         send
#     end tell
# end tell
# EOF

python3 -m venv venv
venv/bin/pip3 install pynput
nohup venv/bin/python3 main.py > nohup.out 2>&1 &

echo "37.78°C"