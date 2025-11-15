import pyautogui
import pytesseract
import tkinter as tk
from tkinter import messagebox

# iske path ko set karna jaruri hai bina isake error dega.
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def read_screen():
    # Yah screen ki height or width leta hai.
    screen_width, screen_height = pyautogui.size()
    print(screen_width, screen_height)
    # yah left side ke 50% portion ko coverkarta hai.
    width = int(screen_width * 50 / 100)
    height = screen_height
    region = (0,0,width, height)
    print(f"Data Type of region:{type(region)}")

    screenshot = pyautogui.screenshot(region=region)
    
    # OCR text extraction,  Yah image se text ko extract karta hai.
    text = pytesseract.image_to_string(screenshot)
    print(text)
    
    return text

def check_predefined_text():
    predefined_words = ["microsoft", "python", "Google","chrome"]
    screen_text = read_screen()
    
    for word in predefined_words:
        if word.lower() in screen_text.lower():
            show_popup(f"Found: {word}")
            break

def show_popup(message):
    # Using tkinter for popup
    root = tk.Tk()
    root.attributes('-topmost', True)   # isase pop-up top pe dikhega.
    root.withdraw()  # Isase main window hide hoti hai or sirf Alert massage dikhata hai.
    messagebox.showinfo("Alert", message)
    root.destroy()

# Continuous monitoring
import time
while True:
    check_predefined_text()
    # time.sleep(1)  # Check every 5 seconds