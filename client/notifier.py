import datetime
import threading
import tkinter as tk
from tkinter import messagebox

from utils import minutes_before_next_work

warning_sent = False

def show_popup(msg):
    def _popup():
        root = tk.Tk()
        root.withdraw()
        messagebox.showwarning("Attention", msg)
        root.destroy()
    threading.Thread(target=_popup).start()

def check_and_warn(rules):
    global warning_sent

    mins = minutes_before_next_work(rules["work_periods"])

    if mins is None:
        warning_sent = False
        return

    if 0 < mins <= rules["warning_minutes"] and not warning_sent:
        msg = rules["messages"]["warning"].replace("{min}", str(int(mins)))
        show_popup(msg)
        warning_sent = True
