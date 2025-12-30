"""When users post an update on social media,such as a URL, image, status update etc., other users in their network are able to view this new post on their news feed. Users can also see exactly when the post was published, i.e, how many hours, minutes or seconds ago.

Since sometimes posts are published and viewed in different time zones, this can be confusing. You are given two timestamps of one such post that a user can see on his newsfeed in the following format:

Day dd Mon yyyy hh:mm:ss +xxxx

Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them."""


def time_delta(t1,t2):
    time1 = toseconds(t1)
    time2 = toseconds(t2)
    return abs(time1-time2)

def toseconds(time):
    months = {"Jan": 31, "Feb": 28, "Mar": 31, "Apr": 30, "May": 31, "Jun": 30, "Jul": 31, "Aug": 31, "Sep": 30, "Oct": 31, "Nov": 30, "Dec":31}
    t = time.split()
    date = int(t[1])
    month = t[2]
    year = int(t[3])
    h,m,sec = map(int, t[4].split(":"))
    tz = t[5]

    sign = 1 if tz[0] == "+" else -1
    tz_sec = sign * (int(tz[1:3])*3600 + int(tz[3:]) * 60)
    time_sec = h * 3600 + m * 60 + sec - tz_sec

    y = year - 1
    leap = y // 4 - y // 100 + y // 400
    days = y * 365 + leap

    for mth in months:
        if(mth == month):
            break
        days += months[mth]
        if(mth == "Feb" and is_leap(year)):
            days +=1
    
    days += date - 1

    return (days * 24 * 60 * 60) + time_sec

def is_leap(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)