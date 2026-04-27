import time
from config_loader import load_rules
from process_watcher import enforce_rules
from notifier import check_and_warn
from watchdog import start_watchdog

CONFIG_URL = "https://raw.githubusercontent.com/oscar-quiloulou/parental_control_work/main/remote_config/rules.json"

def main():
    start_watchdog()

    rules = load_rules(CONFIG_URL)

    while True:
        rules = load_rules(CONFIG_URL)
        check_and_warn(rules)
        enforce_rules(rules)
        time.sleep(3)

if __name__ == "__main__":
    main()
