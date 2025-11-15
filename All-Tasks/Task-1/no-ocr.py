import pyautogui
import time
from plyer import notification

def simple_monitor():
    print("Simple screen monitor running...")
    
    while True:
        # Just screenshot save karein (optional)
        pyautogui.screenshot('screenshot.png')
        
        # Simple notification
        notification.notify(
            title="Monitor Running",
            message="Screen monitoring active",
            timeout=5
        )
        
        time.sleep(3)  # 30 seconds

simple_monitor()