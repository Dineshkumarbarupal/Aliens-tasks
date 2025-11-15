import pyautogui
import time
from tkinter import messagebox
import tkinter as tk

def check_for_colors_or_patterns():
    """Text detection ke bina simple color/pattern detection"""
    try:
        # Screenshot lete hain
        screenshot = pyautogui.screenshot()
        
        # Specific color check (example: red color for errors)
        width, height = screenshot.size
        
        # Kuch specific pixels check karein
        for x in [100, 500, 900]:
            for y in [100, 300, 500]:
                r, g, b = screenshot.getpixel((x, y))
                
                # Red color detection (example)
                if r > 200 and g < 100 and b < 100:
                    show_popup("Red color detected - Possible error!")
                    return True
                    
        return False
        
    except Exception as e:
        print(f"Error: {e}")
        return False

def show_popup(message):
    """Popup show karein"""
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)  # Always on top
    messagebox.showwarning("Screen Alert", message)
    root.destroy()

def simple_screen_monitor():
    """Simple screen monitoring"""
    print("Screen monitoring started... Press Ctrl+C to stop")
    
    try:
        while True:
            if check_for_colors_or_patterns():
                print("Alert triggered!")
            
            time.sleep(5)  # 5 seconds wait
            
    except KeyboardInterrupt:
        print("Monitoring stopped")

if __name__ == "__main__":
    simple_screen_monitor()