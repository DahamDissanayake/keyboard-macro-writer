import time
import random
import sys
from pynput.keyboard import Key, Controller

def countdown(seconds):
    """Display a countdown timer."""
    for i in range(seconds, 0, -1):
        print(f"\rStarting in {i} seconds...", end="", flush=True)
        time.sleep(1)
    print(f"\rStarting in 0 seconds... GO!", flush=True)
    time.sleep(0.5)  # Brief pause before starting
    print()

def send_keystrokes(text):
    """Send actual keystrokes for each character in the text."""
    keyboard = Controller()
    
    print("Sending keystrokes in 2 seconds...")
    time.sleep(2)  # Give time to focus on target application
    
    for char in text:
        # Send the actual keystroke
        if char == '\n':
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
        elif char == '\t':
            keyboard.press(Key.tab)
            keyboard.release(Key.tab)
        else:
            keyboard.type(char)
        
        # Random delay between 1-3 milliseconds
        delay = random.uniform(0.25, 0.028)  # 1-3 ms
        time.sleep(delay)
    
    print("\n\nKeystroke simulation complete!")

def main():
    print("=== Keystroke Typing Simulator ===")
    print("This will send actual keystrokes to your active window!")
    print("Make sure to click on the target text field before the countdown ends.")
    print()
    
    # Check if pynput is available
    try:
        from pynput.keyboard import Key, Controller
    except ImportError:
        print("ERROR: pynput library is required!")
        print("Install it with: pip install pynput")
        return
    
    print("Enter your text or paragraph (press Enter twice when done):")
    print()
    
    # Get input text (allowing multiline input)
    lines = []
    while True:
        try:
            line = input()
            if line == "" and lines and lines[-1] == "":
                # Two consecutive empty lines means end of input
                lines.pop()  # Remove the last empty line
                break
            lines.append(line)
        except EOFError:
            break
    
    # Join lines with newlines to preserve original formatting
    text = "\n".join(lines)
    
    if not text.strip():
        print("No text entered. Exiting...")
        return
    
    print(f"\nText received! ({len(text)} characters)")
    print("=" * 50)
    print("IMPORTANT: After pressing Enter below:")
    print("1. Click on the text field where you want the text typed")
    print("2. Wait for the countdown to finish")
    print("3. The keystrokes will be sent automatically")
    print("=" * 50)
    
    # Ask to start
    input("Press Enter when you're ready to start...")
    
    # 5-second countdown
    countdown(5)
    
    # Start keystroke simulation
    try:
        send_keystrokes(text)
    except Exception as e:
        print(f"Error during keystroke simulation: {e}")
        print("Make sure you have the necessary permissions for keyboard automation.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nSimulation interrupted by user.")
        sys.exit(0)