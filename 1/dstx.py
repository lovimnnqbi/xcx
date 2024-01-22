import time
import os

def set_reminder(reminder_time, reminder_message):
    while True:
        current_time = time.strftime("%H:%M:%S")
        if current_time == reminder_time:
            print(reminder_message)
            break
        time.sleep(1)

if __name__ == "__main__":
    reminder_time = input("请输入提醒时间（格式：HH:MM:SS）：")
    reminder_message = input("请输入提醒内容：")
    set_reminder(reminder_time, reminder_message)
