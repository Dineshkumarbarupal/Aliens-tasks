import pytesseract
import pyautogui
import time
import tkinter as tk
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def take_partial_screenshot(side='left', percentage=50):
    """Screen ke specific side ka screenshot lein"""
    screen_width, screen_height = pyautogui.size()
    
    if side == 'left':
        # Left 50% portion
        width = int(screen_width * percentage / 100)
        height = screen_height
        region = (0, 0, width, height)
    
    elif side == 'right':
        # Right 50% portion
        width = int(screen_width * percentage / 100)
        x_start = screen_width - width
        region = (x_start, 0, screen_width, screen_height)
    
    elif side == 'top':
        # Top 50% portion
        width = screen_width
        height = int(screen_height * percentage / 100)
        region = (0, 0, width, height)
    
    elif side == 'bottom':
        # Bottom 50% portion
        width = screen_width
        height = int(screen_height * percentage / 100)
        y_start = screen_height - height
        region = (0, y_start, width, screen_height)
    
    else:
        # Full screen
        region = None
    
    screenshot = pyautogui.screenshot(region=region)
    return screenshot

def read_partial_screen(side='left'):
    """Specific portion se text read karein"""
    try:
        screenshot = take_partial_screenshot(side)
        text = pytesseract.image_to_string(screenshot, lang='eng')
        return text.lower()
    except Exception as e:
        print(f"OCR Error: {e}")
        return ""

def check_predefined_text_in_portion(side='left'):
    """Specific portion mein predefined text check karein"""
    predefined_words = ["error", "fail", "warning", "success", "complete"]
    screen_text = read_partial_screen(side)
    
    print(f"Checking {side} side...")  # Debug info
    
    for word in predefined_words:
        if word in screen_text:
            return f"Found '{word}' in {side} side"
    return None

def show_force_popup(message):
    """Popup show karein"""
    root = tk.Tk()
    root.attributes('-topmost', True)
    root.overrideredirect(True)
    root.geometry("400x200+500+300")
    root.configure(bg='lightyellow')
    
    label = tk.Label(root, text="ALERT!", font=("Arial", 16, "bold"), 
                    bg='lightyellow', fg='red')
    label.pack(pady=10)
    
    msg_label = tk.Label(root, text=message, font=("Arial", 12), 
                        bg='lightyellow', wraplength=350)
    msg_label.pack(pady=10)
    
    btn = tk.Button(root, text="Close", command=root.destroy, 
                   font=("Arial", 10), bg='red', fg='white')
    btn.pack(pady=10)
    
    root.lift()
    root.focus_force()
    root.grab_set()
    root.mainloop()

def start_monitoring():
    print("Partial Screen Monitoring Started...")
    print("Monitoring: Left 50% and Right 50% portions")
    
    try:
        while True:
            # Left side check
            left_result = check_predefined_text_in_portion('left')
            if left_result:
                print(f"ALERT: {left_result}")
                show_force_popup(left_result)
            
            # Right side check  
            right_result = check_predefined_text_in_portion('right')
            if right_result:
                print(f"ALERT: {right_result}")
                show_force_popup(right_result)
            
            time.sleep(10)
            
    except KeyboardInterrupt:
        print("Monitoring stopped!")

if __name__ == "__main__":
    start_monitoring()