import time
import random
import sys
import threading
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from pynput.keyboard import Key, Controller

class KeystrokeSimulatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Keystroke Typing Simulator")
        self.root.geometry("700x600")
        self.root.resizable(True, True)
        
        # Remove default tkinter icon
        self.root.iconbitmap()
        # Alternative method for different systems
        try:
            self.root.iconphoto(False, tk.PhotoImage(width=1, height=1))
        except:
            pass
        
        # Check if pynput is available
        try:
            from pynput.keyboard import Key, Controller
            self.keyboard = Controller()
        except ImportError:
            messagebox.showerror("Error", "pynput library is required!\nInstall it with: pip install pynput")
            self.root.destroy()
            return
        
        self.is_running = False
        self.setup_gui()
        
    def setup_gui(self):
        """Setup the GUI components."""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(1, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="Keystroke Typing Simulator", 
                               font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, pady=(0, 10))
        
        # Text input frame
        text_frame = ttk.LabelFrame(main_frame, text="Text to Type", padding="10")
        text_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        text_frame.columnconfigure(0, weight=1)
        text_frame.rowconfigure(0, weight=1)
        
        # Text area
        self.text_area = scrolledtext.ScrolledText(text_frame, height=15, width=70,
                                                   wrap=tk.WORD, font=("Consolas", 10))
        self.text_area.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Character count label
        self.char_count_label = ttk.Label(text_frame, text="Characters: 0")
        self.char_count_label.grid(row=1, column=0, sticky=tk.W, pady=(5, 0))
        
        # Settings frame
        settings_frame = ttk.LabelFrame(main_frame, text="Settings", padding="10")
        settings_frame.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Delay settings
        delay_frame = ttk.Frame(settings_frame)
        delay_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 5))
        
        ttk.Label(delay_frame, text="Typing Speed:").grid(row=0, column=0, sticky=tk.W)
        
        self.speed_var = tk.StringVar(value="Normal (accurate)")
        speed_combo = ttk.Combobox(delay_frame, textvariable=self.speed_var, 
                                   values=["Fast (good)", "Normal (accurate)", "Slow (more accurate)"],
                                   state="readonly", width=25)
        speed_combo.grid(row=0, column=1, padx=(10, 0))
        
        # Countdown settings
        countdown_frame = ttk.Frame(settings_frame)
        countdown_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(5, 0))
        
        ttk.Label(countdown_frame, text="Countdown (seconds):").grid(row=0, column=0, sticky=tk.W)
        
        self.countdown_var = tk.IntVar(value=5)
        countdown_spin = ttk.Spinbox(countdown_frame, from_=1, to=10, 
                                     textvariable=self.countdown_var, width=10)
        countdown_spin.grid(row=0, column=1, padx=(10, 0))
        
        # Control buttons frame
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=3, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Start button
        self.start_button = ttk.Button(button_frame, text="Start Typing Simulation", 
                                       command=self.start_simulation, style="Accent.TButton")
        self.start_button.pack(side=tk.LEFT, padx=(0, 10))
        
        # Stop button
        self.stop_button = ttk.Button(button_frame, text="Stop", 
                                      command=self.stop_simulation, state="disabled")
        self.stop_button.pack(side=tk.LEFT, padx=(0, 10))
        
        # Clear button
        clear_button = ttk.Button(button_frame, text="Clear Text", 
                                  command=self.clear_text)
        clear_button.pack(side=tk.LEFT)
        
        # Status frame
        status_frame = ttk.Frame(main_frame)
        status_frame.grid(row=4, column=0, sticky=(tk.W, tk.E))
        
        self.status_label = ttk.Label(status_frame, text="Ready", 
                                      font=("Arial", 10))
        self.status_label.pack(side=tk.LEFT)
        
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(status_frame, variable=self.progress_var, 
                                            length=200, mode='determinate')
        self.progress_bar.pack(side=tk.RIGHT)
        
        # Instructions
        instructions = """Instructions:
1. Enter or paste your text in the text area above
2. Choose your typing speed and countdown duration
3. Click 'Start Typing Simulation'
4. Click on the target text field where you want the text typed
5. Wait for the countdown to finish - typing will begin automatically

Note: Make sure you have the necessary permissions for keyboard automation."""
        
        instructions_frame = ttk.LabelFrame(main_frame, text="Instructions", padding="10")
        instructions_frame.grid(row=5, column=0, sticky=(tk.W, tk.E), pady=(10, 0))
        
        instructions_label = ttk.Label(instructions_frame, text=instructions, 
                                       justify=tk.LEFT, wraplength=650)
        instructions_label.grid(row=0, column=0, sticky=tk.W)
        
        # Author and GitHub info
        author_frame = ttk.Frame(main_frame)
        author_frame.grid(row=6, column=0, sticky=(tk.W, tk.E), pady=(10, 0))
        
        author_label = ttk.Label(author_frame, text="Author: DAMA", 
                                font=("Arial", 9, "bold"))
        author_label.pack(side=tk.LEFT)
        
        # GitHub link (clickable)
        github_label = ttk.Label(author_frame, text="GitHub: https://github.com/DahamDissanayake", 
                                 font=("Arial", 9), foreground="blue", cursor="hand2")
        github_label.pack(side=tk.RIGHT)
        github_label.bind("<Button-1>", self.open_github)
        
        # Bind events
        self.text_area.bind('<KeyRelease>', self.update_char_count)
        self.text_area.bind('<Button-1>', self.update_char_count)
        
        # Update character count initially
        self.update_char_count()
        
    def update_char_count(self, event=None):
        """Update the character count label."""
        text = self.text_area.get("1.0", tk.END)
        # Subtract 1 because tk.END includes a trailing newline
        char_count = len(text) - 1
        self.char_count_label.config(text=f"Characters: {char_count}")
        
    def clear_text(self):
        """Clear the text area."""
        self.text_area.delete("1.0", tk.END)
        self.update_char_count()
        
    def get_delay_range(self):
        """Get delay range based on selected speed."""
        speed_delays = {
            "Fast (good)": (0.030, 0.036),        # 30-36 ms
            "Normal (accurate)": (0.036, 0.045),  # 36-45 ms
            "Slow (more accurate)": (0.045, 0.060) # 45-60 ms
        }
        return speed_delays.get(self.speed_var.get(), (0.036, 0.045))
        
    def update_status(self, message):
        """Update the status label."""
        self.status_label.config(text=message)
        self.root.update()
        
    def countdown(self, seconds):
        """Display a countdown."""
        for i in range(seconds, 0, -1):
            if not self.is_running:
                return False
            self.update_status(f"Starting in {i} seconds... Click on target window!")
            self.progress_var.set(((seconds - i) / seconds) * 50)  # 50% for countdown
            time.sleep(1)
        
        if self.is_running:
            self.update_status("Starting in 0 seconds... GO!")
            self.progress_var.set(50)
            time.sleep(0.5)
            return True
        return False
        
    def send_keystrokes(self, text):
        """Send keystrokes for each character in the text."""
        min_delay, max_delay = self.get_delay_range()
        total_chars = len(text)
        
        for i, char in enumerate(text):
            if not self.is_running:
                break
                
            try:
                # Send the keystroke
                if char == '\n':
                    self.keyboard.press(Key.enter)
                    self.keyboard.release(Key.enter)
                elif char == '\t':
                    self.keyboard.press(Key.tab)
                    self.keyboard.release(Key.tab)
                else:
                    self.keyboard.type(char)
                
                # Update progress
                progress = 50 + ((i + 1) / total_chars) * 50  # 50-100%
                self.progress_var.set(progress)
                self.update_status(f"Typing... {i + 1}/{total_chars} characters")
                
                # Random delay
                delay = random.uniform(min_delay, max_delay)
                time.sleep(delay)
                
            except Exception as e:
                self.update_status(f"Error: {str(e)}")
                messagebox.showerror("Error", f"Keystroke error: {str(e)}\nMake sure you have keyboard automation permissions.")
                break
        
        if self.is_running:
            self.update_status("Typing complete!")
            self.progress_var.set(100)
        else:
            self.update_status("Typing stopped by user")
            
    def simulation_thread(self):
        """Run the simulation in a separate thread."""
        try:
            text = self.text_area.get("1.0", tk.END).rstrip('\n')
            
            if not text.strip():
                messagebox.showwarning("Warning", "Please enter some text to type!")
                self.reset_buttons()
                return
            
            self.update_status("Preparing...")
            self.progress_var.set(0)
            
            # Countdown
            countdown_seconds = self.countdown_var.get()
            if self.countdown(countdown_seconds):
                # Start typing
                self.send_keystrokes(text)
            
        except Exception as e:
            self.update_status(f"Error: {str(e)}")
            messagebox.showerror("Error", f"Simulation error: {str(e)}")
        finally:
            self.reset_buttons()
            
    def start_simulation(self):
        """Start the keystroke simulation."""
        self.is_running = True
        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")
        
        # Start simulation in a separate thread
        thread = threading.Thread(target=self.simulation_thread, daemon=True)
        thread.start()
        
    def stop_simulation(self):
        """Stop the ongoing simulation."""
        self.is_running = False
        self.update_status("Stopping...")
        
    def reset_buttons(self):
        """Reset button states."""
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")
        self.is_running = False
        
    def open_github(self, event):
        """Open GitHub link in default browser."""
        import webbrowser
        webbrowser.open("https://github.com/DahamDissanayake")

def main():
    # Create the main window
    root = tk.Tk()
    
    # Set the theme to a modern one if available
    try:
        style = ttk.Style()
        # Use a modern theme if available
        available_themes = style.theme_names()
        if 'clam' in available_themes:
            style.theme_use('clam')
        elif 'alt' in available_themes:
            style.theme_use('alt')
    except:
        pass  # Use default theme if styling fails
    
    # Create the application
    app = KeystrokeSimulatorGUI(root)
    
    # Handle window closing
    def on_closing():
        if app.is_running:
            app.stop_simulation()
            time.sleep(0.5)  # Give time for cleanup
        root.destroy()
    
    root.protocol("WM_DELETE_WINDOW", on_closing)
    
    # Start the GUI
    root.mainloop()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nApplication interrupted by user.")
        sys.exit(0)