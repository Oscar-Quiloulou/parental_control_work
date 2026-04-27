import psutil
from utils import is_work_time

def enforce_rules(rules):
    if not is_work_time(rules["work_periods"]):
        return

    blacklist = [p.lower() for p in rules["blacklist"]]

    for proc in psutil.process_iter(["name"]):
        try:
            name = proc.info["name"].lower()
            if name in blacklist:
                proc.terminate()
        except:
            pass
