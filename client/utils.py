import datetime

def parse_time(t):
    h, m = map(int, t.split(":"))
    return h, m

def is_work_time(periods):
    now = datetime.datetime.now()
    for p in periods:
        h1, m1 = parse_time(p["start"])
        h2, m2 = parse_time(p["end"])
        start = now.replace(hour=h1, minute=m1, second=0)
        end = now.replace(hour=h2, minute=m2, second=0)
        if start <= now <= end:
            return True
    return False

def minutes_before_next_work(periods):
    now = datetime.datetime.now()
    mins_list = []

    for p in periods:
        h, m = parse_time(p["start"])
        start = now.replace(hour=h, minute=m, second=0)
        delta = (start - now).total_seconds() / 60
        if delta > 0:
            mins_list.append(delta)

    return min(mins_list) if mins_list else None
