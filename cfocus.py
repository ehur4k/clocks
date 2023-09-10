import time

def focus_timer(total_work_time, total_break_time):
    while True:
        print("工作时间：")
        countdown(total_work_time)
        print("休息时间：")
        countdown(total_break_time)

def countdown(minutes):
    seconds = minutes * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        seconds -= 1
    print("00:00")

if __name__ == "__main__":
    total_work_time = 25  # 工作时间，以分钟为单位
    total_break_time = 5  # 休息时间，以分钟为单位
    focus_timer(total_work_time, total_break_time)
