import threading
import time
import os
import sys

def start_watchdog():
    def watchdog():
        while True:
            if not os.path.exists("main.py"):
                os.execv(sys.executable, ['python'] + sys.argv)
            time.sleep(5)

    threading.Thread(target=watchdog, daemon=True).start()
