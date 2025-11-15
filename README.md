# 🔄 Router Reboot Automation

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![Selenium](https://img.shields.io/badge/selenium-latest-green.svg)](https://www.selenium.dev/)

Automate your router reboot with style! This Python script uses Selenium WebDriver to automatically log into your router's web interface and execute a reboot - no more manual clicking through menus.

**🌐 [View Live Demo & Documentation](https://ibrahim24-crypto.github.io/cyberrouter_reboot_improved.py/)**

## ✨ Features

- 🎨 **Two Display Modes**: Choose between Normal (clean) or Hacker (Matrix-style) interface
- ⚡ **Fast & Efficient**: Optimized timing for quick router reboots
- 🔧 **Highly Configurable**: Easy configuration for any router brand
- 🌐 **Multi-Router Support**: Works with Tenda, TP-Link, Netgear, Asus, and more (with configuration)
- 📊 **Real-time Monitoring**: Detects when router successfully reboots by monitoring internet connectivity
- 🎯 **User-Friendly**: Clear progress indicators and error messages

## 🎭 Display Modes

### Normal Mode
Clean and professional interface with clear progress indicators:
```
╔════════════════════════════════════════╗
║     Router Reboot Automation v2.0      ║
║          Normal Mode Active            ║
╚════════════════════════════════════════╝

[1/5] ✓ Login credentials submitted
[2/5] ✓ Advanced settings opened
[3/5] ✓ Reboot option selected
[4/5] ✓ Reboot button clicked
[5/5] ✓ Internet lost detected at 18s
```

### Hacker Mode
Matrix-style terminal with timestamps and ASCII art:
```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃   ██████╗  ██████╗ ██╗   ██╗████████╗ ┃
┃   ██╔══██╗██╔═══██╗██║   ██║╚══██╔══╝ ┃
┃   ██████╔╝██║   ██║██║   ██║   ██║    ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

14:32:15 [>] Target: Router @ 192.168.1.1
14:32:18 [+] Authentication payload delivered
14:32:40 [+] Network outage detected after 18s
```

## 🚀 Quick Start

### Prerequisites

- Python 3.6 or higher
- Chrome, Chromium, or Brave browser
- ChromeDriver (matching your browser version)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ibrahim24-crypto/cyberrouter_reboot_improved.py.git
   cd cyberrouter_reboot_improved.py
   ```

2. **Install dependencies:**
   ```bash
   pip install selenium
   ```

3. **Download ChromeDriver:**
   - Visit [chromedriver.chromium.org](https://chromedriver.chromium.org/downloads)
   - Download the version matching your browser version
   - Extract and place it in a known location

4. **Configure the script:**
   - Open `rebootrouter.py` in a text editor
   - Edit the configuration section at the top of the file
   - Update router IP, credentials, browser path, and ChromeDriver path

### Configuration

Edit these variables at the top of the script:

```python
# Router Configuration
ROUTER_IP = "192.168.1.1"              # Your router's IP address
ROUTER_USERNAME = "admin"              # Your router's admin username
ROUTER_PASSWORD = "your_password"      # Your router's admin password

# Browser Configuration
BROWSER_BINARY = "/usr/bin/brave-browser"  # Path to your browser
CHROMEDRIVER_PATH = "/path/to/chromedriver"  # Path to ChromeDriver
```

### Usage

Run the script:
```bash
python3 rebootrouter.py
```

Select your preferred mode:
- Press `1` for Normal Mode
- Press `2` for Hacker Mode
- Press `0` to exit

The script will:
1. Open your browser
2. Log into your router
3. Navigate to the reboot section
4. Execute the reboot
5. Monitor for connection loss
6. Exit when reboot is confirmed

## ⚙️ How It Works

The script automates the router reboot process in 5 steps:

1. **Login** - Opens router's web interface and authenticates
2. **Navigate** - Accesses Advanced settings menu
3. **Locate** - Finds Management section and Reboot option
4. **Execute** - Clicks reboot button and confirms action
5. **Monitor** - Detects internet connection loss (successful reboot)

## 🔌 Router Compatibility

This script works with most web-based router interfaces:

- ✅ **Tenda** (tested and configured by default)
- 🔧 **TP-Link** (requires configuration)
- 🔧 **Netgear** (requires configuration)
- 🔧 **Asus** (requires configuration)
- 🔧 **D-Link** (requires configuration)
- 🔧 **Linksys** (requires configuration)

### Configuring for Your Router

1. Open your router's web interface in a browser
2. Press F12 to open Developer Tools
3. Inspect the login form and reboot button elements
4. Copy the element IDs and XPaths
5. Update the configuration section in the script:

```python
# Element Selectors (change for your router model)
LOGIN_USERNAME_ID = "username"           # ID of username field
LOGIN_PASSWORD_ID = "password"           # ID of password field
MANAGEMENT_TAB_XPATH = "//a[text()='Management']"  # XPath to Management
REBOOT_BUTTON_XPATH = "//button[@id='reboot']"     # XPath to Reboot button
```

## 🎯 Use Cases

- **Network Troubleshooting**: Quickly reboot router when experiencing connectivity issues
- **Scheduled Maintenance**: Integrate with cron/Task Scheduler for regular reboots
- **Automation**: Part of larger network management scripts
- **Remote Management**: Run from SSH/remote desktop without accessing router physically

## 📋 Common Browser Paths

**Linux:**
- Brave: `/usr/bin/brave-browser`
- Chrome: `/usr/bin/google-chrome`
- Chromium: `/usr/bin/chromium-browser`

**Windows:**
- Chrome: `C:\Program Files\Google\Chrome\Application\chrome.exe`
- Brave: `C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe`

**macOS:**
- Chrome: `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`
- Brave: `/Applications/Brave Browser.app/Contents/MacOS/Brave Browser`

## 🛠️ Troubleshooting

### Script fails at login
- Verify router IP, username, and password are correct
- Check if `LOGIN_USERNAME_ID` and `LOGIN_PASSWORD_ID` match your router's HTML elements

### Cannot find reboot button
- Open router interface and use browser DevTools to find correct XPath
- Update `REBOOT_BUTTON_XPATH` in configuration section

### Browser doesn't open
- Verify `BROWSER_BINARY` path is correct
- Ensure ChromeDriver version matches your browser version
- Check `CHROMEDRIVER_PATH` is correct and file has execute permissions

### Script hangs or times out
- Increase timeout values in configuration section:
  ```python
  PAGE_LOAD_TIMEOUT = 30  # Increase if router is slow
  ELEMENT_WAIT_TIMEOUT = 30
  ```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. 🐛 **Report Bugs**: Open an issue describing the problem
2. 💡 **Suggest Features**: Share your ideas for improvements
3. 🔧 **Submit Pull Requests**: Fix bugs or add new features
4. 📝 **Improve Documentation**: Help others use the script
5. ⭐ **Star the Repository**: Show your support!

### Development Setup

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Test thoroughly
5. Commit: `git commit -am 'Add feature'`
6. Push: `git push origin feature-name`
7. Submit a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 Router Reboot Automation Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

## ⚠️ Disclaimer

This software is provided "as is", without warranty of any kind. Use at your own risk. Always ensure you have physical access to your router in case something goes wrong.

## 💬 Support

Need help? Here's how to get support:

- 📋 Check [existing issues](https://github.com/ibrahim24-crypto/cyberrouter_reboot_improved.py/issues)
- 💬 Open a [new issue](https://github.com/ibrahim24-crypto/cyberrouter_reboot_improved.py/issues/new)
- 📖 Read the [documentation](https://ibrahim24-crypto.github.io/cyberrouter_reboot_improved.py/)

## 🙏 Acknowledgments

- Thanks to all contributors who help improve this project
- Selenium WebDriver team for the automation framework
- The open source community for inspiration and support

## 📊 Project Stats

![GitHub stars](https://img.shields.io/github/stars/ibrahim24-crypto/cyberrouter_reboot_improved.py?style=social)
![GitHub forks](https://img.shields.io/github/forks/ibrahim24-crypto/cyberrouter_reboot_improved.py?style=social)
![GitHub issues](https://img.shields.io/github/issues/ibrahim24-crypto/cyberrouter_reboot_improved.py)
![GitHub pull requests](https://img.shields.io/github/issues-pr/ibrahim24-crypto/cyberrouter_reboot_improved.py)

---

Made with ❤️ by the Open Source Community

**[⬆ Back to Top](#-router-reboot-automation)**
