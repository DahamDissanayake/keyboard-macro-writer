# Keystroke Typing Simulator

A Python GUI application that simulates human-like typing by automatically typing text with realistic delays and variations. Perfect for automating text input, testing applications, or demonstrations.

![Python](https://img.shields.io/badge/python-3.6+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)

## Features

- **Human-like Typing**: Simulates realistic typing patterns with random delays
- **Multiple Speed Settings**: Choose between Fast, Normal, and Slow typing speeds
- **Customizable Countdown**: Set a countdown timer (1-10 seconds) before typing begins
- **Real-time Progress**: Visual progress bar and character counter
- **Special Character Support**: Handles newlines, tabs, and special characters
- **Cross-platform**: Works on Windows, macOS, and Linux
- **Modern GUI**: Clean, intuitive interface built with tkinter
- **Thread-safe**: Non-blocking operation with proper thread management

## Screenshots

The application features a clean, modern interface with:
- Large text input area with scroll support
- Real-time character counting
- Speed and countdown settings
- Progress tracking
- Start/Stop controls

## Requirements

- Python 3.6 or higher
- `pynput` library for keyboard automation
- `tkinter` (usually included with Python)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/DahamDissanayake/keystroke-simulator.git
   cd keystroke-simulator
   ```

2. **Install required dependencies:**
   ```bash
   pip install pynput
   ```

3. **Run the application:**
   ```bash
   python main.py
   ```

### Alternative Installation (pip)

```bash
pip install pynput
wget https://raw.githubusercontent.com/DahamDissanayake/keystroke-simulator/main/main.py
python main.py
```

## Usage

### Basic Usage

1. **Launch the application:**
   ```bash
   python main.py
   ```

2. **Enter your text:**
   - Type or paste text into the large text area
   - The character count updates automatically

3. **Configure settings:**
   - **Typing Speed**: Choose from Fast (30-36ms), Normal (36-45ms), or Slow (45-60ms)
   - **Countdown**: Set delay before typing starts (1-10 seconds)

4. **Start typing simulation:**
   - Click "Start Typing Simulation"
   - Quickly click on the target application/text field
   - Wait for countdown to complete
   - Typing will begin automatically

5. **Control the simulation:**
   - Use "Stop" button to halt typing mid-process
   - "Clear Text" button empties the text area

### Speed Settings Explained

| Setting | Delay Range | Best For |
|---------|-------------|----------|
| **Fast (good)** | 30-36ms | Quick data entry, less detection |
| **Normal (accurate)** | 36-45ms | General purpose, natural feel |
| **Slow (more accurate)** | 45-60ms | Careful typing, better compatibility |

### Keyboard Automation Permissions

**macOS:**
- System Preferences → Security & Privacy → Privacy → Accessibility
- Add Terminal or Python to allowed applications

**Windows:**
- Usually works without additional setup
- Some antivirus software may require exceptions

**Linux:**
- Ensure X11 forwarding if using SSH
- May require running with appropriate user permissions

## Code Structure

```
main.py
├── KeystrokeSimulatorGUI (Main Class)
│   ├── __init__()           # Initialize GUI and components
│   ├── setup_gui()          # Create interface elements
│   ├── simulation_thread()  # Handle typing in separate thread
│   ├── send_keystrokes()    # Core typing logic
│   ├── countdown()          # Countdown timer
│   └── utility methods      # Status updates, character counting
└── main()                   # Entry point and theme setup
```

## Key Features Explained

### Human-like Typing Simulation
- Random delays between keystrokes (configurable ranges)
- Proper handling of special characters (Enter, Tab)
- Realistic typing patterns

### Thread Management
- Non-blocking GUI operation
- Proper thread cleanup on application exit
- Safe start/stop functionality

### Cross-platform Compatibility
- Uses `pynput` for universal keyboard control
- Automatic theme detection and fallbacks
- Handles different system requirements

## Troubleshooting

### Common Issues

**"pynput library is required" Error:**
```bash
pip install pynput
```

**Permission Denied (macOS):**
- Grant accessibility permissions in System Preferences
- Restart Terminal after granting permissions

**Typing Not Working:**
- Ensure target application is focused before countdown ends
- Check that keyboard automation is allowed
- Try running as administrator (Windows) or with sudo (Linux)

**Application Won't Start:**
- Verify Python 3.6+ is installed: `python --version`
- Check tkinter availability: `python -c "import tkinter"`

### Performance Tips

- Use "Fast" mode for large text blocks
- Close unnecessary applications to reduce system load
- Ensure stable system performance during typing

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Test thoroughly on your platform
5. Submit a pull request

### Coding Standards

- Follow PEP 8 style guidelines
- Add comments for complex logic
- Maintain cross-platform compatibility
- Include error handling for new features

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**DAMA**
- GitHub: [@DahamDissanayake](https://github.com/DahamDissanayake)

## Acknowledgments

- Built with Python's `tkinter` for the GUI
- Uses `pynput` library for cross-platform keyboard automation
- Inspired by the need for realistic typing automation tools

## Disclaimer

This tool is intended for legitimate automation and testing purposes. Users are responsible for ensuring compliance with applicable terms of service and local laws when using keyboard automation software.

---

⭐ If you find this project helpful, please consider giving it a star on GitHub!