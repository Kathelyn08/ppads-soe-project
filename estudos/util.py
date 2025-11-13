from datetime import date, datetime, timedelta

def week_range():
    now = datetime.now()
    week_start = (now - timedelta(days=now.weekday() + 1)).replace(hour=0, minute=0, second=0, microsecond=0)
    week_end = week_start + timedelta(days=6, hours=23, minutes=59, seconds=59)

    return week_start, week_end

def compact(dict):
    return {k: v for k, v in dict.items() if v is not None}

def exclude(dict, *keys):
    return {k: v for k, v in dict.items() if k not in keys}
