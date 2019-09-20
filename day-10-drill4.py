import re
from datetime import datetime as dt

def cleanup(date):
    patterns = [
        r'(\d{1,2})-(\d{1,2})-(\d{4})$',
        r'(\d{4})-(\d{1,2})-(\d{1,2})$',
        r'(\d{4})-(\d{1,2})$',
        r'(\d{1,2})-(\d{4})$',
    ]

    try:
        return str(int(date))
    except ValueError:
        pass

    for pat in patterns:
        q = re.match(pat, date)
        if q:
            if pat == patterns[0]:
                year = re.sub(patterns[0], r'\3', date)
                month = re.sub(patterns[0], r'\2', date)
                day = re.sub(patterns[0],  r'\1', date)
                return '{0}-{1:0>2}-{2:0>2}'.format(year, month, day)
            if pat == patterns[1]:
                year = re.sub(patterns[1], r'\1', date)
                month = re.sub(patterns[1], r'\2', date)
                day = re.sub(patterns[1],  r'\3', date)
                return '{0}-{1:0>2}-{2:0>2}'.format(year, month, day)
            if pat == patterns[2]:
                year = re.sub(patterns[2], r'\1', date)
                month = re.sub(patterns[2], r'\2', date)
                return '{0}-{1:0>2}'.format(year, month)
            if pat == patterns[3]:
                year = re.sub(patterns[3], r'\2', date)
                month = re.sub(patterns[3], r'\1', date)
                return '{0}-{1:0>2}'.format(year, month)
            else:
                return date

def main():
    dates = 1858.0, '1-12-1963', '1945-2', '7-2018', '1789-7-14',
    for date in dates:
        print('in: {}  out: {}'.format(date, cleanup(date)))

if __name__ == "__main__":
    main()